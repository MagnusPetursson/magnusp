---
title: PFB Studio
description: Forrit fyrir Windows og Linux sem notar PerlinFieldBot til að búa til generative art á tölvunni þinni og sýnir verkin verða til í rauntíma.
hide:
  - toc
---

# PFB Studio

Forrit fyrir Windows og Linux sem notar PerlinFieldBot til að búa til generative art á tölvunni þinni. Þú getur fylgst með því hvernig hvert verk verður til í rauntíma.

<dl class="mp-facts">
  <dt>Forritið</dt><dd>Forrit fyrir Windows og Linux</dd>
  <dt>Uppruni</dt><dd>Fork af <a href="https://github.com/dvalim/perlinfieldbot">perlinfieldbot</a> eftir dvalim</dd>
  <dt>Þróað með</dt><dd>C++17, SFML, Dear ImGui, CMake</dd>
  <dt>Sækja</dt><dd><a href="https://github.com/MagnusPetursson/pfb-studio/releases/latest">Nýjasta útgáfa</a>, <a href="https://github.com/MagnusPetursson/pfb-studio">frumkóði á GitHub</a></dd>
</dl>

## Það sem forritið býður upp á

- Veldu generator, breyttu færibreytunum og fylgstu með því hvernig myndin verður til í rauntíma.
- Láttu forritið velja seed-gildi sjálfkrafa eða sláðu inn tiltekið gildi til að endurskapa fyrri niðurstöðu.
- Vistaðu myndina í fullri upplausn sem PNG eða JPEG með vistunarglugga stýrikerfisins.
- Notaðu portable-útgáfuna fyrir Windows, Debian-pakka eða AppImage. Hægt er að endurtaka build-ferlið með CMake. Sérstakur headless-prófunarhamur býr til myndir með öllum generators fyrir sjálfvirkar prófanir.

## Fimm leiðir til að búa til myndir

Hver þessara fimm generators hefur sínar færibreytur. Myndirnar hér að neðan voru búnar til í PFB Studio.

<div class="mp-figures" markdown>
<figure>
  <img src="/images/pfb-studio/flowfield.webp" alt="Þéttar, flæðandi línur í magenta, fjólubláu og ólífugrænu á dökkum grunni" width="1000" height="1000" loading="lazy">
  <figcaption><strong>Noise flowfield.</strong> Lífræn hreyfing sem er stýrt af Perlin noise.</figcaption>
</figure>
<figure>
  <img src="/images/pfb-studio/flame.webp" alt="Glóandi grænir þræðir og bleikir bogar á dökkplómulituðum grunni" width="1000" height="1000" loading="lazy">
  <figcaption><strong>Fractal flame.</strong> Iterated function systems sem mynda flókin fractal-mynstur.</figcaption>
</figure>
<figure>
  <img src="/images/pfb-studio/growth.webp" alt="Ljósar agnaþyrpingar og blúndulíkir, blágrænir hringir á nær svörtum grunni" width="1000" height="1000" loading="lazy">
  <figcaption><strong>Organic growth.</strong> Hermun á vaxtarmynstrum úr náttúrunni.</figcaption>
</figure>
<figure>
  <img src="/images/pfb-studio/fujii.webp" alt="Hálfgagnsæjar, regnbogalitaðar slæður sem mynda háar fellingar á svörtum grunni" width="1000" height="1000" loading="lazy">
  <figcaption><strong>Fujii attractor.</strong> Sjónræn framsetning á strange attractor.</figcaption>
</figure>
<figure>
  <img src="/images/pfb-studio/fujii-2.webp" alt="Fíngert, dökkgrænt línunet sem myndar fellingar á ljósgráum grunni" width="1000" height="1000" loading="lazy">
  <figcaption><strong>Fujii attractor</strong> með ljósari litum.</figcaption>
</figure>
<figure>
  <img src="/images/pfb-studio/galaxy.webp" alt="Reykkenndir sveipir í ljósfjólubláu, límónugrænu og rósbleiku innan í daufum kúlum úr punktum" width="1000" height="1000" loading="lazy">
  <figcaption><strong>Galaxies.</strong> Agnakerfi sem mynda form stjörnukerfa.</figcaption>
</figure>
</div>
