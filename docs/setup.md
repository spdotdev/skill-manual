# Setup

manual follows the open Agent Skills layout: a folder with a `SKILL.md`. The skill folder in this repo is `.`.
Commands below come from each host's official documentation.

## Claude Code

Personal (all your projects): `~/.claude/skills/manual/`. Project only: `.claude/skills/manual/`.

```
git clone https://github.com/spdotdev/manual
ln -s "$PWD/manual" ~/.claude/skills/manual
```

Check with `/skills`. Docs: https://code.claude.com/docs/en/skills

## Claude on the web (claude.ai)

Zip the skill folder, then Customize > Skills > "+" > Create skill > Upload a skill. Needs code execution enabled.
Docs: https://support.claude.com/en/articles/12512180-use-skills-in-claude

## Codex and ChatGPT

Codex loads skills from `$HOME/.agents/skills` (all projects) or `.agents/skills` in a repo.

```
mkdir -p ~/.agents/skills && cp -r manual ~/.agents/skills/manual
```

Docs: https://developers.openai.com/codex/build-skills

## Gemini CLI

Gemini CLI loads skills through extensions. When this repo has a `gemini-extension.json`:

```
gemini extensions install https://github.com/spdotdev/manual
```

Docs: https://geminicli.com/docs/extensions/reference/

## Grok

Grok loads skills from `~/.grok/skills/` (all projects) or `./.grok/skills/` (this repo).

```
mkdir -p ~/.grok/skills && cp -r manual ~/.grok/skills/manual
```

Docs: https://docs.x.ai/build/features/skills-plugins-marketplaces

## Hermes

```
hermes skills install spdotdev/manual
hermes skills list
```

Hermes scans a skill before it installs it. Docs: https://hermes-agent.nousresearch.com/docs/user-guide/features/skills
