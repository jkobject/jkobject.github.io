                        importScripts("/assets/js/workbox-v3.6.3/workbox-sw.js");
            workbox.setConfig({modulePathPrefix: "/assets/js/workbox-v3.6.3"});

            self.__precacheManifest = [{"url":"/index.html","revision":"e385d9f161619fee661b3509843c9e5e"},{"url":"/blog/umap-explanation/","revision":"afde3b3c6cdca2a08f42d7ac3657bf19"},{"url":"/blog/a-month-at-the-broad/","revision":"6d920c7dbfc49674c36831ce2928c718"},{"url":"/blog/interviews-at-epfl/","revision":"21dad48e3275677b5d05213a98403e73"},{"url":"/blog/broadinstitute-interview/","revision":"739ba1e7b2846d6aa60dcda1f5cfc66e"},{"url":"/blog/interviews-in-cambridge/","revision":"bb4f8f4d3813b0c5756a619ee9820e61"}];
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
