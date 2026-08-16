# PromptSnitch

**macOS menu bar app that detects sensitive data (PII, API keys) before you paste it into AI tools.**

> Status: personal project, v2 (53 documented fixes over v1). Codebase private.

## Why it exists

Everyone using AI tools daily eventually pastes something they shouldn't — an API key buried in a stack trace, a customer email in a log. PromptSnitch sits in the menu bar and catches it *before* it leaves your clipboard.

## Features

- **Block Paste** — hard-stop pastes containing detected secrets/PII
- **Redact Paste** — paste with sensitive spans automatically masked
- **Trusted Destinations** — allow-list apps where pasting is safe
- **Test Detection** — sandbox to verify what the detectors catch
- **Today Stats** — dashboard of catches per day

## Stack & notes

SwiftUI, menu bar app (`MenuBarExtra`). One fun bug: menu bar icon rendering broke due to a `.menuBarExtraStyle(.menu)` vs `.window` mismatch — the kind of platform-specific detail that never shows up in tutorials.

Positioned as a standalone tool first, with a longer-term angle toward LLM-routing middleware with GDPR / EU AI Act compliance in mind.
