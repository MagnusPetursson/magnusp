---
title: Hvað er agent?
template: faq.html
lang: is
single_language: true
noindex: true
search:
  exclude: true
hide:
  - navigation
  - toc
---

# Hvað er agent?

- Gervigreind sem getur framkvæmt, ekki bara svarað. Hún fær tól (skrár, skipanir, vafra), tekur skref, skoðar útkomuna og ákveður næsta skref.
- Chat: Spurningar, hugmyndir, lítil uppköst.
- Agent: Vinnur verkefni til enda með skrám, tólum og prófunum.

## Hvað getur agent gert?

- Lesið og breytt skrám, keyrt skipanir, byggt og prófað hluti.
- Unnið sjálfstætt að markmiði í mörgum skrefum.
- Hann vinnur með þeim aðgangi sem þið gefið honum.
- Ef hann skýtur upp á bak getur það verið fjörugt.
- Passið að takmarka aðgengi.

## Tengingar (MCP)

- MCP er staðall sem leyfir agent-um að tala við annan hugbúnað. Til dæmis Google Workspace (póstur, Drive, dagatal), Notion eða gagnagrunna. Svipað og USB fyrir gervigreind.
- Tengið bara það sem verkefnið þarf. Alltaf best að byrja read-only.

<small>(Ég hef aldrei treyst gervigreind fyrir samskiptum)</small>


## Öryggi og gögn

- Byrjið í afmörkuðu umhverfi: ein mappa, engar persónuupplýsingar, engin admin réttindi.
- Permission modes: Agentinn spyr áður en hann framkvæmir (Claude Code: Manual eða Plan. Codex: Approval). Aldrei byrja í "skip permissions".
- Prompt injection: Tölvupóstur eða vefsíða getur haft faldar skipanir sem agentinn hlýðir. Þess vegna skiptir máli hvað þið tengið hann við.
- Þjálfun: ChatGPT og Gemini á persónulegum áskriftum þjálfa á gögnunum ykkar nema þið slökkvið á því. Claude spyr. Vinnu- og skólaáskriftir þjálfa ekki.

## Hvernig vinnur maður með agent?

- Forrit: Claude Desktop (með Claude Code) eða Codex appið. Auðveldasta byrjunin.
- Í IDE: VS Code með Claude Code eða Codex viðbót, Cursor, Google Antigravity.
- Í terminal (CLI): Claude Code, Codex CLI. Öflugast en tæknilegast.
- Í skýinu: Codex cloud, Claude Code á vefnum. Vinnur á afriti hjá þeim, ekki á tölvunni ykkar.
- Í gegnum spjallforrit: Hermes á t.d. Discord (Ég nota þetta mikið)

## Hvað er í boði?

- Claude Code (Anthropic): Sterkt í kóða og löngum, vönduðum verkefnum. Góð stjórn á heimildum.
- Codex (OpenAI): Innifalið í ChatGPT Plus. Keyrir í sandbox sjálfgefið. Þægilegra viðmót en ekki jafn góður forritari.
- Gemini / Antigravity (Google): Stórt context og ódýr byrjun. Ekki jafn fínpússuð upplifun.
- GitHub Copilot: Fyrir forritara inni í IDE. Ekki það sama og Microsoft Copilot.
- Hermes og annað open source: Full stjórn og hvaða módel sem er. Þið keyrið þetta sjálf. Bleeding edge.
- Local módel (Ollama, LM Studio): Gögnin fara aldrei af tölvunni. Ókeypis en töluvert slakari.

## Hvar byrja ég og hvað kostar það?

- Ef þið eruð með ChatGPT Plus ($20, ≈3.050 kr) er Codex innifalið. Prófið það fyrst.
- Annars Claude Pro ($20, ≈3.050 kr) með Claude Code í Desktop appinu.
- Byrjið á einu ódýru og færið ykkur upp ef þið rekist á usage limit.

## Hvernig skrifa ég gott prompt?

- Skrifið á ensku. Agentar eru því miður talsvert slakari á íslensku.
- Lýsið útkomunni eins og þið viljið hafa hana, ekki bara ferlinu.
- Gefið agentinum þær upplýsingar sem hann þarf til að klára verkið.
- Segið hvenær verkið telst klárt og hvað þarf ykkar samþykki.


Dæmi:

> "Make a web page where I can draw a rectangle on a map of Iceland and download a 3D-printable STL of the terrain inside it. Use free elevation data that needs no login. Test it in a browser before you call it done, and ask me before publishing anything."

## Hvernig veit ég hvort hann sé bara að bulla?

- Látið hann prófa eigin vinnu og opnið svo útkomuna sjálf.
- Biðjið um heimildir og athugið hvort þær segi það sem hann heldur fram.
- Notið alltaf Git/version control.
- Litlar prufur fyrst. Vel heppnað export er ekki það sama og vel heppnuð prentun.
