---
title: "A Startup idea to accelerate the transition to smart-things"
excerpt:
  "The technology is there but the changes are slow and often at cause radical
  changes in the distribution of market actors."
category: "Frustrations and Solutions"
---

Last time, I was in my kitchen, looking at my google home and the 3 lights +
thermostat it was able to control. I felt quite underwhelmed with the effort I
had to go through to find and install these. Amongst the many objects in my
home, there is still a few, mostly expansive objects that I could call "smart".
10 years after the beginning of the smaart things revolution. 60 years after the
first ideas of the smart home. Why so little progress? Why is it so expansive?
why do I always need yet another app, yet another complex IFTTT API to just be
able to turn off my light bulb from my phone?

## The obvious reasons

The core issue is fragmentation — and it runs deep. Walk into any electronics
store and you'll find lights talking Zigbee, locks running Z-Wave, thermostats
on their own proprietary Wi-Fi protocol, and plugs that only work inside their
brand's walled garden. Each of these companies built a separate kingdom, and
none of them particularly want to talk to each other.

Part of the problem is structural: appliance manufacturers are hardware
companies. They make washing machines, ovens, and door locks. They don't make
phones, and they don't have the software culture to ship great apps or APIs.
So when they bolt a Wi-Fi chip onto their product and call it "smart", what you
get is a barely-maintained app, a cloud service that might disappear in three
years, and zero interoperability with anything else in your home.

The other issue is that making something truly smart usually means disrupting an
existing market. Smart locks threaten locksmiths. Smart thermostats threaten
HVAC installers. Every company entering this space has to fight entrenched
incumbents who profit from the current complexity. That friction slows everything
down.

## The solutions

The open source community got tired of waiting. Home Assistant, now one of the
most active open source projects in the world, basically built a universal
translator for smart home devices. It runs on a Raspberry Pi in your closet and
lets you connect everything — Zigbee, Z-Wave, MQTT, cloud APIs — into one
coherent system. It's powerful, but it's also deeply technical. Setting it up is
not something your parents will do on a Sunday afternoon.

On the corporate side, some big players are finally making the right moves. IKEA
deserves credit here: they've been quietly building an affordable, Zigbee-based
smart home lineup that actually works — and they're not trying to lock you into
an IKEA cloud subscription to use your lightbulbs. That's rare.

The most promising development of 2022 is Matter — a new open standard backed by
Apple, Google, Amazon, and Samsung. The idea is simple: one protocol to rule
them all. A Matter-certified device should work with any Matter controller, no
matter who made it. The first version launched in October 2022, and while it's
still early days, it's the first time I've felt genuinely optimistic about the
smart home space. But standards take decades to fully roll out, and the current
device selection is still thin.

Which brings me to the gap in the market.

## The company

Here's the startup idea: a company that only does smart things — and does it
right.

Not a platform play. Not another hub. A vertically integrated company that
manufactures and sells a curated line of smart home products built on open
standards (Matter, Zigbee, or Thread), with a single, beautiful app, and an
explicit commitment to local-first control. No cloud required to turn on your
lights. No subscription to keep your thermostat working. No data harvested from
your home.

The value proposition is simple: you shouldn't need to be a home automation
enthusiast to have a smart home that actually works. This company would cover the
full stack — from the hardware design to the firmware to the UX — with the same
obsessive attention that Apple brought to the iPhone. Premium pricing is fine;
people will pay for things that just work.

The timing is good. Matter lowers the technical barrier. Consumers are frustrated
with fragmentation. The open source community has already proven the demand. What
the market is missing is someone willing to make it boring, reliable, and
beautiful — all at once.

---

*Further reading:*

- [67 open source tools for IoT](https://techbeacon.com/app-dev-testing/67-open-source-tools-resources-iot)
- [SmartThings Community on GitHub](https://github.com/SmartThingsCommunity)
