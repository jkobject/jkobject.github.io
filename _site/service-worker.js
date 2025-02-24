                        importScripts("/assets/js/workbox-v3.6.3/workbox-sw.js");
            workbox.setConfig({modulePathPrefix: "/assets/js/workbox-v3.6.3"});

            self.__precacheManifest = [{"url":"/index.html","revision":"ed89862f6d9ade556b32c012218e488e"},{"url":"/blog/about-the-aivc-paper/","revision":"ef3da42a74254acf22beba088a200033"},{"url":"/blog/a-year-in-the-phd/","revision":"2a79aef5f1e4fb8ce96b77b8a7ceb71c"},{"url":"/blog/what-are-large-cell-models/","revision":"a03c3c83a5ed3cfffda6506b2f6d6f9a"},{"url":"/blog/ancestry-bias-in-crispr/","revision":"30c469109b64cd6a27b5b7a443f6a6ff"},{"url":"/blog/manage-grn-and-what-they-mean/","revision":"f806a40d529a4a690f757e04a24a8f4a"}];
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
