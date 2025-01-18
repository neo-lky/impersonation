"""A pydantic model for a response from the ConversationAgent."""

from pydantic import BaseModel


class Response(BaseModel):
    """A response from the ConversationAgent."""

    is_other_person_finished_talking: bool
    responses: list[str] | None
