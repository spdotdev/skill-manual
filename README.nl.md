# manual

[English](README.md) | **Nederlands** | [Deutsch](README.de.md) | [Français](README.fr.md) | [Español](README.es.md) | [Русский](README.ru.md) | [简体中文](README.zh-CN.md) | [日本語](README.ja.md)

Een skill voor AI-codeeragents die een uitgebreide, visueel verzorgde "veldhandleiding" voor een codebase maakt: architectuur, toestandsmachines, stroomdiagrammen, procedures, configuratietabellen en het referentieoppervlak.

## Elke run levert op

1. Een gepubliceerd HTML-**Artifact** (past zich aan het thema aan, met mermaid-diagrammen en een vast ontwerpsysteem, zodat de handleiding van elk project bij dezelfde familie documenten hoort).
2. Een **Markdown-bestand** dat in het project wordt vastgelegd als de bron van waarheid onder versiebeheer.
3. Optioneel een **losstaand HTML-bestand** (`--html`) om de handleiding in elke browser te openen zonder claude.ai.
4. Optioneel een **PDF** (`--pdf`) om te delen buiten een terminal of browser.

Zie [`SKILL.md`](SKILL.md) voor het volledige proces dat de skill volgt.

## Installeren

Clone deze repository in je Claude Code skills-map:

```sh
git clone https://github.com/spdotdev/skill-manual.git ~/.claude/skills/manual
```

Roep hem daarna aan met `/manual` in een project, of vraag Claude om uitgebreide projectdocumentatie. De installatie voor andere hosts (Claude op het web, Codex en ChatGPT, Gemini CLI, Grok, Hermes) staat in [docs/setup.md](docs/setup.md).

## Gebruik

```
/manual                          # writes MANUAL.md + publishes an Artifact
/manual docs/ARCHITECTURE.md     # custom output path
/manual --html                   # also write a standalone MANUAL.html
/manual --pdf                    # also render MANUAL.pdf
```

Vaste standaardwaarden kun je per project instellen in de `CLAUDE.md` van dat project:

```
manual output: docs/ARCHITECTURE.md
manual html: true
manual pdf: true
```

## Licentie

MIT, zie [LICENSE](LICENSE). Beveiligingsmeldingen: [SECURITY.md](SECURITY.md). Wijzigingen: [CHANGELOG.md](CHANGELOG.md).

_Vertaling met AI-hulp. Correcties zijn welkom._
