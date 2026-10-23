# manual

[English](README.md) | [Nederlands](README.nl.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | **Español** | [Русский](README.ru.md) | [简体中文](README.zh-CN.md) | [日本語](README.ja.md)

Una skill para agentes de código con IA que genera un "manual de campo" detallado y de diseño cuidado para una base de código: arquitectura, máquinas de estados, diagramas de flujo, procedimientos, tablas de configuración y la superficie de referencia.

## Cada ejecución produce

1. Un **Artifact** HTML publicado (se adapta al tema, con diagramas mermaid y un sistema de diseño fijo, de modo que el manual de cada proyecto parece de la misma familia de documentos).
2. Un **archivo Markdown** guardado en el proyecto como fuente de verdad bajo control de versiones.
3. Opcionalmente, un **archivo HTML independiente** (`--html`) para abrir el manual en cualquier navegador sin claude.ai.
4. Opcionalmente, un **PDF** (`--pdf`) para compartir fuera de una terminal o un navegador.

Consulta [`SKILL.md`](SKILL.md) para ver el proceso completo que sigue la skill.

## Instalación

Clona este repositorio en tu carpeta de skills de Claude Code:

```sh
git clone https://github.com/spdotdev/skill-manual.git ~/.claude/skills/manual
```

Luego invócala con `/manual` en un proyecto, o pide a Claude documentación detallada del proyecto. La instalación para otros hosts (Claude en la web, Codex y ChatGPT, Gemini CLI, Grok, Hermes) está en [docs/setup.md](docs/setup.md).

## Uso

```
/manual                          # writes MANUAL.md + publishes an Artifact
/manual docs/ARCHITECTURE.md     # custom output path
/manual --html                   # also write a standalone MANUAL.html
/manual --pdf                    # also render MANUAL.pdf
```

Los valores predeterminados permanentes se pueden fijar por proyecto en el `CLAUDE.md` de ese proyecto:

```
manual output: docs/ARCHITECTURE.md
manual html: true
manual pdf: true
```

## Licencia

MIT, consulta [LICENSE](LICENSE). Avisos de seguridad: [SECURITY.md](SECURITY.md). Cambios: [CHANGELOG.md](CHANGELOG.md).

_Traducción hecha con ayuda de IA. Se agradecen las correcciones._
