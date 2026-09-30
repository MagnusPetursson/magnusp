---
title: McCompass
description: Vasastór Minecraft-áttaviti í raunheimum sem bendir á vistaðan stað eða á tvíburann sinn yfir LoRa.
hide:
  - toc
---

<!-- DRÖG: þýðing, Magnús fer yfir -->

# McCompass

Vasastór Minecraft-áttaviti í raunheimum. Ýttu á takkann til að vista stað, til dæmis hótelið, og nálin bendir aftur þangað. Eða skiptu um ham og hún bendir á tvíburann í vasa vinar þíns.

<dl class="mp-facts">
  <dt>Hvað</dt><dd>Tveir eins handáttavitar, 70 × 60 × 18 mm</dd>
  <dt>Með</dt><dd>Smíðað með <a href="https://kristofer.is">Kristófer</a></dd>
  <dt>Staða</dt><dd>Borð fyrir útgáfu 2 pöntuð í september 2026; beðið eftir sendingu</dd>
  <dt>Tól</dt><dd>KiCad, FreeCAD, Freerouting, PlatformIO, Bambu Studio</dd>
  <dt>Íhlutir</dt><dd>Seeed XIAO ESP32-S3, 46 × WS2812B-2020, u-blox MAX-M10S GNSS, SX1262 LoRa, LSM303AGR</dd>
</dl>

<figure>
  <img src="/images/mccompass/pcb_iso.webp" alt="Framhlið rafrásaborðsins: 46 litlar ljósdíóður í laginu eins og áttavitinn og ferkantað GNSS-loftnet" width="1400" height="1150">
  <figcaption>Framhlið borðsins í útgáfu 2: 46 ljósdíóður í formi áttavitans, með GNSS-loftnetið fyrir neðan.</figcaption>
</figure>

## Af hverju

Kristófer vinur minn og ég vildum geta fundið hvor annan, eða leiðina aftur á hótelið, á ferðalögum erlendis, án þess að treysta á síma eða reikigögn. Áttavitinn í Minecraft gerir einmitt það í leiknum, svo við smíðuðum einn.

## Hugmyndin

Áttavitinn í Minecraft er 14 × 12 pixla mynd. McCompass gerir hann áþreifanlegan: hver pixill er 5 mm, kassinn fylgir útlínum myndarinnar nákvæmlega og nálin er teiknuð með ljósdíóðum undir pixlum skífunnar.

Hann er hannaður í kringum tvo hami, báða úr leiknum:

- **Vistaður staður**: langt ýtt vistar núverandi GPS-staðsetningu. Nálin bendir aftur þangað, rauð og glitrandi eins og á segulsteinsáttavita.
- **Hvor á annan**: tækin tvö skiptast á staðsetningum yfir LoRa-útvarp og nálin verður blágræn eins og á endurheimtaráttavitanum.

Ef ekkert GPS-merki næst, eða ekkert heyrist frá hinu tækinu, snýst nálin stefnulaust, alveg eins og í Nether. Glitrið hraðar á sér eftir því sem styttist á milli.

Ekkert af þessu þarf síma, SIM-kort eða Wi‑Fi. Staðsetningar fara yfir [MeshCore](https://meshcore.co.uk/), beint á milli tækjanna eða í gegnum opnar endurvarpsstöðvar.

## Eitt net, tvær afurðir

Ein rúmfræðiskrá skilgreinir pixlabilið, útlínur myndarinnar og hvaða pixlar bera ljósdíóður. Bæði rafrásaborðið og þrívíddarprentaði kassinn eru búin til úr henni, svo ljósdíóðurnar raðast upp við pixlagluggana í prentinu af sjálfu sér, án nákvæmra mælinga.

<figure>
  <img src="/images/mccompass/pcb_top.webp" alt="Rafrásaborðið ofan frá með tröppóttum útlínum myndarinnar og ljósdíóðunetinu" width="1400" height="1229" loading="lazy">
  <figcaption>Útlínur borðsins eru myndin sjálf. Ljósdíóðurnar 46 sitja undir hverjum pixli sem nokkur rammi áttavitans í leiknum lýsir.</figcaption>
</figure>

Nálin notar sömu 32 skref og leikurinn, svo allt sem áttavitinn í leiknum getur sýnt getur McCompass sýnt líka. Rammarnir eru sóttir úr okkar eigin eintaki af leiknum þegar kóðinn er þýddur, en eru ekki geymdir í kóðasafninu.

## Breytingar frá útgáfu 1

Útgáfa 1 var eitt borð fræst í Roland-rafrásafræsara. Hún sannaði hugmyndina og sýndi hvað þurfti að breytast:

- Ljósdíóðurnar fengu straum frá 5 V pinna sem virkar aðeins með USB, svo þær slokknuðu á rafhlöðu. Í útgáfu 2 fá þær straum beint frá rafhlöðunni.
- Gagnamerki ljósdíóðanna var utan forskriftar við 5 V. Nýju ljósdíóðurnar taka við 3,3 V merki og draga undir 1 µA í hvíld.
- Útgáfa 1 vissi ekkert í hvaða átt hún sneri. Útgáfa 2 bætir við hallaleiðréttum segulmæli, GNSS og LoRa-útvarpi.

## Smíðin

Fjögurra laga borðið er sett upp fyrir vélræna samsetningu, þar sem verksmiðjan raðar 117 íhlutum. Örtölvan er svo lóðuð á í höndunum, á bakhliðina við hlið LoRa-einingarinnar og hreyfiskynjarans.

<figure>
  <img src="/images/mccompass/pcb_iso_back.webp" alt="Bakhlið rafrásaborðsins með XIAO-örtölvunni, LoRa-einingu, GNSS-móttakara og takka" width="1400" height="1150" loading="lazy">
  <figcaption>Bakhliðin: XIAO ESP32-S3 með USB-C tenginu, LoRa-einingin, GNSS-móttakarinn og takkinn.</figcaption>
</figure>

Kassinn er tveir prentaðir hlutar, festir með M2-skrúfum í hitaþrýstar messingmúffur, og ramminn er prentaður í fjórum möttum gráum litum í stíl við myndina. Hönnunin er prófuð sjálfvirkt í hverri endurbyggingu: 22 prófanir ná yfir árekstra við samsett borðið, stöðu ljósdíóða miðað við glugga (innan 0,005 mm), pláss fyrir skrúfur, rafhlöðu og op. Áttavitareikningar fastbúnaðarins eru með einingaprófum sem keyra á tölvu áður en nokkur vélbúnaður er til.

## Næst

Setja saman fyrstu tækin þegar borðin koma, prenta prufustykki til að stilla hvernig pixlarnir lýsa í gegnum skífuna, skrifa svo fastbúnaðinn á grunni MeshCore og prófa drægni, GPS-merki, stefnunákvæmni og rafhlöðuendingu úti á göngu.

Kóðinn er ekki opinber enn.
