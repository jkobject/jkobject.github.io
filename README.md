# jkobject.github.io
Jkobject's website

## plugins
 - [jekyll admin](https://github.com/jekyll/jekyll-admin)
 - [jekyll](https://jekyllrb.com)
 - [jekyll-paginate](https://github.com/sverrirs/jekyll-paginate-v2)
 - jekyll-sitemap
 - jekyll-gist
 - [jekyll-feed](https://github.com/jekyll/jekyll-feed)
 - [jemoji](https://github.com/jekyll/jemoji)
 - jekyll-figure
 - minimal-mistakes-jekyll
 - [jekyll-seo-tag](https://github.com/jekyll/jekyll-seo-tag)
 - [jekyll-toc](https://github.com/toshimaru/jekyll-toc)
 - [jekyll-scholar](https://github.com/inukshuk/jekyll-scholar)
 - [amp-jekyll](https://github.com/juusaw/amp-jekyll)
 - [jekyll-gist](https://github.com/jekyll/jekyll-gist)
 - [jekyll-maps](https://github.com/ayastreb/jekyll-maps)
 - [jekyll-pwa-plugin](https://github.com/lavas-project/jekyll-pwa)
 - [jekyll-display-medium-posts](https://github.com/jameshamann/jekyll-display-medium-posts)

## about

This is my website which showcase anything directly related to me: Jérémie Kalfon.

the website is divided into topics which speak about different things
COLLECTIONS some of them have many different posts. they are called collections
AGREGATORS some of them are only here to gather some data under one view. they are called agregators
LINKERS some of them are unique page which present and links to other websites. they are called linkers


\_bibliography : It contains .bib files where I display the bibliography for specific posts.
\_drafts: Where I put the unfinished posts or files
\_data: Where some website specific data files are placed
\_posts: Where each post is put
\_pages: Where the website architectural files are placed
\_site: Where the actual website is compiled
archive: Where the previous website exists
assests: Where the images and documents are placed

## install

install jekyll and bundler:

- https://jekyllrb.com/docs/installation/
- https://bundler.io/

then do:

`bundle install`

then run it with:

`bundle exec jekyll serve`

## publish

to push a new version, just do:
`bundle update && bundle exec jekyll build && git add . && git commit -m 'new site version' && git push`

## legal

Any content in this website is strictly belonging to Jérémie Kalfon.
The templates and architecture might be reused at will.

## previously

-made in a couple of hours to display my professional life and maybe some personal posts
-used MDL

-the website itself is under a basic apache license but each project or paper has its own rights and terms
-please use it accordingly


https://lingojam.com/🐌EmojiTranslator🎲

## Example data

```markdown
---
date:
title: "Home"
layout: default
permalink
excerpt: "This is the Home of my website."
id: 
sitemap: true
category: 
published: true
header:
  image:
  caption:

	video:
    id: XsxDH4HcOWA
    provider: youtube # vimeo google-drive

  overlay_image: /assets/images/unsplash-image-1.jpg
  overlay_filter: rgba(255, 0, 0, 0.5)
  caption: "Photo credit: [**Unsplash**](https://unsplash.com)"
  actions:
    - label: "Download"
      url: "https://github.com"

  og_image:

footer:
sidebar:
  - title: "Title"
    image: http://placehold.it/350x250
    image_alt: "image"
    text: "Some text here."
  - title: "Another Title"
    text: "More text here."

  nav: "docs"


gallery:
  - url: /assets/images/unsplash-gallery-image-1.jpg
    image_path: /assets/images/unsplash-gallery-image-1-th.jpg
    alt: "placeholder image 1"
    title: "Image 1 title caption"
  - url: /assets/images/unsplash-gallery-image-2.jpg
    image_path: /assets/images/unsplash-gallery-image-2-th.jpg
    alt: "placeholder image 2"
    title: "Image 2 title caption"
  - url: /assets/images/unsplash-gallery-image-3.jpg
    image_path: /assets/images/unsplash-gallery-image-3-th.jpg
    alt: "placeholder image 3"
    title: "Image 3 title caption"

tags: 
 - blog
 - lifestyle
 - science
 - bio
 - biology
 - genomics
 - ML
 - AI
 - ideas
toc: true
toc_label: "table of content"
toc_icon:
toc_sticky: false
canonical_url:
skip_amp: false
location:
	latitude: 51.5285582
	longitude: -0.2416807
	title: custom marker title
<!-- other any food: Pizza)-->

---
{% seo %}
{% if page.path contains '_posts' %}
  <link rel="amphtml" href="{{ page.id | prepend: '/YOURDIR' | prepend: site.baseurl | prepend: site.url | append: '.html' }}">
{% endif %}

{{ content | toc }}

{% gist c08ee0f2726fd0e3909d %}

{% include gallery caption="This is a sample gallery with **Markdown support**." %}

{% include video id="XsxDH4HcOWA" provider="youtube" %}


{% google_map %}
{% google_map src="_posts/2016" %}

{% bibliography --file secondary %}
{% if entry.abstract %}
<p>{{ entry.abstract }}</p>
{% endif %}

<pre>{{ entry.bibtex }}</pre>

This is a sample post with a large feature image[^1] up top and tons of text. Odio 

[^1]: Texture image courtesty of [Lovetextures](http://www.lovetextures.com/)


**[Terry Richardson](#) shabby chic +1**

  * Sartorial hoodie
  * Labore viral forage
  * Tote bag selvage
  * DIY exercitation et id ugh tumblr church-key

> Whatever velit occaecat quis deserunt gastropub, leggings elit tousled roof party 3 

Alt-H1
======

Alt-H2
------

# H1
## H2
### H3
#### H4
##### H5
###### H6

Emphasis, aka italics, with *asterisks* or _underscores_.

Strong emphasis, aka bold, with **asterisks** or __underscores__.

Combined emphasis with **asterisks and _underscores_**.

Strikethrough uses two tildes. ~~Scratch this.~~

1. First ordered list item
2. Another item
  * Unordered sub-list. 
1. Actual numbers don't matter, just that it's a number
  1. Ordered sub-list
4. And another item.  
   
   Some text that should be aligned with the above item.

* Unordered list can use asterisks
- Or minuses
+ Or pluses


Markdown | Less | Pretty
--- | --- | ---
*Still* | `renders` | **nicely**
1 | 2 | 3

$-b \pm \sqrt{b^2 - 4ac} \over 2a$
$x = a_0 + \frac{1}{a_1 + \frac{1}{a_2 + \frac{1}{a_3 + a_4}}}$
$\forall x \in X, \quad \exists y \leq \epsilon$


-----


____


<div class="row">
  <div class="col-md-8" markdown="1">
  Some text.
  </div>
  <div class="col-md-4" markdown="1">
  <!-- ![Alt Text](../img/folder/blah.jpg) -->
  <img height="600px" class="center-block" src="../img/folder/blah.jpg">
  </div>
</div>

```

```javascript
var s = "JavaScript syntax highlighting";
alert(s);
```
 
```python
s = "Python syntax highlighting"
print s
```
 
```
No language indicated, so no syntax highlighting. 
But let's throw in a <b>tag</b>.
```





## Debug 


- sharing social media
- links in about
- parenthesis in about

## TODO

- add more images and link in my description in about 
- have wiki preview for role models https://github.com/aleks/jekyll_preview_tag
- have better book and paper citation model https://github.com/aleks/jekyll_preview_tag
- add papers that I have not yet read.. (https://rmarkdown.rstudio.com/authoring_bibliographies_and_citations.html)


```css
/*Chrome*/
@media screen and (-webkit-min-device-pixel-ratio:0) {
    input[type='range'] {
      overflow: hidden;
      width: 80px;
      -webkit-appearance: none;
      background-color: #9a905d;
    }
    
    input[type='range']::-webkit-slider-runnable-track {
      height: 10px;
      -webkit-appearance: none;
      color: #13bba4;
      margin-top: -1px;
    }
    
    input[type='range']::-webkit-slider-thumb {
      width: 10px;
      -webkit-appearance: none;
      height: 10px;
      cursor: ew-resize;
      background: #434343;
      box-shadow: -80px 0 0 80px #43e5f7;
    }

}
/** FF*/
input[type="range"]::-moz-range-progress {
  background-color: #43e5f7; 
}
input[type="range"]::-moz-range-track {  
  background-color: #9a905d;
}
/* IE*/
input[type="range"]::-ms-fill-lower {
  background-color: #43e5f7; 
}
input[type="range"]::-ms-fill-upper {  
  background-color: #9a905d;
}
<input type="range" disabled="disabled"
value="80"/>
or maybe "readonly"
```


contact :  jkobject@gmail.com 
MIT LICENCE ®
