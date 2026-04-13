                        importScripts("/assets/js/workbox-v3.6.3/workbox-sw.js");
            workbox.setConfig({modulePathPrefix: "/assets/js/workbox-v3.6.3"});

            self.__precacheManifest = [{"url":"/index.html","revision":"008f0167c2db84654510950e4de7a703"},{"url":"/blog/vcc-starter-pack/","revision":"306b2da00f21394ac3534d20395809ca"},{"url":"/blog/a-year-in-the-phd/","revision":"80b704022807a65afa296c618547a558"},{"url":"/blog/finishing-the-phd/","revision":"78ff0f58d8fbd42d94f29f1638ed2d8a"},{"url":"/blog/about-the-aivc-paper/","revision":"16147e620d3ed7ba6d7468c31d04ac71"},{"url":"/blog/what-are-large-cell-models/","revision":"a03c3c83a5ed3cfffda6506b2f6d6f9a"}];
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
