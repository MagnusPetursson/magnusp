---
title: McCompass
description: A pocket-sized, real-life Minecraft compass that points at a saved spot or at its twin over LoRa.
hide:
  - toc
---

# McCompass

A pocket-sized, real-life Minecraft compass. Press the button to save a spot, like your hotel, and the needle points back to it. Or switch modes, and it points at its twin in a friend's pocket.

<dl class="mp-facts">
  <dt>What</dt><dd>Two identical handheld compasses, 70 × 60 × 18 mm</dd>
  <dt>With</dt><dd>Built together with <a href="https://kristofer.is">Kristofer</a></dd>
  <dt>Status</dt><dd>Version 2 boards ordered in September 2026; waiting on delivery</dd>
  <dt>Tools</dt><dd>KiCad, FreeCAD, Freerouting, PlatformIO, Bambu Studio</dd>
  <dt>Parts</dt><dd>Seeed XIAO ESP32-S3, 46 × WS2812B-2020, u-blox MAX-M10S GNSS, SX1262 LoRa, LSM303AGR</dd>
</dl>

<figure>
  <img src="../../images/mccompass/pcb_iso.webp" alt="Render of the circuit board front: 46 small LEDs in the shape of the compass sprite, and a square GNSS antenna" width="1400" height="1150">
  <figcaption>The front of the version 2 board: 46 LEDs in the compass sprite, with the GNSS antenna below.</figcaption>
</figure>

## Why

My friend Kristofer and I wanted a way to find each other, or our way back to the hotel, when travelling abroad, without depending on phones or roaming data. A Minecraft compass does exactly that in the game, so we built one.

## The idea

The compass in Minecraft is a 14 × 12 pixel sprite. McCompass makes it physical: every pixel is 5 mm, the case follows the sprite's outline exactly, and the needle is drawn with LEDs sitting under the face pixels.

It's designed around two modes, both borrowed from the game:

- **Saved spot**: a long press stores the current GPS position. The needle points back to it with the red needle and shimmer of a lodestone compass.
- **Each other**: the two units swap positions over LoRa radio, and the needle turns the cyan of the recovery compass.

With no GPS fix, or no word from the other unit, the needle spins aimlessly, just like it does in the Nether. The shimmer speeds up as you get closer.

None of it needs a phone, SIM card or Wi‑Fi. Positions travel over [MeshCore](https://meshcore.co.uk/), directly between the two units or through public repeaters.

## One grid, two outputs

A single geometry file defines the pixel pitch, the sprite outline and which pixels carry LEDs. Both the circuit board and the 3D-printed case are generated from it, so the LEDs line up with the printed pixel windows by construction instead of by careful measuring.

<figure>
  <img src="../../images/mccompass/pcb_top.webp" alt="Top-down render of the circuit board showing the stepped sprite outline and the LED grid" width="1400" height="1229" loading="lazy">
  <figcaption>The board outline is the sprite itself. The 46 LEDs sit under every pixel any in-game compass frame ever lights.</figcaption>
</figure>

The needle uses the same 32-frame steps as the game, so every frame the in-game compass can show, McCompass can show too. The frames are extracted at build time from our own copy of the game rather than stored in the repository.

## What changed from version 1

Version 1 was a single board milled on a Roland PCB mill. It proved the idea and showed what had to change:

- The LEDs were fed from the USB-only 5 V pin, so they went dark on battery. Version 2 runs them straight from the battery.
- The LED data signal was out of spec at 5 V. The new LEDs accept 3.3 V logic and draw under 1 µA when idle.
- Version 1 had no idea which way it was facing. Version 2 adds a tilt-compensated magnetometer, GNSS and a LoRa radio.

## The build

The 4-layer board is set up for machine assembly, with 117 parts placed by the factory. The microcontroller is soldered on by hand afterwards, on the back beside the LoRa module and motion sensor.

<figure>
  <img src="../../images/mccompass/pcb_iso_back.webp" alt="Render of the back of the circuit board with the XIAO microcontroller, LoRa module, GNSS receiver and button" width="1400" height="1150" loading="lazy">
  <figcaption>The back: XIAO ESP32-S3 with its USB-C port, the LoRa module, GNSS receiver and button.</figcaption>
</figure>

The case is two printed parts held by M2 screws in brass heat-set inserts, and the bezel prints in four matte greys to match the sprite. Its design is checked automatically on every rebuild: 22 checks cover interference with the populated board, LED alignment with the windows (within 0.005 mm), screw clearance, battery fit and openings. The firmware's compass maths has unit tests that run on a PC before any hardware exists.

## Next

Assemble the first units when the boards arrive, print a diffuser test piece to tune how the LED pixels glow through the face, then write the MeshCore-based firmware and walk-test range, GPS fix, heading accuracy and battery life.

The source isn't public yet.
