# SFX Forge

**Local text-to-SFX workbench for sound designers.** Python/FastAPI backend + single-file web UI.

> Status: personal project, v3. Codebase private (planned experiments include LoRA fine-tuning on studio-specific sound aesthetics).

<!-- TODO: add screenshot -->
<!-- ![SFX Forge UI](../assets/sfx-forge-ui.png) -->

## What it does

Generate, audition, and iterate on sound effects from text prompts — locally, fast, with the ergonomics a working sound designer actually needs (takes, regions, waveform view), not a generic web playground.

## Key features

- **Multi-provider generation** — Stable Audio (Small-SFX) and ElevenLabs Sound Generation behind a clean abstraction layer (`providers.py`). The UI adapts dynamically to each provider's parameters. Adding a third provider is a single class.
- **Region-based inpainting** — select a region of the waveform and regenerate only that section, with a child-takes system so every variation stays organized under its parent.
- **Takes workflow** — generate N variations per prompt, audition side by side, keep the winners. Mirrors how SFX auditioning actually works in game audio.
- **Waveform visualization** — inline, with region selection.
- **Zero-friction ops** — `run.sh` launcher, `.env`-based API key management, no cloud dependency for the app itself.

## Design decisions

- **Provider abstraction first.** Text-to-audio models are moving fast; the tool shouldn't be married to any of them. Each provider declares its own parameter schema, and the frontend renders controls from that schema. See the [illustrative excerpt](../examples/providers_pattern.py).
- **Single-file web UI.** No build step, no framework churn. The complexity budget goes to the audio workflow, not the frontend stack.
- **Local-first.** Generated audio, takes, and metadata live on disk where a sound designer's tools (and backup habits) already are.

## Relationship to Wavebase

SFX Forge is the generation half of a loop that [Wavebase](wavebase.md) closes: Wavebase's LLM captioning pipeline produces rich descriptions of existing libraries, which become training/conditioning data for generating *similar* sounds — "Generate Similar" as a feature, with the captioning pipeline as the moat.
