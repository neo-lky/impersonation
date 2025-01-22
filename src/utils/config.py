"""A module to store the configuration variables."""

import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    """A class to store the configuration variables."""

    XAI_API_KEY = str(os.getenv("XAI_API_KEY"))
    OPENAI_API_KEY = str(os.getenv("OPENAI_API_KEY"))
    DISCORD_TOKEN = str(os.getenv("DISCORD_TOKEN"))

    TWITTER_BEARER_TOKEN = str(os.getenv("TWITTER_BEARER_TOKEN"))
    TWITTER_API_KEY = str(os.getenv("TWITTER_API_KEY"))
    TWITTER_SECRET_KEY = str(os.getenv("TWITTER_SECRET_KEY"))
    TWITTER_ACCESS_TOKEN = str(os.getenv("TWITTER_ACCESS_TOKEN"))
    TWITTER_ACCESS_TOKEN_SECRET = str(os.getenv("TWITTER_ACCESS_TOKEN_SECRET"))
