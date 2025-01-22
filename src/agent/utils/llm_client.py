"""A module for providing the LLM clients."""

from abc import ABC, abstractmethod

import httpx
from openai import AsyncOpenAI


class LLMClient(AsyncOpenAI, ABC):
    """An abstract class for the LLM clients."""

    @property
    @abstractmethod
    def model(self) -> str:
        """Returns the model name."""


class XAI(LLMClient):
    """A class for the XAI client."""

    model = "grok-2-latest"
    base_url = httpx.URL("https://api.x.ai/v1")


class OpenAI(LLMClient):
    """A class for the OpenAI client."""

    model = "gpt-4o"
