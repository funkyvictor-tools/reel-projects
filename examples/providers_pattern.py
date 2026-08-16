"""
Provider abstraction pattern — illustrative excerpt.

This is a standalone, rewritten example of the pattern used in SFX Forge
to support multiple text-to-audio backends (Stable Audio, ElevenLabs
Sound Generation) behind a single interface. It is not the production
code; it exists to show the design.

Key ideas:
  1. Each provider declares its own parameter schema. The frontend
     renders controls dynamically from that schema — no hardcoded UI
     per provider.
  2. The app talks to `generate()` only. Swapping or adding providers
     never touches the workbench logic (takes, regions, inpainting).
  3. API keys come from the environment, never from code or requests.
"""

from __future__ import annotations

import os
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any


@dataclass
class ParamSpec:
    """A single provider parameter, renderable as a UI control."""
    name: str
    label: str
    kind: str                      # "float" | "int" | "text" | "select"
    default: Any = None
    minimum: float | None = None
    maximum: float | None = None
    choices: list[str] = field(default_factory=list)


@dataclass
class GenerationResult:
    audio_bytes: bytes
    sample_rate: int
    provider: str
    prompt: str
    params: dict[str, Any]


class AudioProvider(ABC):
    """Base class every text-to-audio backend implements."""

    id: str
    display_name: str

    @abstractmethod
    def param_schema(self) -> list[ParamSpec]:
        """Parameters this provider exposes. Drives the dynamic UI."""

    @abstractmethod
    def generate(self, prompt: str, **params: Any) -> GenerationResult:
        """Generate audio for a prompt. Raises ProviderError on failure."""

    def _require_key(self, env_var: str) -> str:
        key = os.environ.get(env_var, "")
        if not key:
            raise ProviderError(
                f"{self.display_name}: missing {env_var}. "
                f"Set it in your .env file."
            )
        return key


class ProviderError(RuntimeError):
    pass


class ElevenLabsSoundGen(AudioProvider):
    id = "elevenlabs"
    display_name = "ElevenLabs Sound Generation"

    def param_schema(self) -> list[ParamSpec]:
        return [
            ParamSpec("duration_seconds", "Duration (s)", "float",
                      default=5.0, minimum=0.5, maximum=22.0),
            ParamSpec("prompt_influence", "Prompt influence", "float",
                      default=0.3, minimum=0.0, maximum=1.0),
        ]

    def generate(self, prompt: str, **params: Any) -> GenerationResult:
        api_key = self._require_key("ELEVENLABS_API_KEY")
        # ... POST to the Sound Generation endpoint, stream bytes ...
        raise NotImplementedError("Illustrative excerpt")


class StableAudioSFX(AudioProvider):
    id = "stable_audio"
    display_name = "Stable Audio (Small-SFX)"

    def param_schema(self) -> list[ParamSpec]:
        return [
            ParamSpec("duration_seconds", "Duration (s)", "float",
                      default=4.0, minimum=0.5, maximum=11.0),
            ParamSpec("steps", "Diffusion steps", "int",
                      default=8, minimum=1, maximum=50),
            ParamSpec("cfg_scale", "CFG scale", "float",
                      default=1.0, minimum=0.0, maximum=15.0),
        ]

    def generate(self, prompt: str, **params: Any) -> GenerationResult:
        # ... local inference or hosted endpoint ...
        raise NotImplementedError("Illustrative excerpt")


# --- Registry -----------------------------------------------------------

PROVIDERS: dict[str, AudioProvider] = {
    p.id: p for p in (ElevenLabsSoundGen(), StableAudioSFX())
}


def list_providers() -> list[dict[str, Any]]:
    """What the frontend calls to build the provider picker + dynamic UI."""
    return [
        {
            "id": p.id,
            "name": p.display_name,
            "params": [vars(spec) for spec in p.param_schema()],
        }
        for p in PROVIDERS.values()
    ]


def generate(provider_id: str, prompt: str, **params: Any) -> GenerationResult:
    provider = PROVIDERS.get(provider_id)
    if provider is None:
        raise ProviderError(f"Unknown provider: {provider_id}")
    return provider.generate(prompt, **params)
