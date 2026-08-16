# Marketing Audio Pipeline (Zynga)

**End-to-end AI pipeline automating audio production for video ads.** Built solo, from concept to production.

> Status: in production, used daily by Zynga's marketing team. Company IP — described here at a high level only; no code from this project is or will be published.

## What it does

Takes a raw video ad and produces broadcast-ready audio — voiceover, sound effects, and final mix — in minutes, with no manual sound-design pass.

## Architecture (high level)

```
video in
   │
   ├─ multimodal video analysis ──── Gemini 2.5 Pro
   ├─ competitor audio analysis ──── Whisper transcription → ChromaDB
   │
   ├─ VO + SFX cue generation ────── single LLM call (see below)
   │        │
   │        ├─ TTS ────────────────── ElevenLabs
   │        └─ SFX ────────────────── ElevenLabs Sound Generation
   │
   └─ mux + mix ──────────────────── ffmpeg, sidechain ducking
```

Orchestrated with **LangGraph**.

## Key design decision

**VO and SFX cues are generated in a single LLM call**, not separate ones. Splitting them looks cleaner architecturally, but produces audio that doesn't cohere — SFX that fight the voiceover's rhythm, cues that miss the narrative beat. One call, one creative context, coherent output.

## How I knew it worked

Adoption. The marketing team runs the pipeline without my involvement — the tool disappeared into the daily workflow, which was the actual goal. Turnaround for an ad's audio went from a sound designer's manual pass to minutes.
