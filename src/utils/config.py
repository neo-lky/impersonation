"""A module to store the configuration variables."""

import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    """A class to store the configuration variables."""

    XAI_API_KEY = str(os.getenv("XAI_API_KEY"))
    OPENAI_API_KEY = str(os.getenv("OPENAI_API_KEY"))
    DISCORD_TOKEN = str(os.getenv("DISCORD_TOKEN"))
