# manual

[English](README.md) | [Nederlands](README.nl.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Español](README.es.md) | **Русский** | [简体中文](README.zh-CN.md) | [日本語](README.ja.md)

Скилл для ИИ-агентов, пишущих код, который создаёт подробное, визуально оформленное «полевое руководство» по кодовой базе: архитектура, конечные автоматы, диаграммы потоков, процедуры, таблицы конфигурации и справочная поверхность.

## Каждый запуск создаёт

1. Опубликованный HTML-**Artifact** (подстраивается под тему, с диаграммами mermaid и единой дизайн-системой, так что руководство каждого проекта выглядит частью одной семьи документов).
2. **Markdown-файл**, который коммитится в проект как источник истины под версионным контролем.
3. По желанию **отдельный HTML-файл** (`--html`), чтобы открывать руководство в любом браузере без claude.ai.
4. По желанию **PDF** (`--pdf`), чтобы делиться вне терминала или браузера.

Полный процесс, которому следует скилл, описан в [`SKILL.md`](SKILL.md).

## Установка

Склонируйте этот репозиторий в каталог скиллов Claude Code:

```sh
git clone https://github.com/spdotdev/skill-manual.git ~/.claude/skills/manual
```

Затем вызовите его командой `/manual` в проекте или попросите Claude подготовить подробную документацию проекта. Установка для других хостов (Claude в вебе, Codex и ChatGPT, Gemini CLI, Grok, Hermes) описана в [docs/setup.md](docs/setup.md).

## Использование

```
/manual                          # writes MANUAL.md + publishes an Artifact
/manual docs/ARCHITECTURE.md     # custom output path
/manual --html                   # also write a standalone MANUAL.html
/manual --pdf                    # also render MANUAL.pdf
```

Постоянные значения по умолчанию можно задать для каждого проекта в его `CLAUDE.md`:

```
manual output: docs/ARCHITECTURE.md
manual html: true
manual pdf: true
```

## Лицензия

MIT, см. [LICENSE](LICENSE). Сообщения о безопасности: [SECURITY.md](SECURITY.md). Изменения: [CHANGELOG.md](CHANGELOG.md).

_Перевод выполнен с помощью ИИ. Исправления приветствуются._
