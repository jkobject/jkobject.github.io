---
title: "Accelerate the transition to smart-things"
excerpt:
  "Make a consulting firm that helps existing manufacturers add smart features to their products."
category: "Frustrations and Solutions"
date: 2022-12-10
---

Last time, I was in my kitchen, looking at my google home and the 3 lights +
thermostat it was able to control. I felt quite underwhelmed with the effort I
had to go through to find and install these. Amongst the many objects in my
home, there is still a few, mostly expansive objects that I could call "smart".
10 years after the beginning of the smart things revolution. 60 years after the
first ideas of the smart home. Why so little progress? Why is it so expansive?
why do I always need yet another app, yet another complex IFTTT API to just be
able to turn off my light bulb from my phone?

## The obvious reasons

The core issue is that the companies who make your stuff — your oven, your
doorbell, your desk lamp — are hardware companies. They've been making these
things for decades, sometimes centuries. They know materials, manufacturing,
supply chains. What they don't know is software, firmware, wireless protocols,
app design. And it shows.

Walk into any electronics store: lights talking Zigbee, locks running Z-Wave,
thermostats on their own proprietary Wi-Fi, plugs locked inside a brand's walled
garden. Each manufacturer bolts a Wi-Fi chip onto their product, ships a
barely-maintained app, stands up a cloud service that might disappear in three
years, and calls it "smart." The result is a mess — not because the hardware is
bad, but because these companies simply don't have the software DNA to do it
right.

And then there's the market structure problem. Making something truly smart
often means disrupting existing distribution channels. Smart locks threaten
locksmiths. Smart thermostats threaten HVAC installers. Every company entering
this space has to fight entrenched incumbents who profit from the current
complexity. That friction slows everything down.

## The solutions (so far)

Some people are trying to fix this from different angles.

The open source community got tired of waiting. Home Assistant, now one of the
most active open source projects in the world, basically built a universal
translator for smart home devices. It runs on a Raspberry Pi in your closet and
lets you connect everything — Zigbee, Z-Wave, MQTT, cloud APIs — into one
coherent system. It's powerful, but it's also deeply technical. Setting it up is
not something your parents will do on a Sunday afternoon. And it solves the
problem on the consumer side — it doesn't help manufacturers ship better
products in the first place.

On the corporate side, IKEA deserves credit: they've been quietly building an
affordable, Zigbee-based smart home lineup that actually works. But IKEA is the
exception — they have both the hardware scale and the tech ambition to pull it
off. Most manufacturers don't.

The most promising development is Matter — a new open standard backed by Apple,
Google, Amazon, and Samsung. One protocol to rule them all. A Matter-certified
device should work with any controller, no matter who made it. This is great for
interoperability. But here's the thing: having a standard doesn't mean
manufacturers can suddenly implement it. You still need people who understand
firmware, wireless stacks, app development, cloud architecture. The standard
lowers the protocol barrier, but the competence gap remains wide open.

Which is exactly where the opportunity is.

## The company

The default startup response to all this is: make a new brand of smart products.
Another startup making a smart mattress, a smart chair, a smart desk — selling
it at a huge markup because they had to build everything from scratch.

But that's the wrong approach. The manufacturers are already there. They already
know how to make a great lock, a great chair, a great oven. They just can't make
it talk to your phone.

So the startup idea is not "make smart things." It's: **help the people who
already make things make them smart.**

A consulting firm specialized in integrating smart features into existing
products. You're a furniture company that wants a desk with adjustable height
controlled by an app? A lighting manufacturer that wants Matter support? A lock
company that wants biometric access without building a whole software team? You
come to us.

The value: you get the domain expertise of the existing manufacturer (they know
how to make a good lock, a good chair) combined with real electronics and
software competence. The product ships under their brand, at a lower price point
than if a startup had to build everything from zero. And because we work with
multiple manufacturers across categories, we can push for interoperability from
the inside.

This is how you actually speed up the smart home transition. Not by building one
more product line, but by making the thousands of product lines that already
exist a little bit smarter.

---

_Further reading:_

- [67 open source tools for IoT](https://techbeacon.com/app-dev-testing/67-open-source-tools-resources-iot)
- [SmartThings Community on GitHub](https://github.com/SmartThingsCommunity)
