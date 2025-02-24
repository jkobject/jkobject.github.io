                        importScripts("/assets/js/workbox-v3.6.3/workbox-sw.js");
            workbox.setConfig({modulePathPrefix: "/assets/js/workbox-v3.6.3"});

            self.__precacheManifest = [{"url":"/index.html","revision":"decdc635cc51a23f6e01d138b8c0603a"},{"url":"/blog/a-year-in-the-phd/","revision":"42bcf5e3bc7d19c5efce65e187197f14"},{"url":"/blog/the-phd-decision-grn-foundation-model/","revision":"7e1bd02c8d9605b2a9ea95a30fc325bf"},{"url":"/blog/WhitelabGx-and-being-team-lead-redacted/","revision":"983030b3ffebea3bfe737bbabaf0dcb9"},{"url":"/blog/the-aqemia-story-redacted/","revision":"f4d9b5540b05f386289f5f58a4645fcf"},{"url":"/blog/leaving-broad/","revision":"3a31f8cdfda387eb04047a6558e111be"}];
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
