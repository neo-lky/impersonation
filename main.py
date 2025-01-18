"""Main file to run the bot."""

from src.discord_client.discord_client import DiscordClient

client = DiscordClient()
client.start_client()
