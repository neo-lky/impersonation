"""A module for the GrokAgent class."""

from openai.types.chat import (
    ChatCompletionAssistantMessageParam,
    ChatCompletionMessageParam,
    ChatCompletionSystemMessageParam,
    ChatCompletionUserMessageParam,
    ParsedChatCompletion,
)

from ..base_agent import BaseAgent
from ..utils import LLMClient
from .utils import Message, Response


class ConversationAgent(BaseAgent):
    """A class for the ConversationAgent."""

    def __init__(self, client: LLMClient, name: str | None = None) -> None:
        super().__init__(name)
        self.client = client

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
            model=self.client.model, messages=llm_messages, response_format=Response
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
