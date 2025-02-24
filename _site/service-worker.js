                        importScripts("/assets/js/workbox-v3.6.3/workbox-sw.js");
            workbox.setConfig({modulePathPrefix: "/assets/js/workbox-v3.6.3"});

            self.__precacheManifest = [{"url":"/index.html","revision":"80d374268a32d8d69e3768af76f9c5f4"},{"url":"/blog/about-the-aivc-paper/","revision":"ef3da42a74254acf22beba088a200033"},{"url":"/blog/what-are-large-cell-models/","revision":"a03c3c83a5ed3cfffda6506b2f6d6f9a"},{"url":"/blog/ancestry-bias-in-crispr/","revision":"30c469109b64cd6a27b5b7a443f6a6ff"},{"url":"/blog/manage-grn-and-what-they-mean/","revision":"f806a40d529a4a690f757e04a24a8f4a"},{"url":"/blog/auprc-vs-ap/","revision":"eb2e5db27c3ed3a8cb4e53797e38e2c0"}];
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
