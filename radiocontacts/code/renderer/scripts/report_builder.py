# /// script
# requires-python = ">=3.11"
# dependencies = ["Markdown==3.8.2", "beautifulsoup4==4.13.4", "plotly==6.3.0"]
# ///
"""Build one shareable HTML scientific report from trusted, author-owned sources."""

from base64 import b64encode
from hashlib import sha256
from html import escape
import json
import mimetypes
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

from bs4 import BeautifulSoup
import markdown

ASSETS = Path(__file__).resolve().parents[1] / "assets"


def _data_url(name: str, content: bytes) -> str:
    """Encode a local attachment without requiring a companion download file."""
    mime = mimetypes.guess_type(name)[0] or "application/octet-stream"
    return f"data:{mime};base64," + b64encode(content).decode("ascii")


def _embed_resources(content: str, source: Path, attachments: dict[str, bytes]) -> str:
    """Embed local figures/downloads and reject unsupported runtime dependencies.

    Ordinary HTTPS bibliography links stay navigable. Authored JavaScript,
    iframes, stylesheets, srcset and remote media are rejected rather than
    silently producing an HTML file that still needs a network or sidecar.
    """
    soup = BeautifulSoup(content, "html.parser")
    for element in soup.find_all(True):
        if element.name in {
            "script",
            "style",
            "link",
            "iframe",
            "object",
            "embed",
            "base",
        } or element.has_attr("srcset"):
            raise ValueError(f"Unsupported authored runtime element: {element.name}")
        for attribute in element.attrs:
            if attribute.lower().startswith("on") or (
                attribute == "style"
                and re.search(r"url\s*\(|@import", element["style"], re.I)
            ):
                raise ValueError(
                    "Use the report runtime/theme instead of inline executable resources"
                )
        for attribute in ("src", "href", "poster"):
            if not element.has_attr(attribute):
                continue
            value = element[attribute]
            if value.startswith("#"):
                continue
            url = urlsplit(value)
            if url.scheme or url.netloc:
                if value.startswith("data:") or (
                    element.name == "a" and url.scheme in {"https", "http", "mailto"}
                ):
                    continue
                raise ValueError(
                    f"External runtime dependency is not portable: {value}"
                )
            name = unquote(url.path)
            if url.query or url.fragment or not name:
                raise ValueError(
                    f"Local resources must be plain relative file paths: {value}"
                )
            if name in attachments:
                data = attachments[name]
            else:
                path = (source / name).resolve()
                if not path.is_relative_to(source.resolve()):
                    raise ValueError(f"Resource escapes the source directory: {name}")
                data = path.read_bytes()
            # SVG can load nested external assets or execute handlers. Inline SVG
            # markup is rejected below; raster figures are the supported input.
            if element.name != "a" and Path(name).suffix.lower() not in {
                ".png",
                ".jpg",
                ".jpeg",
                ".gif",
                ".webp",
                ".avif",
            }:
                raise ValueError(f"Use a raster figure for embedded media: {name}")
            element[attribute] = _data_url(name, data)
            if element.name == "a":
                element["download"] = Path(name).name
    if soup.find("svg"):
        raise ValueError(
            "Use a raster figure or a generated Plotly chart instead of authored SVG"
        )
    return str(soup)


