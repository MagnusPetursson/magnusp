---
title: McCompass
description: Áttavitinn úr Minecraft, smíðaður í vasastærð, sem vísar á vistaðan stað eða annað tæki með LoRa-sambandi.
hide:
  - toc
---

# McCompass

Áttavitinn úr Minecraft, smíðaður í vasastærð. Ýttu á takkann til að vista staðsetningu, til dæmis hótelið sem þú gistir á, og nálin vísar þangað. Í hinum hamnum vísar hún á sams konar tæki í vasa vinar þíns.

<dl class="mp-facts">
  <dt>Verkefnið</dt><dd>Tveir eins áttavitar í vasastærð, 70 × 60 × 18 mm</dd>
  <dt>Samstarf</dt><dd>Hannað og smíðað með <a href="https://kristofer.is">Kristófer</a></dd>
  <dt>Staða</dt><dd>PCB fyrir útgáfu 2 pöntuð í september 2026; beðið eftir afhendingu</dd>
  <dt>Verkfæri</dt><dd>KiCad, FreeCAD, Freerouting, PlatformIO, Bambu Studio</dd>
  <dt>Íhlutir</dt><dd>Seeed XIAO ESP32-S3, 46 × WS2812B-2020, u-blox MAX-M10S GNSS, SX1262 LoRa, LSM303AGR</dd>
</dl>

<figure>
  <img src="/images/mccompass/pcb_iso.webp" alt="Þrívíddarmynd af framhlið PCB með 46 LED-ljósum í lögun áttavitans og ferköntuðu GNSS-loftneti" width="1400" height="1150">
  <figcaption>Framhlið PCB í útgáfu 2: 46 LED-ljós mynda áttavitann og GNSS-loftnetið situr fyrir neðan.</figcaption>
</figure>

## Hugmyndin að baki

Kristófer vinur minn og ég vildum geta fundið hvor annan, eða leiðina aftur á hótelið, á ferðalögum erlendis án þess að reiða okkur á síma eða gagnareiki. Áttavitinn úr Minecraft varð fyrirmyndin, svo við smíðuðum okkar eigin.

## Hvernig áttavitinn virkar

Áttavitinn í Minecraft er 14 × 12 pixla mynd, svokallað sprite. McCompass færir hann úr leiknum í áþreifanlegt form: hver pixill er 5 mm, hulstrið fylgir útlínum myndarinnar og LED-ljós undir skífunni birta nálina.

Tveir notkunarhamir eru í hönnuninni, báðir sóttir í leikinn:

- **Vistaður staður:** Haltu takkanum inni til að vista núverandi GPS-staðsetningu. Rauða nálin vísar síðan á staðinn og glitrar líkt og á *lodestone compass*.
- **Finna hvort annað:** Tækin skiptast á staðsetningum með LoRa-sambandi. Nálin verður þá blágræn, líkt og á *recovery compass*.

Ef tækið nær ekki að ákvarða GPS-staðsetningu eða hefur ekki samband við hitt tækið snýst nálin stefnulaust, alveg eins og í Nether. Glitrið verður hraðara eftir því sem þú nálgast áfangastaðinn eða hitt tækið.

Hvorki þarf síma, SIM-kort né Wi‑Fi. Staðsetningar eru sendar með [MeshCore](https://meshcore.co.uk/), annaðhvort beint milli tækjanna eða um opnar endurvarpsstöðvar.

## Sama rúmfræði fyrir PCB og hulstur

Ein skrá skilgreinir pixlabilið, útlínur myndarinnar og hvaða pixlar fá LED-ljós. Bæði PCB og þrívíddarprentaða hulstrið eru búin til út frá þessum gögnum. Ljósin lenda því sjálfkrafa á réttum stað undir pixlagluggunum, án þess að stilla þurfi hlutana saman með nákvæmum handmælingum.

<figure>
  <img src="/images/mccompass/pcb_top.webp" alt="Þrívíddarmynd af PCB ofan frá, með þrepóttum útlínum Minecraft-áttavitans og LED-ljósum í pixlaneti" width="1400" height="1229" loading="lazy">
  <figcaption>Útlínur PCB fylgja myndinni úr leiknum. LED-ljósin 46 sitja undir öllum pixlum sem kviknar á í einhverjum myndramma áttavitans.</figcaption>
</figure>

Nálin hefur sömu 32 stöður og í leiknum. McCompass getur því birt alla myndrammana sem áttavitinn í leiknum notar. Í build-ferlinu eru þeir sóttir úr okkar eigin eintaki af leiknum, en ekki geymdir í repository.

## Breytingar frá útgáfu 1

Útgáfa 1 var eitt PCB, fræst í Roland PCB-fræsara. Hún sýndi að hugmyndin gengi upp og leiddi í ljós hvað þyrfti að bæta:

- LED-ljósin fengu spennu frá 5 V pinna sem virkar aðeins þegar USB er tengt. Þau slokknuðu því þegar tækið gekk fyrir rafhlöðu. Í útgáfu 2 fá þau spennu beint frá rafhlöðunni.
- Spennustig LED-gagnamerkisins uppfyllti ekki kröfurnar þegar ljósin gengu á 5 V. Nýju ljósin taka við 3,3 V logic-merki og draga minna en 1 µA í hvíld.
- Útgáfa 1 gat ekki greint í hvaða átt hún sneri. Í útgáfu 2 bætast við segulmælir með hallaleiðréttingu (tilt-compensated magnetometer), GNSS og LoRa-eining.

## Smíðin

Fjögurra laga PCB er hannað fyrir sjálfvirka íhlutasetningu, þar sem verksmiðjan setur á það 117 íhluti. XIAO microcontroller er síðan lóðaður á með höndunum, á bakhliðinni við hlið LoRa-einingarinnar og hreyfiskynjarans.

<figure>
  <img src="/images/mccompass/pcb_iso_back.webp" alt="Þrívíddarmynd af bakhlið PCB með XIAO microcontroller, LoRa-einingu, GNSS-móttakara og takka" width="1400" height="1150" loading="lazy">
  <figcaption>Bakhliðin: XIAO ESP32-S3 með USB-C tengi, LoRa-eining, GNSS-móttakari og takki.</figcaption>
</figure>

Hulstrið er úr tveimur þrívíddarprentuðum hlutum sem eru festir saman með M2-skrúfum og heat-set inserts úr messing. Ramminn um skífuna er prentaður í fjórum möttum gráum tónum til að líkjast myndinni úr leiknum.

Í hvert sinn sem líkanið er búið til að nýju eru keyrðar 22 sjálfvirkar prófanir. Þær ná yfir bil við PCB með öllum íhlutum, staðsetningu LED-ljósa miðað við gluggana (innan 0,005 mm skekkjumarka) og rými fyrir skrúfur, rafhlöðu og op. Útreikningar áttavitans í firmware eru sannreyndir með unit tests sem keyra á tölvu áður en vélbúnaðurinn er til staðar.

## Næstu skref

Þegar PCB koma verða fyrstu tækin sett saman. Síðan verður prentað prufustykki til að stilla ljósdreifinguna í skífunni, firmware skrifað á grunni MeshCore og farið í göngu til að prófa drægni, GPS-staðsetningu, stefnunákvæmni og rafhlöðuendingu.

Frumkóðinn er ekki opinber enn.
