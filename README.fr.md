# manual

[English](README.md) | [Nederlands](README.nl.md) | [Deutsch](README.de.md) | **Français** | [Español](README.es.md) | [Русский](README.ru.md) | [简体中文](README.zh-CN.md) | [日本語](README.ja.md)

Une skill pour agents de code IA qui génère un « manuel de terrain » détaillé et soigné visuellement pour une base de code : architecture, machines à états, diagrammes de flux, procédures, tableaux de configuration et surface de référence.

## Chaque exécution produit

1. Un **Artifact** HTML publié (qui s'adapte au thème, avec des diagrammes mermaid et un système de design fixe, pour que le manuel de chaque projet appartienne à la même famille de documents).
2. Un **fichier Markdown** versionné dans le projet comme source de vérité.
3. En option, un **fichier HTML autonome** (`--html`) pour ouvrir le manuel dans n'importe quel navigateur sans claude.ai.
4. En option, un **PDF** (`--pdf`) à partager en dehors d'un terminal ou d'un navigateur.

Voir [`SKILL.md`](SKILL.md) pour le processus complet suivi par la skill.

## Installation

Clonez ce dépôt dans votre dossier de skills Claude Code :

```sh
git clone https://github.com/spdotdev/skill-manual.git ~/.claude/skills/manual
```

Appelez-la ensuite avec `/manual` dans un projet, ou demandez à Claude une documentation détaillée du projet. L'installation pour les autres hôtes (Claude sur le web, Codex et ChatGPT, Gemini CLI, Grok, Hermes) est dans [docs/setup.md](docs/setup.md).

## Utilisation

```
/manual                          # writes MANUAL.md + publishes an Artifact
/manual docs/ARCHITECTURE.md     # custom output path
/manual --html                   # also write a standalone MANUAL.html
/manual --pdf                    # also render MANUAL.pdf
```

Des valeurs par défaut permanentes peuvent être définies par projet dans le `CLAUDE.md` de ce projet :

```
manual output: docs/ARCHITECTURE.md
manual html: true
manual pdf: true
```

## Licence

MIT, voir [LICENSE](LICENSE). Signalements de sécurité : [SECURITY.md](SECURITY.md). Modifications : [CHANGELOG.md](CHANGELOG.md).

_Traduction réalisée avec l'aide d'une IA. Les corrections sont les bienvenues._
