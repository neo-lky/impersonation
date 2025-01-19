"""A Discord client that can respond to messages."""

import asyncio
import logging
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

        self.pending_tasks: dict[int, asyncio.Task] = {}

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

        self.logger.info(
            f"Received message from {message.author.name}: {message.content}"
        )
        channel_id = message.channel.id
        if channel_id in self.pending_tasks:
            task = self.pending_tasks[channel_id]
            if not task.done():
                task.cancel()
                self.logger.debug(f"Cancelled existing task for channel {channel_id}")

        task = asyncio.create_task(self._handle_response_after_delay(message.channel))
        self.pending_tasks[channel_id] = task

    async def _handle_response_after_delay(self, channel: discord.DMChannel) -> None:
        """Wait for a while and respond to the latest message in the channel.

        Args:
            channel (discord.DMChannel): The channel to respond in.
        """
        try:
            await asyncio.sleep(8)

            past_messages = await self._get_past_messages(channel)
            responses = await self.agent.generate_response(past_messages)
            self.logger.info("Responses: \n%s", "\n".join(f"{r!s}" for r in responses))

            for response in responses:
                async with channel.typing():
                    await asyncio.sleep(len(response.content) * 0.15)
                    await channel.send(response.content)
                await asyncio.sleep(1)

        except asyncio.CancelledError:
            self.logger.debug(f"Response task for channel {channel.id} was cancelled.")
        except Exception as e:
            self.logger.error(f"Error in handle_response_after_delay: {e}")
        finally:
            if channel.id in self.pending_tasks:
                del self.pending_tasks[channel.id]

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
