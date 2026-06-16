# jkobject.github.io agent notes

## Workspace

Use this repository path for all edits:

```bash
/home/ubuntu/workspace/work/jkobject.github.io
```

It resolves to the OpenClaw workspace checkout:

```bash
/home/ubuntu/.openclaw/workspace/work/jkobject.github.io
```

Do not place working files directly in `/home/ubuntu`; keep drafts, sources, and assets inside the repo or another existing workspace/project directory.

## Build / validation

`bundle` and `jekyll` are not on the global PATH. The working OpenClaw setup uses the vendored executables in `vendor/bundle/ruby/3.3.0/bin`.

From the repo root:

```bash
export PATH="$PWD/vendor/bundle/ruby/3.3.0/bin:$PATH"
export BUNDLE_PATH="$PWD/vendor/bundle"
bundle exec jekyll build
```

Expected successful build output includes:

```text
Configuration file: .../_config.yml
Remote Theme: Using theme mmistakes/minimal-mistakes
Jekyll Feed: Generating feed for posts
done in ... seconds.
```

Warnings like this are harmless deprecation warnings from the Ruby/gem stack:

```text
Calling `DidYouMean::SPELL_CHECKERS.merge!(...)` has been deprecated
```

## Publishing

When the user explicitly asks to publish/push:

```bash
git status --short
git add .
git commit -m "<clear message>"
git push origin master
```

The repo tracks generated `_site/` files, so after `bundle exec jekyll build`, review and include the relevant `_site/` changes in the commit unless there is a specific reason not to.

## Home page

The homepage uses `_layouts/home.html`. Recent entries should include multiple collections, not only blog posts:

```liquid
site.posts | concat: site.ideas | concat: site.opinions | concat: site.projects
```

Sort by `date`, reverse, then render with `_includes/archive-single.html`.
