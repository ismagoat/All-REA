# All-REA

**A curated directory of open-source reverse-engineering projects, REA experiments, and AI-assisted software reconstructions.**

[![GitHub stars](https://img.shields.io/github/stars/ismagoat/All-REA?style=flat-square)](https://github.com/ismagoat/All-REA/stargazers)
[![Last commit](https://img.shields.io/github/last-commit/ismagoat/All-REA?style=flat-square)](https://github.com/ismagoat/All-REA/commits/main)

**All-REA** helps you discover what people are building with [Reverse Engineer Anything (REA)](https://github.com/morluto/rea) and related AI reverse-engineering workflows. The focus is on **public GitHub repositories with code**, not just announcements.

> **Important:** Not every project below uses REA. To avoid confusing unrelated work with the original tool, entries are separated into REA projects, ecosystem tools, other AI-assisted reconstructions, and community indexes. Descriptions summarize the authors' public documentation; results have not been independently reproduced.

**Last manually curated:** October 15, 2026 · **Language:** English · **Status:** Growing

## Contents

- [Projects using or testing REA](#projects-using-or-testing-rea)
- [REA analysis and research](#rea-analysis-and-research)
- [REA ecosystem and developer tools](#rea-ecosystem-and-developer-tools)
- [Other AI-assisted reconstruction projects](#other-ai-assisted-reconstruction-projects)
- [Community lists and resources](#community-lists-and-resources)
- [Contributing](#contributing)

## Projects using or testing REA

These repositories **explicitly mention using or evaluating REA** in their project documentation. They may be early prototypes, partial reconstructions, or independent implementations rather than exact copies of the original software.

| Project | Original target / purpose | What it does | REA relationship |
| --- | --- | --- | --- |
| [DX-Ball reconstruction](https://github.com/N0zoM1z0/dx-ball) | DX-Ball 1.07 | Reconstructs the classic Windows game as readable C/C++ with Ghidra-assisted, function-by-function comparisons. | **Used** |
| [Snowball War](https://github.com/tuunanet/rea-ski-or-die-reconstruction) | *Ski or Die* (DOS) | Rebuilds the Snowball War minigame in Rust and SDL2. | **Used** |
| [ReaCut](https://github.com/Xiangyu-CAS/rea-capcut) | CapCut / Jianying | Independently develops a video editor after examining application behavior and project formats. | **Used** |
| [Ledger Reborn](https://github.com/lxistired/ledger-reborn) | QuickBooks Desktop for Mac | Develops an independent desktop accounting application with a SQLite-backed ledger. | **Used** |
| [Ananasar](https://github.com/andy778/ananasar) | Ananas Modbus/TCP tool | Ports the functionality of a Modbus/TCP client/server tool to Rust. | **Used** |
| [SoundConnect Desktop](https://github.com/B-Howell/soundconnect-desktop) | Sony headphones / Sound Connect | Windows desktop controls for compatible Sony headphones; documentation describes using REA to evaluate and review the project. | **Tested** |

**Key:** **Used** = author credits REA in the development/research workflow. **Tested** = author reports using REA to inspect or evaluate the project, not necessarily to recreate the target.

## REA analysis and research

Projects that demonstrate or document binary analysis rather than delivering a full replacement application.

| Project | Focus |
| --- | --- |
| [OpenBSD netcat REA](https://github.com/NullLabTests/OpenBSD_netcat_REA) | Evidence-backed static analysis of the Ubuntu netcat-openbsd binary with REA and Ghidra. |
| [rea-lab](https://github.com/pablodiazjorge/rea-lab) | Windows test environment for measuring and visualizing REA + Ghidra workflows. |
| [rea-research](https://github.com/ringozzt/rea-research) | Technical investigation of the REA architecture and workflow (primarily Chinese). |
| [Touhou 4 / TH04 reconstruction](https://github.com/N0zoM1z0/th04) | Ongoing reconstruction of *Lotus Land Story* for PC-98. **REA usage not confirmed from the README**; included as related reconstruction work. |

## REA ecosystem and developer tools

These tools help with REA workflows, documentation, integrations, or adjacent forms of reverse engineering. **Being in this section does not imply that every tool depends on REA.**

| Repository | Type | Description |
| --- | --- | --- |
| [morluto/rea](https://github.com/morluto/rea) | Original project | Reverse Engineer Anything: AI-agent access to reverse-engineering workflows through CLI/MCP interfaces. |
| [rea-engine](https://github.com/0xHavoc/rea-engine) | Extension / fork | Adds investigation and reconstruction orchestration on top of REA. |
| [REA Reconstruction Companion](https://github.com/ShadowSwaps/REA-Reconstruction-Companion) | Agent skill | Converts reverse-engineering evidence into specifications, plans, and validation steps. |
| [dsh-plugin-rea](https://github.com/czcdr/dsh-plugin-rea) | Integration | Connects REA to DeepSeek Harness. |
| [dsh-rea-mcp](https://github.com/sheilacraig/dsh-rea-mcp) | MCP bridge | A compact, configuration-based DeepSeek Harness to REA bridge. |
| [rea-casebook](https://github.com/pablodiazjorge/rea-casebook) | Claude Code tool | Maintains a structured casebook of evidence collected through REA. |
| [ReversePort](https://github.com/laaielichter/reverseport) | Related tool | Agent-oriented reverse-engineering and porting across applications, games, binaries, and websites. |
| [hexvero](https://github.com/maximilianfeix/hexvero) | Related tool | Static analysis of binaries and app bundles; positions itself alongside, not as a dependency of, REA. |
| [Guide REA en français](https://github.com/valorisa/Reverse-Engineer-Anything) | Documentation | Unofficial French-language guide to the original REA. |

**Name collision:** [mytechnotalent/rea](https://github.com/mytechnotalent/rea) is a separate project named *Reverse Engineering Assistant*, **not** the original *Reverse Engineer Anything*.

## Other AI-assisted reconstruction projects

This section covers the **broader wave of AI-assisted alternatives and recreations**. **REA usage is not claimed or verified for these repositories.** They are listed for discovery, not as REA success stories.

### ArtCraft family

An independent family of open-source creative and productivity applications inspired by popular commercial tools.

| Repository | Inspired by |
| --- | --- |
| [PhotoCraft](https://github.com/storytold/photocraft) | Adobe Photoshop |
| [LightCraft](https://github.com/storytold/lightcraft) | Adobe Lightroom |
| [FilmCraft](https://github.com/storytold/filmcraft) | Adobe Premiere Pro |
| [VectorCraft](https://github.com/storytold/vectorcraft) | Adobe Illustrator |
| [EffectCraft](https://github.com/storytold/effectcraft) | Adobe After Effects |
| [DesignCraft](https://github.com/storytold/designcraft) | Adobe InDesign |
| [PdfCraft](https://github.com/storytold/pdfcraft) | Adobe Acrobat |
| [WordCraft](https://github.com/storytold/wordcraft) | Microsoft Word |
| [GridCraft](https://github.com/storytold/gridcraft) | Microsoft Excel |
| [DeckCraft](https://github.com/storytold/deckcraft) | Microsoft PowerPoint |
| [CADCraft](https://github.com/storytold/cadcraft) | CAD software |
| [FigCraft](https://github.com/storytold/figcraft) | Figma |
| [SoundCraft](https://github.com/storytold/soundcraft) | Digital audio workstations |

These are **inspired-by projects**, not guaranteed feature-equivalent replacements. Availability, maturity, and functionality vary.

## Community lists and resources

Further indexes may include case studies, discussions, related AI-assisted work, and projects without public source code. Their inclusion criteria are broader than those of All-REA.

| Resource | Notes |
| --- | --- |
| [Awesome REA Cases](https://github.com/songshikang0111/awesome-REA-cases) · [English index](https://github.com/songshikang0111/awesome-REA-cases/blob/main/INDEX.en.md) | Large, actively updated case collection; **includes non-REA AI-assisted reverse engineering**. |
| [rea-gems](https://github.com/sqwu/rea-gems) | Community discovery index of REA-related repositories and cases. |
| [awesome-rea](https://github.com/yibie/awesome-rea) | Additional REA resource collection. |
| [rea-casebook](https://github.com/aliaihub/rea-casebook) | Additional curated REA examples and notes. |
| [awesome-REA-cases](https://github.com/beyondchenlin/awesome-REA-cases) | Further community collection of REA cases. |

## Contributing

Found a project that should be here? Contributions are welcome!

1. Check that the repository is public and the URL works.
2. Open an [issue](https://github.com/ismagoat/All-REA/issues) or a pull request.
3. Include the repository link, a one-sentence description, and a link to the evidence showing whether REA was used.
4. Specify the correct category: **REA used**, **REA tested**, **REA ecosystem**, or **other AI-assisted work**.
5. Mention if the project is a proof of concept, a work in progress, or actively maintained.

For quick submissions, copy this template into an issue:

```text
Repository:
Original software / target (if any):
What the project does:
REA relationship (used / tested / related / not used):
Evidence URL:
Status:
```

### Curation principles

- Prefer **code repositories** over social-media posts and unsupported claims.
- Attribute claims to their authors; do **not** imply independent validation.
- Avoid duplicates and distinguish forks from original implementations.
- Clearly label projects **not using REA**.
- Do not redistribute proprietary source code, commercial assets, credentials, or copyrighted game files.

---

**All-REA is an unofficial community directory.** It is not affiliated with, endorsed by, or maintained by the authors of REA or any of the applications mentioned. All trademarks belong to their respective owners. Each linked project has its own license and terms.

Made for developers, researchers, and anyone curious about what AI-assisted reverse engineering can (and cannot yet) build.
