"""An abstract class that represents an agent that can respond to messages."""

from abc import ABC, abstractmethod

from ..utils import Message, sanitize_name


class Agent(ABC):
    """An abstract class that represents an agent that can respond to messages."""

    def __init__(self, name: str) -> None:
        self._name = sanitize_name(name)

    @property
    def name(self) -> str:
        """Property for the name of the agent.

        Returns:
            str: The name of the agent.
        """
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        self._name = sanitize_name(value)

    @abstractmethod
    async def generate_response(self, messages: list[Message]) -> list[Message]:
        """Generate a response to a list of messages.

        Args:
            messages (list[Message]): A list of messages to respond to.

        Returns:
            list[Message]: A list of responses to the messages.
        """
