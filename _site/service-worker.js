                        importScripts("/assets/js/workbox-v3.6.3/workbox-sw.js");
            workbox.setConfig({modulePathPrefix: "/assets/js/workbox-v3.6.3"});

            self.__precacheManifest = [{"url":"/index.html","revision":"c9aadc4a0cdde387a40cdaf82ed3dd5d"},{"url":"/blog/gene-regulation-landscape/","revision":"517f8352936231ebc716c78ffcc1aac8"},{"url":"/blog/finishing-the-phd/","revision":"33e6878e58ca24d2741af39b5c77b05d"},{"url":"/blog/lamindb-these/","revision":"fae046d50e720c7e5460195971bc7ee0"},{"url":"/blog/vcc-starter-pack/","revision":"306b2da00f21394ac3534d20395809ca"},{"url":"/blog/a-year-in-the-phd/","revision":"4f3d101095d5ac2bfd5dee2b9a815f7a"}];
            // service-worker.js

// set names for both precache & runtime cache
workbox.core.setCacheNameDetails({
    prefix: 'my-blog',
    suffix: 'v1',
    precache: 'precache',
    runtime: 'runtime-cache'
});

// let Service Worker take control of pages ASAP
workbox.skipWaiting();
workbox.clientsClaim();

// let Workbox handle our precache list
workbox.precaching.precacheAndRoute(self.__precacheManifest);

// use `networkFirst` strategy for `*.html`, like all my posts
workbox.routing.registerRoute(
    /\.html$/,
    workbox.strategies.networkFirst()
);

// use `cacheFirst` strategy for images
workbox.routing.registerRoute(
    /assets\/(img|icons)/,
    workbox.strategies.cacheFirst()
);

// third party files
workbox.routing.registerRoute(
    /^https?:\/\/cdn.staticfile.org/,
    workbox.strategies.staleWhileRevalidate()
);
