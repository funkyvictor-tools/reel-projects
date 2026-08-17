# Victor Solà — AI Audio Tools & Pipelines

**Associate Audio Director @ Zynga (Socialpoint) · Barcelona**

I build AI-powered audio tools that eliminate repetitive work — from internal pipelines shipping daily at a major game studio, to independent products with paying customers.

This repo is a technical showcase of selected projects. Some codebases are private (commercial products or company IP), so each project page includes architecture, design decisions, and demos instead.

---

## Projects

| Project | What it is | Status |
|---|---|---|
| [SFX Forge](projects/sfx-forge.md) | Local text-to-SFX workbench with multi-provider abstraction (Stable Audio + ElevenLabs) | Personal, v3 |
| [Wavebase](projects/wavebase.md) | AI audio tagging for untagged SFX libraries — LLM-based captioning | **Commercial, paying customers** |
| [Marketing Audio Pipeline](projects/marketing-audio-pipeline.md) | End-to-end LangGraph pipeline automating audio for video ads at Zynga | In production (company IP) |
| [PromptSnitch](projects/promptsnitch.md) | macOS menu bar app detecting PII/API keys before pasting into AI tools | Personal, v2 |

## Illustrative code

- [`examples/providers_pattern.py`](examples/providers_pattern.py) — the provider abstraction pattern used in SFX Forge to swap text-to-audio backends (Stable Audio, ElevenLabs Sound Generation) behind a single interface. Rewritten as a standalone, illustrative excerpt.

## Stack

Python (FastAPI, LangGraph), C# / Unity (game audio implementation), ChromaDB, Whisper, Gemini, ElevenLabs API, ffmpeg, SwiftUI.

## Contact

- LinkedIn: [linkedin.com/in/victorsola](https://www.linkedin.com/) <!-- TODO: replace with your actual LinkedIn URL -->
