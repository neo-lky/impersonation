"""A module that defines a message class."""

from datetime import datetime

from pydantic import BaseModel, Field, field_validator

from ....utils.sanitize_name import sanitize_name


class Message(BaseModel):
    """A message class that represents a message sent by a user."""

    sender: str
    content: str
    timestamp: datetime = Field(default_factory=datetime.now)

    @field_validator("sender")
    @classmethod
    def sanitize_sender(cls, v: str) -> str:
        """Sanitize the sender name before setting it."""
        return sanitize_name(v)

    def __str__(self) -> str:
        time_str = self.timestamp.ctime()
        return f"[{time_str}] {self.sender}: {self.content}"
