---
title: GlassLight
description: Forrit fyrir generative art sem hermir ferð ljóss í gegnum ósýnileg glerform og birtir ljósmynstrin sem þau mynda (caustics).
hide:
  - toc
---

# GlassLight

Forrit fyrir generative art sem hermir ferð ljóss í gegnum glerform og birtir aðeins litríku ljósmynstrin sem lenda á veggnum, svokölluð caustics. Glerformið verður til með reikniritum og er sjálft ósýnilegt; aðeins áhrif þess á ljósið sjást.

<dl class="mp-facts">
  <dt>Forritið</dt><dd>Forrit fyrir Windows og Linux</dd>
  <dt>Þróað með</dt><dd>C++20, Vulkan 1.2, SDL 3, Dear ImGui</dd>
  <dt>Hugbúnaðarleyfi</dt><dd>MIT, opinn hugbúnaður</dd>
  <dt>Sækja</dt><dd><a href="https://github.com/MagnusPetursson/GlassLight/releases/latest">Nýjasta útgáfa</a>, <a href="https://github.com/MagnusPetursson/GlassLight">frumkóði á GitHub</a></dd>
</dl>

<figure>
  <img src="/images/glasslight/studio.webp" alt="Viðmót GlassLight: ljósmynstur á myndfletinum og stillingar til hliðar" width="1600" height="967">
  <figcaption>Viðmótið. Myndin uppfærist jafnóðum þegar stillingunum er breytt.</figcaption>
</figure>

## Hugmyndin að baki

Ég hef alltaf heillast af generative art. Hugmyndin að GlassLight kviknaði þegar ég horfði á ljósakrónu sveiflast í golunni og dreifa ljósi frá borðlampa yfir loftið. Ég vildi geta búið til slík ljósmynstur sjálfur.

## Hvernig forritið virkar

Hvert verk hefst með seed-gildi. Veldu eina af sex gerðum glerforma: Pebble, Lens, Ribbon, Faceted Vessel, Cut Crystal eða Fracture. Síðan geturðu breytt löguninni, litunum, efninu, ljósgjafanum, veggnum og hreyfingunni. Vulkan renderer uppfærir myndina jafnóðum.

Í sérstakri forskoðun geturðu skoðað sjálfan glerhlutinn frá öllum hliðum. Þar er líka hægt að birta útlínur hans til að sjá betur hvernig hann beygir ljósið.

<figure>
  <img src="/images/glasslight/gallery.webp" alt="Þrjú verk flutt út úr GlassLight: Cathedral Faceted, Ember Cut Crystal og Tidal Ribbon" width="1968" height="360" loading="lazy">
  <figcaption>Verk flutt út úr GlassLight: Cathedral / Faceted Vessel, Ember / Cut Crystal, Tidal / Ribbon.</figcaption>
</figure>

<figure>
  <video controls muted loop playsinline preload="none" poster="/images/glasslight/loop-poster.webp" width="640" height="360">
    <source src="/images/glasslight/loop.mp4" type="video/mp4">
  </video>
  <figcaption>Cut Crystal-verk í samfelldri endurtekningu, sýnt á minni hraða.</figcaption>
</figure>

## Verkið geymir sína eigin uppskrift

Hver PNG-mynd sem er flutt út geymir allar stillingar verksins í skránni. Þegar myndin er opnuð aftur í GlassLight hleður forritið nákvæmlega sömu stillingum. Myndin er því líka uppskrift að sjálfri sér.

Verk í hreyfingu má flytja út sem MP4-myndband af heilum snúningi, þar sem endir og upphaf falla saman. Myndbandið er búið til með deterministic rendering, svo sama seed-gildi og sömu stillingar gefa alltaf sömu niðurstöðu.
