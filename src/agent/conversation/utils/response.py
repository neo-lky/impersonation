"""A pydantic model for a response from the ConversationAgent."""

from pydantic import BaseModel, field_validator


class Response(BaseModel):
    """A response from the ConversationAgent."""

    is_other_person_finished_talking: bool
    responses: list[str] | None

    @field_validator("responses")
    @classmethod
    def sanitize_responses(cls, responses: list[str] | None) -> list[str] | None:
        """Sanitize the responses name before setting it."""
        if responses is None:
            return None

        return [response.strip() for response in responses if response.strip()]
