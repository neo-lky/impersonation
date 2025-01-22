"""Main file to run the bot."""

from src.agent import XAI, ConversationAgent
from src.discord_client import DiscordClient
from src.utils import Config

llm_client = XAI(api_key=Config.XAI_API_KEY)
agent = ConversationAgent(client=llm_client)
discord = DiscordClient(agent=agent, token=Config.DISCORD_TOKEN)
discord.start_client()
