# manual

[English](README.md) | [Nederlands](README.nl.md) | **Deutsch** | [Français](README.fr.md) | [Español](README.es.md) | [Русский](README.ru.md) | [简体中文](README.zh-CN.md) | [日本語](README.ja.md)

Ein Skill für KI-Coding-Agenten, der ein ausführliches, optisch gestaltetes "Feldhandbuch" für eine Codebasis erzeugt: Architektur, Zustandsautomaten, Ablaufdiagramme, Verfahren, Konfigurationstabellen und die Referenzoberfläche.

## Jeder Lauf erzeugt

1. Ein veröffentlichtes HTML-**Artifact** (passt sich dem Theme an, mit Mermaid-Diagrammen und einem festen Designsystem, sodass das Handbuch jedes Projekts zur selben Dokumentenfamilie gehört).
2. Eine **Markdown-Datei**, die im Projekt als versionierte Quelle der Wahrheit eingecheckt wird.
3. Optional eine **eigenständige HTML-Datei** (`--html`), um das Handbuch in jedem Browser ohne claude.ai zu öffnen.
4. Optional ein **PDF** (`--pdf`) zum Teilen außerhalb eines Terminals oder Browsers.

Den vollständigen Ablauf des Skills findest du in [`SKILL.md`](SKILL.md).

## Installation

Klone dieses Repository in dein Claude-Code-Skills-Verzeichnis:

```sh
git clone https://github.com/spdotdev/skill-manual.git ~/.claude/skills/manual
```

Rufe ihn dann mit `/manual` in einem Projekt auf, oder bitte Claude um ausführliche Projektdokumentation. Die Einrichtung für andere Hosts (Claude im Web, Codex und ChatGPT, Gemini CLI, Grok, Hermes) steht in [docs/setup.md](docs/setup.md).

## Verwendung

```
/manual                          # writes MANUAL.md + publishes an Artifact
/manual docs/ARCHITECTURE.md     # custom output path
/manual --html                   # also write a standalone MANUAL.html
/manual --pdf                    # also render MANUAL.pdf
```

Dauerhafte Standardwerte lassen sich pro Projekt in der `CLAUDE.md` dieses Projekts festlegen:

```
manual output: docs/ARCHITECTURE.md
manual html: true
manual pdf: true
```

## Lizenz

MIT, siehe [LICENSE](LICENSE). Sicherheitsmeldungen: [SECURITY.md](SECURITY.md). Änderungen: [CHANGELOG.md](CHANGELOG.md).

_Übersetzung mit KI-Hilfe. Korrekturen sind willkommen._
