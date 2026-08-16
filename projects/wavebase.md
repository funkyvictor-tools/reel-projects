# Wavebase

**AI audio tagging for sound designers.** Point it at an untagged SFX library; get searchable, professionally captioned metadata.

> Status: **commercial product with paying customers**. Closed source.
> From a single LinkedIn post: 10 users, 4 sales — a 40% conversion rate.

<!-- TODO: add link to landing page / demo video -->

## The problem

Sound designers accumulate tens of thousands of untagged or badly tagged audio files. Existing tools rely on embedding-similarity transfer from already-tagged libraries — which means they have a cold-start problem: they can't help you with a library that has no tags to learn from.

## The approach

Wavebase uses cloud LLMs to **analyze the audio directly** and generate captions and structured metadata from scratch. No seed tags required. That's the core competitive differentiator versus embedding-based competitors.

- Tauri + React frontend, FastAPI Python backend
- LLM-based captioning pipeline with semantic rules
- CLAP-based confidence scoring in the classification path

## What building it taught me

- **Distribution beats features.** The product was strong for months; revenue only appeared when I focused on where game audio professionals actually are (Airwiggles, r/GameAudio, direct industry relationships).
- **Pricing AI products is a real design problem.** Perpetual licenses clash with variable LLM API costs — I evaluated BYO-API-key, credit systems, and perpetual-plus-update-window models.
- **The captioning pipeline is the moat.** It's also the foundation for the next feature ("Generate Similar") and for fine-tuning experiments in [SFX Forge](sfx-forge.md).
