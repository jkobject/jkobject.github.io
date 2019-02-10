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
tags: ["blog","lifestyle","science","bio","biology","genomics","ML","AI","ideas"]
image:
toc: true
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

{% google_map %}
{% google_map src="_posts/2016" %}

{% bibliography --file secondary %}
{% if entry.abstract %}
<p>{{ entry.abstract }}</p>
{% endif %}

<pre>{{ entry.bibtex }}</pre>