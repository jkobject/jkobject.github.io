                        importScripts("/assets/js/workbox-v3.6.3/workbox-sw.js");
            workbox.setConfig({modulePathPrefix: "/assets/js/workbox-v3.6.3"});

            self.__precacheManifest = [{"url":"/index.html","revision":"c39f00284de744bf28020cebb6bcc545"},{"url":"/blog/interviews-at-epfl/","revision":"21dad48e3275677b5d05213a98403e73"},{"url":"/blog/broadinstitute-interview/","revision":"739ba1e7b2846d6aa60dcda1f5cfc66e"},{"url":"/blog/interviews-in-cambridge/","revision":"bb4f8f4d3813b0c5756a619ee9820e61"},{"url":"/blog/an-msc-at-the-univeristy-of-kent/","revision":"c3db6ee0bceecbd330d055ef655a7495"},{"url":"/blog/human-brain-project/","revision":"a271026cfaec3af67bcaa7de2ec47659"}];
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
