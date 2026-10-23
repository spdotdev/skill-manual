# manual

[English](README.md) | [Nederlands](README.nl.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Español](README.es.md) | [Русский](README.ru.md) | **简体中文** | [日本語](README.ja.md)

一个面向 AI 编程代理的技能，为代码库生成详细且设计精美的“现场手册”：架构、状态机、流程图、操作步骤、配置表和参考接口。

## 每次运行会生成

1. 一个已发布的 HTML **Artifact**（随主题切换，带 mermaid 图表和固定的设计系统，使每个项目的手册都属于同一类文档）。
2. 一个 **Markdown 文件**，作为受版本控制的权威来源提交到项目中。
3. 可选：**独立的 HTML 文件**（`--html`），无需 claude.ai 即可在任何浏览器中打开手册。
4. 可选：**PDF**（`--pdf`），便于在终端或浏览器之外分享。

技能遵循的完整流程见 [`SKILL.md`](SKILL.md)。

## 安装

将此仓库克隆到你的 Claude Code 技能目录：

```sh
git clone https://github.com/spdotdev/skill-manual.git ~/.claude/skills/manual
```

然后在项目中用 `/manual` 调用它，或让 Claude 生成详细的项目文档。其他平台（网页版 Claude、Codex 和 ChatGPT、Gemini CLI、Grok、Hermes）的安装方法见 [docs/setup.md](docs/setup.md)。

## 用法

```
/manual                          # writes MANUAL.md + publishes an Artifact
/manual docs/ARCHITECTURE.md     # custom output path
/manual --html                   # also write a standalone MANUAL.html
/manual --pdf                    # also render MANUAL.pdf
```

可以在项目的 `CLAUDE.md` 中为该项目设置长期默认值：

```
manual output: docs/ARCHITECTURE.md
manual html: true
manual pdf: true
```

## 许可证

MIT，见 [LICENSE](LICENSE)。安全问题报告：[SECURITY.md](SECURITY.md)。更新记录：[CHANGELOG.md](CHANGELOG.md)。

_本翻译由 AI 辅助完成，欢迎指正。_
