# manual

[English](README.md) | [Nederlands](README.nl.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Español](README.es.md) | [Русский](README.ru.md) | [简体中文](README.zh-CN.md) | **日本語**

AI コーディングエージェント向けのスキルで、コードベースの詳細で見た目も整った「フィールドマニュアル」を生成します。アーキテクチャ、状態機械、フロー図、手順、設定表、リファレンスを含みます。

## 実行のたびに生成されるもの

1. 公開された HTML の **Artifact**（テーマに追従し、mermaid 図と固定のデザインシステムを備えるため、どのプロジェクトのマニュアルも同じ系統の文書に見えます）。
2. バージョン管理された信頼できる情報源として、プロジェクトにコミットされる **Markdown ファイル**。
3. 任意：claude.ai なしで任意のブラウザで開ける **単体の HTML ファイル**（`--html`）。
4. 任意：ターミナルやブラウザの外で共有するための **PDF**（`--pdf`）。

スキルが従う全手順は [`SKILL.md`](SKILL.md) を参照してください。

## インストール

このリポジトリを Claude Code のスキルディレクトリにクローンします：

```sh
git clone https://github.com/spdotdev/skill-manual.git ~/.claude/skills/manual
```

そのあとプロジェクトで `/manual` を実行するか、Claude に詳細なプロジェクト文書を頼んでください。ほかのホスト（Web 版 Claude、Codex と ChatGPT、Gemini CLI、Grok、Hermes）のセットアップは [docs/setup.md](docs/setup.md) にあります。

## 使い方

```
/manual                          # writes MANUAL.md + publishes an Artifact
/manual docs/ARCHITECTURE.md     # custom output path
/manual --html                   # also write a standalone MANUAL.html
/manual --pdf                    # also render MANUAL.pdf
```

プロジェクトの `CLAUDE.md` で、そのプロジェクトの既定値を恒久的に設定できます：

```
manual output: docs/ARCHITECTURE.md
manual html: true
manual pdf: true
```

## ライセンス

MIT、[LICENSE](LICENSE) を参照。セキュリティの報告：[SECURITY.md](SECURITY.md)。変更履歴：[CHANGELOG.md](CHANGELOG.md)。

_この翻訳は AI の支援で作成しました。訂正を歓迎します。_
