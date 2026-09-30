---
title: PFB Studio
description: A native Windows and Linux app that runs the PerlinFieldBot generative art generators locally and draws them live.
hide:
  - toc
---

# PFB Studio

A native desktop app for Windows and Linux that runs the PerlinFieldBot generative art generators on your own machine, so you can watch each piece draw itself live.

<dl class="mp-facts">
  <dt>What</dt><dd>Native desktop app for Windows and Linux</dd>
  <dt>Origin</dt><dd>Fork of dvalim's <a href="https://github.com/dvalim/perlinfieldbot">perlinfieldbot</a></dd>
  <dt>Built with</dt><dd>C++17, SFML, Dear ImGui, CMake</dd>
  <dt>Get it</dt><dd><a href="https://github.com/MagnusPetursson/pfb-studio/releases/latest">Latest release</a>, <a href="https://github.com/MagnusPetursson/pfb-studio">source on GitHub</a></dd>
</dl>

## What it does

- Pick a generator, adjust its parameters, and watch the image build up live.
- Leave the seed on automatic, or type one in to replay a result.
- Save at full resolution as PNG or JPEG through the system's own save dialog.
- Install it as a portable Windows executable, a Debian package or an AppImage. The builds are reproducible with CMake, and a headless test mode renders every generator for automated checks.

## The generators

Five generators, each with its own parameters. These images were rendered with PFB Studio.

<div class="mp-figures" markdown>
<figure>
  <img src="../../images/pfb-studio/flowfield.webp" alt="Dense flowing lines in magenta, violet and olive swirling across a dark field" width="1000" height="1000" loading="lazy">
  <figcaption><strong>Noise flowfield.</strong> Organic motion guided by Perlin noise.</figcaption>
</figure>
<figure>
  <img src="../../images/pfb-studio/flame.webp" alt="Glowing green wisps and pink arcs on a deep plum background" width="1000" height="1000" loading="lazy">
  <figcaption><strong>Fractal flame.</strong> Iterated function systems that build up intricate fractals.</figcaption>
</figure>
<figure>
  <img src="../../images/pfb-studio/growth.webp" alt="Pale particle colonies and lace-like teal rings on near-black" width="1000" height="1000" loading="lazy">
  <figcaption><strong>Organic growth.</strong> Simulated natural growth patterns.</figcaption>
</figure>
<figure>
  <img src="../../images/pfb-studio/fujii.webp" alt="Translucent iridescent veils folding into a tall form on black" width="1000" height="1000" loading="lazy">
  <figcaption><strong>Fujii attractor.</strong> Visualisations of a strange attractor.</figcaption>
</figure>
<figure>
  <img src="../../images/pfb-studio/fujii-2.webp" alt="Fine dark-green line-mesh sheets folding over each other on pale grey" width="1000" height="1000" loading="lazy">
  <figcaption><strong>Fujii attractor</strong>, a lighter palette.</figcaption>
</figure>
<figure>
  <img src="../../images/pfb-studio/galaxy.webp" alt="Smoke-like curls in lavender, lime and rose inside faint dotted spheres" width="1000" height="1000" loading="lazy">
  <figcaption><strong>Galaxies.</strong> Particle systems that form stellar structures.</figcaption>
</figure>
</div>
