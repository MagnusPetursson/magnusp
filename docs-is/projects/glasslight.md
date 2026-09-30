---
title: GlassLight
description: Listsmiðja sem mótar ljós í gegnum ósýnilegt, reiknað gler.
hide:
  - toc
---

<!-- DRÖG: þýðing, Magnús fer yfir -->

# GlassLight

Listsmiðja sem rekur ljós í gegnum reiknað gler og sýnir aðeins litríku ljósbrotin sem lenda á veggnum. Glerið sjálft er ósýnilegt; þú sérð bara hvað það gerir við ljósið.

<dl class="mp-facts">
  <dt>Hvað</dt><dd>Forrit fyrir Windows og Linux</dd>
  <dt>Smíðað með</dt><dd>C++20, Vulkan 1.2, SDL 3, Dear ImGui</dd>
  <dt>Leyfi</dt><dd>MIT, opinn hugbúnaður</dd>
  <dt>Sækja</dt><dd><a href="https://github.com/MagnusPetursson/GlassLight/releases/latest">Nýjasta útgáfa</a>, <a href="https://github.com/MagnusPetursson/GlassLight">kóðinn á GitHub</a></dd>
</dl>

<figure>
  <img src="/images/glasslight/studio.webp" alt="GlassLight: ljósbrotsverk á striganum með stillingum við hliðina" width="1600" height="967">
  <figcaption>Smiðjan. Stillingarnar uppfæra strigann um leið og þú breytir þeim.</figcaption>
</figure>

## Af hverju

Ég hef alltaf heillast af reikniritalist. Hugmyndin að þessu verki kviknaði þegar ég horfði á ljósakrónu dreifa ljósi frá borðlampa um loftið á meðan hún sveiflaðist í golunni. GlassLight er tilraun til að gera það viljandi.

## Hvernig það virkar

Hvert verk byrjar á fræi. Veldu eina af sex glerfjölskyldum (Pebble, Lens, Ribbon, Faceted Vessel, Cut Crystal eða Fracture) og mótaðu svo form, litaspjald, efni, ljósgjafa, vegg og hreyfingu á meðan Vulkan-teiknarinn endurteiknar strigann.

Sérstök forskoðun leyfir þér að snúa ósýnilega glerhlutnum sjálfum, með útlínum ef þú vilt, svo þú sjáir hvað beygir ljósið.

<figure>
  <img src="/images/glasslight/gallery.webp" alt="Þrjú útflutt verk: Cathedral Faceted, Ember Cut Crystal og Tidal Ribbon" width="1968" height="360" loading="lazy">
  <figcaption>Útflutt verk: Cathedral / Faceted Vessel, Ember / Cut Crystal, Tidal / Ribbon.</figcaption>
</figure>

<figure>
  <video controls muted loop playsinline preload="none" poster="/images/glasslight/loop-poster.webp" width="640" height="360">
    <source src="/images/glasslight/loop.mp4" type="video/mp4">
  </video>
  <figcaption>Cut Crystal-verk sem snýst í einni samfelldri lykkju, hægt á.</figcaption>
</figure>

## Endurskapanlegt frá grunni

Hver útflutt PNG-mynd geymir alla samsetningu verksins inni í skránni. Opnaðu myndina í GlassLight og nákvæmlega sömu stillingar koma aftur, svo myndin er líka sín eigin uppskrift.

Hreyfing virkar eins: verk má flytja út sem samfellda MP4-lykkju af einum heilum hring, og hún er teiknuð á ákvarðanlegan hátt svo sama fræ gefur alltaf sama myndband.
