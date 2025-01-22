"""A base class that represents an agent."""

from ..utils import sanitize_name


class BaseAgent:
    """A base class that represents an agent."""

    def __init__(self, name: str | None) -> None:
        self._name = sanitize_name(name or "Oujisama")

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
