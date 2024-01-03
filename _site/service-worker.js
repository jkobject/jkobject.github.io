                        importScripts("/assets/js/workbox-v3.6.3/workbox-sw.js");
            workbox.setConfig({modulePathPrefix: "/assets/js/workbox-v3.6.3"});

            self.__precacheManifest = [{"url":"/index.html","revision":"6ce75034d4f57eea57e3ffdd3ee0c211"},{"url":"/blog/the-final-decision-phd-grn-foundation-model/","revision":"d74d33e241a2feb185f7d0a55162e1f2"},{"url":"/blog/WhitelabGx-and-being-team-lead-redacted/","revision":"9e5310934b8465063b110527ee2c8f75"},{"url":"/blog/the-aqemia-story-redacted/","revision":"ae78efb7a216cf378afa97c2806e1d40"},{"url":"/blog/leaving-broad/","revision":"3a31f8cdfda387eb04047a6558e111be"},{"url":"/blog/DepMap-lessons-learned/","revision":"654b22be99468efa76ca217b848cd688"}];
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
