                        importScripts("/assets/js/workbox-v3.6.3/workbox-sw.js");
            workbox.setConfig({modulePathPrefix: "/assets/js/workbox-v3.6.3"});

            self.__precacheManifest = [{"url":"/index.html","revision":"6c4e82caa2e3e5a03dcd3e0ef83e2b57"},{"url":"/blog/one-year-at-the-broad/","revision":"33cb61f4b9757cdde58d4833de3697a1"},{"url":"/blog/umap-explanation/","revision":"eb4fd5df474a46d6e63f85b5c1023169"},{"url":"/blog/a-month-at-the-broad/","revision":"7e1162d5efe505705b81d545c64e2d35"},{"url":"/blog/interviews-at-epfl/","revision":"ebf4663cb078b5a720dc39fad91deedb"},{"url":"/blog/broadinstitute-interview/","revision":"10f5a1c24e6f4b6538d2a949eb69faef"}];
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
