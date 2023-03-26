                        importScripts("/assets/js/workbox-v3.6.3/workbox-sw.js");
            workbox.setConfig({modulePathPrefix: "/assets/js/workbox-v3.6.3"});

            self.__precacheManifest = [{"url":"/index.html","revision":"1b1dd7eccf18e8d41355ed9242ae3976"},{"url":"/blog/two-years-at-the-broad/","revision":"edc55277b7c1b3495a2abee43daab7f9"},{"url":"/blog/cds-presentation/","revision":"e4354877adf55e05b331b5f4ca7fe602"},{"url":"/blog/one-year-at-the-broad/","revision":"322203920b135bd70f006f67c0366989"},{"url":"/blog/umap-explanation/","revision":"eb4fd5df474a46d6e63f85b5c1023169"},{"url":"/blog/a-month-at-the-broad/","revision":"7e1162d5efe505705b81d545c64e2d35"}];
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
