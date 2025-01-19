"""A module for the GrokAgent class."""

from openai import AsyncOpenAI
from openai.types.chat import (
    ChatCompletionAssistantMessageParam,
    ChatCompletionMessageParam,
    ChatCompletionSystemMessageParam,
    ChatCompletionUserMessageParam,
    ParsedChatCompletion,
)

from ...utils import Config, Message
from ..agent_abc import Agent
from .utils import Response


class ConversationAgent(Agent):
    """A class for the ConversationAgent."""

    def __init__(self, name: str | None = None, api_key: str | None = None) -> None:
        super().__init__(name or "Grok")
        self.client = AsyncOpenAI(
            api_key=api_key or Config.OPENAI_API_KEY,
            # base_url="https://api.x.ai/v1",
        )
        self.model = "gpt-4o"

        self.example_chat_history = self._load_text("src/text_files/chat_history.txt")
        self.prompt = (
            self._load_text("src/text_files/prompt.txt") + self.example_chat_history
        )

    def _load_text(self, file_path: str) -> str:
        with open(file_path, encoding="utf-8") as f:
            return "".join(f.readlines())

    async def generate_response(self, messages: list[Message]) -> list[Message]:
        """Generate a response to a list of messages.

        Args:
            messages (list[Message]): A list of messages to respond to.

        Returns:
            list[Message]: A list of responses to the messages.
        """
        llm_messages: list[ChatCompletionMessageParam] = [
            ChatCompletionSystemMessageParam(content=self.prompt, role="system")
        ]
        llm_messages += [
            ChatCompletionAssistantMessageParam(
                content=message.content, name=message.sender, role="assistant"
            )
            if message.sender == self.name
            else ChatCompletionUserMessageParam(
                content=message.content, name=message.sender, role="user"
            )
            for message in messages
        ]

        completion: ParsedChatCompletion[
            Response
        ] = await self.client.beta.chat.completions.parse(
            model=self.model, messages=llm_messages, response_format=Response
        )
        response = completion.choices[0].message.parsed

        if (
            response is None
            or response.responses is None
            or not response.is_other_person_finished_talking
        ):
            return []

        response_messages = [
            Message(sender=self.name, content=message) for message in response.responses
        ]
        return response_messages