def render_report(
    source: Path,
    output: Path,
    metadata: dict,
    plots: dict,
    attachments: dict[str, bytes] | None = None,
) -> Path:
    """Render a document/presentation report into exactly one self-contained HTML.

    Parameters
    ----------
    source : Path
        Directory containing report.md and optional report.css/report.js overrides.
        Local figure and download paths resolve here, or through attachments.
    output : Path
        Destination .html file (or directory, to produce index.html).
    metadata : dict
        title, subtitle, author, date, version and references keyed by stable ID.
        Extra provenance fields are embedded unchanged in the metadata JSON.
    plots : dict
        Plot IDs mapped to named variants with label, data, layout and caption.
    attachments : dict[str, bytes], optional
        Download paths used in the Markdown, mapped to their exact bytes. Figures
        may also come from here. build.json and report.md are reserved exports.

    Returns
    -------
    Path
        The only file written. It embeds CSS, JavaScript, Plotly (if used), plot
        JSON, metadata, source Markdown, local figures and referenced downloads.
        Scientific calculations are the caller's responsibility.
    """
    source, output = Path(source), Path(output)
    if output.suffix.lower() != ".html":
        output = output / "index.html"
    if output.resolve() == (source / "report.md").resolve():
        raise ValueError("Do not overwrite authored source")
    text = (source / "report.md").read_text(encoding="utf-8")
    if re.search(r"%%[A-Z_]+%%|\[TODO[^\]]*\]", text):
        raise ValueError("Unfinished report placeholder")
    css_path = (
        source / "report.css"
        if (source / "report.css").exists()
        else ASSETS / "report.css"
    )
    js_path = (
        source / "report.js"
        if (source / "report.js").exists()
        else ASSETS / "report.js"
    )
    css, runtime = css_path.read_text(), js_path.read_text()
    if re.search(r"url\s*\(|@import", css, re.I):
        raise ValueError(
            "Theme CSS must not load external resources; use system fonts and embedded figures"
        )
    content = markdown.markdown(
        text, extensions=["tables", "md_in_html", "attr_list", "fenced_code"]
    )
    soup = BeautifulSoup(content, "html.parser")
    sections = soup.find_all("section", recursive=False)
    if not sections or any(
        not section.get("id") or not section.find("h2") for section in sections
    ):
        raise ValueError("Each report section needs a stable id and an h2 heading")
    reserved = {
        "report",
        "toc",
        "plot-data",
        "report-metadata",
        "source-markdown",
        "bibliography",
        "document-mode",
        "presentation-mode",
        "slide-controls",
        "previous",
        "next",
        "slide-status",
    }
    ids = [element["id"] for element in soup.select("[id]")]
    if len(ids) != len(set(ids)) or set(ids) & reserved:
        raise ValueError("Duplicate or reserved document IDs")
    for table in soup.find_all("table"):
        if "table-wrap" not in table.parent.get("class", []):
            wrapper = soup.new_tag("div", attrs={"class": "table-wrap"})
            table.wrap(wrapper)
    references = metadata.get("references", {})
    citation_ids = list(
        dict.fromkeys(element["data-cite"] for element in soup.select("[data-cite]"))
    )
    if set(citation_ids) - references.keys():
        raise ValueError("Missing reference definitions")
    for element in soup.select("[data-cite]"):
        key = element["data-cite"]
        if not re.fullmatch(r"[a-zA-Z0-9_-]+", key):
            raise ValueError(f"Invalid citation ID: {key}")
        index = citation_ids.index(key) + 1
        element.name = "a"
        element["href"] = "#ref-" + key
        element["class"] = [*element.get("class", []), "citation"]
        element["aria-label"] = f"Reference {index}"
        element.string = f"[{index}]"
    plot_ids = [element["data-plot"] for element in soup.select("[data-plot]")]
    if set(plot_ids) != plots.keys() or len(plot_ids) != len(set(plot_ids)):
        raise ValueError("Plot placeholders must uniquely match plot definitions")
    for plot_id, variants in plots.items():
        if not variants or any(
            not {"label", "data", "layout", "caption"} <= variant.keys()
            for variant in variants.values()
        ):
            raise ValueError(f"Missing plot variant fields: {plot_id}")
        for variant in variants.values():
            # Geographic plots fetch tiles or topology; the single-file contract
            # supports charts whose inputs are entirely in the figure JSON.
            for trace in variant["data"]:
                if trace.get("type", "scatter") in {
                    "scattergeo",
                    "choropleth",
                    "scattermapbox",
                    "choroplethmapbox",
                    "densitymapbox",
                    "scattermap",
                    "choroplethmap",
                    "densitymap",
                }:
                    raise ValueError("Geographic plots require external resources")
            images = [*variant["layout"].get("images", []), *variant["data"]]
            if any(
                "source" in item and not str(item["source"]).startswith("data:")
                for item in images
            ):
                raise ValueError("Plot images must use embedded data URLs")
    bibliography = "".join(
        f'<li id="ref-{key}" data-reference="{key}" value="{i}"><a href="{escape(references[key]["url"], quote=True)}">{escape(references[key]["label"])}</a></li>'
        for i, key in enumerate(citation_ids, 1)
    )
    content = (
        str(soup)
        + f'<section id="bibliography"><h2>Bibliography</h2><ol>{bibliography}</ol></section>'
    )
    plot_json = json.dumps(plots, allow_nan=False, ensure_ascii=False).replace(
        "<", "\\u003c"
    )
    hashes = {
        "report.md": sha256(text.encode()).hexdigest(),
        "report.css": sha256(css.encode()).hexdigest(),
        "report.js": sha256(runtime.encode()).hexdigest(),
        "renderer": sha256(Path(__file__).read_bytes()).hexdigest(),
        "plots": sha256(plot_json.encode()).hexdigest(),
    }
    files = dict(attachments or {})
    if {"build.json", "report.md"} & files.keys():
        raise ValueError("build.json and report.md are reserved embedded exports")
    manifest = {
        "metadata": metadata,
        "sha256": hashes,
        "attachments_sha256": {
            name: sha256(data).hexdigest() for name, data in files.items()
        },
    }
    metadata_json = json.dumps(manifest, allow_nan=False, ensure_ascii=False).replace(
        "<", "\\u003c"
    )
    files.update({"build.json": metadata_json.encode(), "report.md": text.encode()})
    content = _embed_resources(content, source, files)
    checked = BeautifulSoup(content, "html.parser")
    targets = {element["id"] for element in checked.select("[id]")}
    if len(targets) != len(checked.select("[id]")):
        raise ValueError("Citation and document IDs collide")
    for link in checked.select('a[href^="#"]'):
        if link["href"][1:] not in targets:
            raise ValueError(f"Broken internal reference: {link['href']}")
    plot_script = ""
    if plots:
        from plotly.offline import get_plotlyjs

        plot_script = (
            "<script>"
            + re.sub(r"</script", r"<\\/script", get_plotlyjs(), flags=re.I)
            + "</script>"
        )
    runtime = re.sub(r"</script", r"<\\/script", runtime, flags=re.I)
    css = re.sub(r"</style", r"<\\/style", css, flags=re.I)
    title, subtitle, author, date, version = (
        escape(str(metadata.get(key, "")))
        for key in ["title", "subtitle", "author", "date", "version"]
    )
    first = escape(sections[0]["id"], quote=True)
    html = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><style>{css}</style></head><body><a class="skip-link" href="#report">Skip to report</a>
