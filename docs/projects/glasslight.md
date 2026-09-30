---
title: GlassLight
description: A generative art studio that shapes light through invisible procedural glass.
hide:
  - toc
---

# GlassLight

A generative art studio that traces light through procedural glass and renders only the coloured caustics that reach the wall. The glass itself stays invisible; you only see what it does to the light.

<dl class="mp-facts">
  <dt>What</dt><dd>Native desktop app for Windows and Linux</dd>
  <dt>Built with</dt><dd>C++20, Vulkan 1.2, SDL 3, Dear ImGui</dd>
  <dt>Licence</dt><dd>MIT, open source</dd>
  <dt>Get it</dt><dd><a href="https://github.com/MagnusPetursson/GlassLight/releases/latest">Latest release</a>, <a href="https://github.com/MagnusPetursson/GlassLight">source on GitHub</a></dd>
</dl>

<figure>
  <img src="../../images/glasslight/studio.webp" alt="The GlassLight studio: a caustic artwork on the canvas with art controls beside it" width="1600" height="967">
  <figcaption>The studio. Controls update the live canvas as you change them.</figcaption>
</figure>

## Why

I've always loved generative art. The idea for this one came from watching a chandelier scatter light across the ceiling from a table lamp while it swayed in a breeze. GlassLight is an attempt to make that on purpose.

## How it works

Each composition starts from a seed. Pick one of six glass families (Pebble, Lens, Ribbon, Faceted Vessel, Cut Crystal or Fracture), then shape the form, palette, material, light source, wall and motion while the Vulkan renderer redraws the canvas.

A separate preview lets you orbit the invisible glass object itself, with optional edge overlays, so you can see what's bending the light.

<figure>
  <img src="../../images/glasslight/gallery.webp" alt="Three exported artworks: Cathedral Faceted, Ember Cut Crystal and Tidal Ribbon" width="1968" height="360" loading="lazy">
  <figcaption>Exported artworks: Cathedral / Faceted Vessel, Ember / Cut Crystal, Tidal / Ribbon.</figcaption>
</figure>

<figure>
  <video controls muted loop playsinline preload="none" poster="../../images/glasslight/loop-poster.webp" width="640" height="360">
    <source src="../../images/glasslight/loop.mp4" type="video/mp4">
  </video>
  <figcaption>A Cut Crystal composition turning through one seamless loop, slowed down.</figcaption>
</figure>

## Reproducible by design

Every exported PNG carries its complete composition inside the file. Open the PNG in GlassLight and the exact settings come back, so an image is also its own recipe.

Motion works the same way: a composition can be exported as a seamless MP4 loop of one full rotation, rendered deterministically so the same seed always gives the same video.
