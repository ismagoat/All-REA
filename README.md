# All-REA

### Discover the tools worth trying from the AI reverse-engineering wave.

**A utility-first directory of open-source apps, developer tools, and software reconstructions.** Find something useful, jump to its repository, and see whether it actually uses [Reverse Engineer Anything (REA)](https://github.com/morluto/rea).

[![GitHub stars](https://img.shields.io/github/stars/ismagoat/All-REA?style=flat-square)](https://github.com/ismagoat/All-REA/stargazers)
[![Last commit](https://img.shields.io/github/last-commit/ismagoat/All-REA?style=flat-square)](https://github.com/ismagoat/All-REA/commits/main)
![Directory](https://img.shields.io/badge/directory-utility--first-blue?style=flat-square)

> [!IMPORTANT]
> **Not everything in this list was built with REA.** We also track the wider wave of AI-assisted, clean-room alternatives. Every entry is labeled. **Experimental software is not necessarily a practical replacement** for its commercial inspiration.

**Updated:** October 15, 2026 · **Language:** English · **Independent community project**

## 🔥 Featured: tools to check out first

**Picked for practical use, public interest, or their importance to the ecosystem.** This is an editorial selection, **not a live popularity or quality ranking**. Star badges update automatically.

| Project | Why you might want it | Category | REA connection | Popularity |
| --- | --- | --- | --- | --- |
| **[Reverse Engineer Anything](https://github.com/morluto/rea)** | Inspect binaries and application behavior with an AI coding agent | Developer tool | **Original REA** | ![Stars](https://img.shields.io/github/stars/morluto/rea?style=flat-square) |
| **[PhotoCraft](https://github.com/storytold/photocraft)** | Edit images with a Rust-based, Photoshop-inspired app | Image editing · early-stage | **Other AI project** | ![Stars](https://img.shields.io/github/stars/storytold/photocraft?style=flat-square) |
| **[ArtCraft](https://github.com/storytold/artcraft)** | Explore a creative environment for images, video, and visual workflows | Creative studio | **Other AI project** | ![Stars](https://img.shields.io/github/stars/storytold/artcraft?style=flat-square) |
| **[ReaCut](https://github.com/Xiangyu-CAS/rea-capcut)** | Try an independent video editor inspired by CapCut / Jianying | Video editing · early-stage | **Uses REA** | ![Stars](https://img.shields.io/github/stars/Xiangyu-CAS/rea-capcut?style=flat-square) |
| **[SoundConnect Desktop](https://github.com/B-Howell/soundconnect-desktop)** | Control supported Sony headphones from Windows | Device utility | **REA tested** | ![Stars](https://img.shields.io/github/stars/B-Howell/soundconnect-desktop?style=flat-square) |
| **[Ledger Reborn](https://github.com/lxistired/ledger-reborn)** | Experiment with local invoicing, bookkeeping, and reports | Accounting · preview | **Uses REA** | ![Stars](https://img.shields.io/github/stars/lxistired/ledger-reborn?style=flat-square) |
| **[Ananasar](https://github.com/andy778/ananasar)** | Work with Modbus/TCP using a Rust client and server | Networking / industrial protocols | **Uses REA** | ![Stars](https://img.shields.io/github/stars/andy778/ananasar?style=flat-square) |
| **[REA Reconstruction Companion](https://github.com/ShadowSwaps/REA-Reconstruction-Companion)** | Turn REA findings into implementation plans and validation workflows | Developer skill | **REA ecosystem** | ![Stars](https://img.shields.io/github/stars/ShadowSwaps/REA-Reconstruction-Companion?style=flat-square) |

### Find something useful, fast

| I want to… | Start with |
| --- | --- |
| **Analyze an existing application** | [REA](https://github.com/morluto/rea), [REA Engine](https://github.com/0xHavoc/rea-engine), [hexvero](https://github.com/maximilianfeix/hexvero) |
| **Edit photos or images** | [PhotoCraft](https://github.com/storytold/photocraft), [LightCraft](https://github.com/storytold/lightcraft) |
| **Edit videos** | [ReaCut](https://github.com/Xiangyu-CAS/rea-capcut), [FilmCraft](https://github.com/storytold/filmcraft) |
| **Create documents, sheets, slides** | [WordCraft](https://github.com/storytold/wordcraft), [GridCraft](https://github.com/storytold/gridcraft), [DeckCraft](https://github.com/storytold/deckcraft) |
| **Control hardware or test a network protocol** | [SoundConnect Desktop](https://github.com/B-Howell/soundconnect-desktop), [Ananasar](https://github.com/andy778/ananasar) |
| **Work on a reverse-engineering project with AI** | [REA Reconstruction Companion](https://github.com/ShadowSwaps/REA-Reconstruction-Companion), [rea-casebook](https://github.com/pablodiazjorge/rea-casebook) |
| **Study game reconstruction** | [DX-Ball](https://github.com/N0zoM1z0/dx-ball), [Snowball War](https://github.com/tuunanet/rea-ski-or-die-reconstruction) |

## 📦 Applications and practical software

### Actually using or testing REA

These projects **explicitly acknowledge REA**. They are independent implementations, experiments, or utilities; they are not necessarily feature-complete equivalents to their reference apps.

| Application | Use case | Original reference | Project status / notes | Code & releases |
| --- | --- | --- | --- | --- |
| **ReaCut** | Video editing | CapCut / Jianying | **Early development**; macOS Apple Silicon is the verified platform listed by its author | [Source](https://github.com/Xiangyu-CAS/rea-capcut) · [Releases](https://github.com/Xiangyu-CAS/rea-capcut/releases) |
| **SoundConnect Desktop** | Sony headphone controls: EQ, noise cancellation, battery, etc. | Sony Sound Connect | **Windows desktop app**; REA was used to test / review the project, not necessarily build every feature | [Source](https://github.com/B-Howell/soundconnect-desktop) · [Releases](https://github.com/B-Howell/soundconnect-desktop/releases) |
| **Ledger Reborn** | Accounting, invoices, payments, stock and reports | QuickBooks Desktop for Mac | **Preview**; does not reproduce all QuickBooks features | [Source](https://github.com/lxistired/ledger-reborn) · [Releases](https://github.com/lxistired/ledger-reborn/releases) |
| **Ananasar** | Modbus/TCP client and server | Ananas | Rust implementation; author credits REA in the port | [Source](https://github.com/andy778/ananasar) · [Releases](https://github.com/andy778/ananasar/releases) |

**Evidence:** The authors' READMEs document REA usage for [ReaCut](https://github.com/Xiangyu-CAS/rea-capcut), [Ledger Reborn](https://github.com/lxistired/ledger-reborn), and [Ananasar](https://github.com/andy778/ananasar). [SoundConnect Desktop](https://github.com/B-Howell/soundconnect-desktop) documents REA as a test and review tool.

### Trending AI-built apps — REA **not confirmed**

These applications belong to the **broader AI software-recreation wave**, not the confirmed REA project list. Most are **early-stage**, and familiar interfaces do not imply commercial feature parity.

**Creative tools**

| Application | What you can do | Inspired by | Source |
| --- | --- | --- | --- |
| **PhotoCraft** | Photo and image editing | Photoshop | [GitHub](https://github.com/storytold/photocraft) |
| **LightCraft** | Photo processing / library | Lightroom | [GitHub](https://github.com/storytold/lightcraft) |
| **FilmCraft** | Video editing | Premiere Pro | [GitHub](https://github.com/storytold/filmcraft) |
| **VectorCraft** | Vector graphics | Illustrator | [GitHub](https://github.com/storytold/vectorcraft) |
| **PdfCraft** | PDF editing workflows | Acrobat | [GitHub](https://github.com/storytold/pdfcraft) |
| **EffectCraft** | Motion graphics / visual effects | After Effects | [GitHub](https://github.com/storytold/effectcraft) |
| **DesignCraft** | Page layouts and publishing | InDesign | [GitHub](https://github.com/storytold/designcraft) |
| **FigCraft** | Interface and layout design | Figma | [GitHub](https://github.com/storytold/figcraft) |
| **CADCraft** | Computer-aided design | AutoCAD-style CAD | [GitHub](https://github.com/storytold/cadcraft) |
| **SoundCraft** | Audio production | Pro Tools-style DAW | [GitHub](https://github.com/storytold/soundcraft) |

**Office and productivity tools**

| Application | What you can do | Inspired by | Source |
| --- | --- | --- | --- |
| **WordCraft** | Write and format documents | Microsoft Word | [GitHub](https://github.com/storytold/wordcraft) |
| **GridCraft** | Work with spreadsheets | Microsoft Excel | [GitHub](https://github.com/storytold/gridcraft) |
| **DeckCraft** | Make presentations | Microsoft PowerPoint | [GitHub](https://github.com/storytold/deckcraft) |

**Also trending:** [ArtCraft](https://github.com/storytold/artcraft) — a related creative studio/engine. **These projects have their own development status and limitations; check the README, issues, and releases before relying on them.**

## 🧰 Developer tools — build, inspect, integrate

For users who want **tools they can use in their own reverse-engineering workflows**, rather than just finished application clones.

| Tool | Why use it? | Connection to REA |
| --- | --- | --- |
| **[REA](https://github.com/morluto/rea)** | Original CLI / MCP access to reverse-engineering capabilities for coding agents | **Original project** |
| **[REA Engine](https://github.com/0xHavoc/rea-engine)** | Additional investigation and reconstruction orchestration | **Built on REA** |
| **[REA Reconstruction Companion](https://github.com/ShadowSwaps/REA-Reconstruction-Companion)** | Transform binary-analysis findings into specs, architecture, and validation checklists | **Companion tool** |
| **[ReversePort](https://github.com/laaielichter/reverseport)** | Analyze and port software across applications, games, and engines | **Related independent tool** |
| **[hexvero](https://github.com/maximilianfeix/hexvero)** | Get initial static facts about binaries and app bundles | **Related independent tool** |
| **[dsh-plugin-rea](https://github.com/czcdr/dsh-plugin-rea)** | Provision and connect REA to DeepSeek Harness | **Integration** |
| **[dsh-rea-mcp](https://github.com/sheilacraig/dsh-rea-mcp)** | Wire DeepSeek Harness to REA's MCP server with a small config bridge | **Integration** |
| **[rea-casebook](https://github.com/pablodiazjorge/rea-casebook)** | Keep a structured record of evidence during a Claude Code REA investigation | **Companion tool** |

> **Different project, same acronym:** [mytechnotalent/rea](https://github.com/mytechnotalent/rea) is **Reverse Engineering Assistant**, *not* the original Reverse Engineer Anything.

## 🎮 Games and reconstruction showcases

These projects are especially useful for learning how reverse-engineering evidence becomes maintainable source code.

| Project | Target | What makes it interesting | REA status |
| --- | --- | --- | --- |
| [DX-Ball reconstruction](https://github.com/N0zoM1z0/dx-ball) | DX-Ball 1.07 (Windows) | Recovers C/C++ functions and compares compiled behavior with the original | **Uses REA** |
| [Snowball War reconstruction](https://github.com/tuunanet/rea-ski-or-die-reconstruction) | *Ski or Die* (DOS minigame) | Recreates Snowball War in Rust / SDL2 | **Uses REA** |
| [Touhou 4 reconstruction](https://github.com/N0zoM1z0/th04) | *Lotus Land Story* (PC-98) | Rebuilds the historical game components | **REA usage not confirmed** |

## 🔬 Research, demos and technical reports

| Repository | What you will find |
| --- | --- |
| [OpenBSD netcat REA](https://github.com/NullLabTests/OpenBSD_netcat_REA) | Static analysis of netcat-openbsd with REA and Ghidra, supported by artifacts |
| [rea-lab](https://github.com/pablodiazjorge/rea-lab) | Windows REA/Ghidra experiments, measurements, and visualizations |
| [rea-research](https://github.com/ringozzt/rea-research) | Detailed technical study of REA, mainly in Chinese |
| [Reverse Engineer Anything — French guide](https://github.com/valorisa/Reverse-Engineer-Anything) | Unofficial French-language documentation |

## 📚 More places to discover projects

| Collection | Best for |
| --- | --- |
| **[Awesome REA Cases](https://github.com/songshikang0111/awesome-REA-cases)** · [English index](https://github.com/songshikang0111/awesome-REA-cases/blob/main/INDEX.en.md) | A broad, frequently refreshed collection of REA and **non-REA** AI reverse-engineering cases |
| [rea-gems](https://github.com/sqwu/rea-gems) | Community discovery of related projects and case studies |
| [awesome-rea](https://github.com/yibie/awesome-rea) | Additional resources around REA |
| [REA Casebook](https://github.com/aliaihub/rea-casebook) | Applied case studies with links and evidence |
| [awesome-REA-cases](https://github.com/beyondchenlin/awesome-REA-cases) | Another community collection |

## 🤝 Contribute a useful tool

**Priority: public, usable source code.** A practical application, library, or developer utility is more valuable to this directory than a viral post with no implementation.

To suggest something, open an [issue](https://github.com/ismagoat/All-REA/issues) or a pull request and provide:

```text
Repository:
What can someone actually do with it?
Original app / target (if applicable):
REA connection: original / used / tested / ecosystem / unrelated AI project
Evidence for the REA connection:
Platforms:
Status: released / preview / experimental / unverified
```

**Curation rules**

- Put **useful, accessible software first**; experiments and research go in later sections.
- Be clear about **what works today**, supported platforms, and preview limitations.
- Distinguish the **original REA**, projects that **used REA**, and **unrelated AI-built software**.
- Prefer maintained code repositories with documentation and releases.
- Avoid duplicates, misleading "fully recreated" claims, and unattributed copied code.
- Do not distribute proprietary application source, assets, game files, or credentials.
- Featured picks are editorial; badge star counts are live and do not constitute a quality assessment.

---

**Disclaimer:** All-REA is an unofficial, independently curated directory. It is not affiliated with the authors of REA or the products referenced above. Names and trademarks belong to their owners. Review each repository's license, maturity, and security before use.
