---
title: PFB Studio
description: Forrit fyrir Windows og Linux sem keyrir listvélar PerlinFieldBot á þinni eigin tölvu og teiknar þær í rauntíma.
hide:
  - toc
---

<!-- DRÖG: þýðing, Magnús fer yfir -->

# PFB Studio

Forrit fyrir Windows og Linux sem keyrir listvélar PerlinFieldBot á þinni eigin tölvu, svo þú getur fylgst með hverju verki teiknast í rauntíma.

<dl class="mp-facts">
  <dt>Hvað</dt><dd>Forrit fyrir Windows og Linux</dd>
  <dt>Uppruni</dt><dd>Kvísl af <a href="https://github.com/dvalim/perlinfieldbot">perlinfieldbot</a> eftir dvalim</dd>
  <dt>Smíðað með</dt><dd>C++17, SFML, Dear ImGui, CMake</dd>
  <dt>Sækja</dt><dd><a href="https://github.com/MagnusPetursson/pfb-studio/releases/latest">Nýjasta útgáfa</a>, <a href="https://github.com/MagnusPetursson/pfb-studio">kóðinn á GitHub</a></dd>
</dl>

## Hvað það gerir

- Veldu vél, stilltu færibreyturnar og fylgstu með myndinni byggjast upp í rauntíma.
- Láttu forritið velja fræið, eða sláðu það inn til að endurtaka niðurstöðu.
- Vistaðu í fullri upplausn sem PNG eða JPEG með vistunarglugga stýrikerfisins.
- Settu það upp sem ferðaútgáfu fyrir Windows, Debian-pakka eða AppImage. Smíðin er endurtakanleg með CMake og skjálaus prófunarhamur teiknar allar vélarnar fyrir sjálfvirkar prófanir.

## Listvélarnar

Fimm vélar, hver með sínar færibreytur. Þessar myndir voru teiknaðar með PFB Studio.

<div class="mp-figures" markdown>
<figure>
  <img src="/images/pfb-studio/flowfield.webp" alt="Þéttar flæðandi línur í magenta, fjólubláu og ólífugrænu á dökkum grunni" width="1000" height="1000" loading="lazy">
  <figcaption><strong>Suðflæði.</strong> Lífræn hreyfing sem Perlin-suð stýrir.</figcaption>
</figure>
<figure>
  <img src="/images/pfb-studio/flame.webp" alt="Glóandi grænir þræðir og bleikir bogar á dökkplómulituðum grunni" width="1000" height="1000" loading="lazy">
  <figcaption><strong>Brotamyndalogi.</strong> Ítruð fallakerfi sem byggja upp flókin brotamynstur.</figcaption>
</figure>
<figure>
  <img src="/images/pfb-studio/growth.webp" alt="Ljósar agnaþyrpingar og blágrænir blúnduhringir á næstum svörtum grunni" width="1000" height="1000" loading="lazy">
  <figcaption><strong>Lífrænn vöxtur.</strong> Hermd vaxtarmynstur úr náttúrunni.</figcaption>
</figure>
<figure>
  <img src="/images/pfb-studio/fujii.webp" alt="Gegnsæjar, regnbogalitaðar slæður sem leggjast í hátt form á svörtu" width="1000" height="1000" loading="lazy">
  <figcaption><strong>Fujii-aðdráttarafl.</strong> Myndir af undarlegum aðdráttarafli.</figcaption>
</figure>
<figure>
  <img src="/images/pfb-studio/fujii-2.webp" alt="Fínt dökkgrænt línunet sem leggst í fellingar á ljósgráum grunni" width="1000" height="1000" loading="lazy">
  <figcaption><strong>Fujii-aðdráttarafl</strong>, ljósari litir.</figcaption>
</figure>
<figure>
  <img src="/images/pfb-studio/galaxy.webp" alt="Reykkenndir sveipir í lavender, límónugrænu og rósbleiku inni í daufum punktakúlum" width="1000" height="1000" loading="lazy">
  <figcaption><strong>Vetrarbrautir.</strong> Agnakerfi sem mynda stjörnuþyrpingar.</figcaption>
</figure>
</div>
