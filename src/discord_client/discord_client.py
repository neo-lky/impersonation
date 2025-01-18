"""A Discord client that can respond to messages."""

import asyncio
import logging
import time
from datetime import datetime, timedelta

import discord

from ..agent import Agent, ConversationAgent
from ..utils import Config, Message


class DiscordClient(discord.Client):
    """A Discord client that can respond to messages."""

    def __init__(self, agent: Agent | None = None, token: str | None = None) -> None:
        super().__init__()
        self.logger = logging.getLogger("discord")
        self.logger.setLevel(logging.DEBUG)
        self.handler = logging.FileHandler(
            filename="discord.log", encoding="utf-8", mode="w"
        )
        self.handler.setFormatter(
            logging.Formatter("[%(asctime)s] [%(levelname)s] %(name)s: %(message)s")
        )
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(
            logging.Formatter("[%(asctime)s] [%(levelname)s] %(name)s: %(message)s")
        )
        self.logger.addHandler(self.handler)
        self.logger.addHandler(console_handler)

        self.agent = agent or ConversationAgent()
        self.token = token or Config.DISCORD_TOKEN

    def start_client(self) -> None:
        """Start the Discord client."""
        while True:
            try:
                self.run(self.token, log_handler=self.handler, log_level=logging.INFO)
            except discord.errors.ConnectionClosed:
                self.logger.error("Connection closed. Reconnecting...")
            except KeyboardInterrupt:
                self.logger.info("Shutting down...")
                return
            except Exception as e:
                self.logger.error(f"An error occurred: {e}")
            time.sleep(5)

    async def on_ready(self) -> None:
        """Print a message when the client is connected."""
        self._update_agent_name()
        self.logger.info(f"Logged on as {self.user}!")

    async def on_message(self, message: discord.Message) -> None:
        """Respond to a message.

        Args:
            message (discord.Message): The message to respond to.
        """
        self._update_agent_name()
        if (
            not isinstance(message.channel, discord.DMChannel)
            or message.author == self.user
        ):
            return

        past_messages = await self._get_past_messages(message.channel)
        self.logger.info(
            "Past messages: \n%s", "\n".join(f"{m!s}" for m in past_messages)
        )
        await asyncio.sleep(0.5)

        responses = self.agent.generate_response(past_messages)
        self.logger.info("Responses: \n%s", "\n".join(f"{r!s}" for r in responses))
        for response in responses:
            async with message.channel.typing():
                await asyncio.sleep(len(response.content) * 0.15)
                await message.channel.send(response.content)
            await asyncio.sleep(0.5)

    async def _get_past_messages(self, channel: discord.DMChannel) -> list[Message]:
        four_hours_ago = datetime.now() - timedelta(hours=4)
        messages = [
            Message(
                sender=msg.author.name,
                content=msg.content,
                timestamp=msg.created_at,
            )
            async for msg in channel.history(limit=None, after=four_hours_ago)
        ]

        return messages

    def _update_agent_name(self) -> None:
        """Update the agent's name to match the client's name."""
        if self.user is not None:
            self.agent.name = self.user.name