<header class="toolbar"><a class="brand" href="#{first}">RadioContacts</a>
<div class="mode-switch" role="group" aria-label="Reading mode"><button id="document-mode" aria-pressed="true">Document</button><button id="presentation-mode" aria-pressed="false">Presentation</button></div></header>
<div class="page"><aside><p class="eyebrow">Contents</p><nav id="toc" aria-label="Table of contents"></nav><p class="aside-note">{date}</p></aside><main id="report">
<div class="title-block"><h1>{title}</h1><p class="subtitle">{subtitle}</p><p class="byline">{author} · {date}</p></div>
<noscript><p>Enable JavaScript for interactive figures and presentation mode. The narrative and embedded source downloads remain available.</p></noscript>
{content}</main></div><footer id="slide-controls" hidden><button id="previous" aria-label="Previous slide">← Previous</button><span id="slide-status" role="status" aria-live="polite"></span><button id="next" aria-label="Next slide">Next →</button></footer>
<script id="plot-data" type="application/json">{plot_json}</script><script id="report-metadata" type="application/json">{metadata_json}</script>
<script id="source-markdown" type="application/json">{json.dumps(text, ensure_ascii=False).replace("<", chr(92) + "u003c")}</script>{plot_script}<script>{runtime}</script></body></html>"""
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(html, encoding="utf-8")
    return output
