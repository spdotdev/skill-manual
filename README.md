# manual

A Claude Code skill that generates a detailed, visually-designed "field
manual" documentation artifact for a codebase: architecture, state
machines, flow diagrams, procedures, config tables, reference surface.

Every run produces:

1. A published HTML **Artifact** (theme-aware, mermaid diagrams, a fixed
   design system so every project's manual looks like part of the same
   family of documents).
2. A **Markdown file** committed to the project as the version-controlled
   source of truth.
3. Optionally, a **standalone HTML file** (`--html`) for opening the
   manual in any browser without claude.ai.
4. Optionally, a **PDF** (`--pdf`) for sharing outside a terminal/browser.

See [`SKILL.md`](SKILL.md) for the full process the skill follows.

## Install

Clone this repo into your Claude Code skills directory:

```sh
git clone https://github.com/spdotdev/skill-manual.git ~/.claude/skills/manual
```

Then invoke it with `/manual` in a project, or ask Claude for detailed
project documentation.

## Usage

```
/manual                          # writes MANUAL.md + publishes an Artifact
/manual docs/ARCHITECTURE.md     # custom output path
/manual --html                   # also write a standalone MANUAL.html
/manual --pdf                    # also render MANUAL.pdf
```

Standing defaults can be set per project in that project's `CLAUDE.md`:

```
manual output: docs/ARCHITECTURE.md
manual html: true
manual pdf: true
```

## License

MIT
