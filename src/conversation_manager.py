"""A module that manages a conversation between a user and an agent."""

from .agent.conversation import ConversationAgent, Message


class ConversationManager:
    """A class that manages a conversation between a user and an agent."""

    def __init__(self, agent: ConversationAgent, user_name: str | None = None) -> None:
        self.agent = agent
        self.user_name = user_name or "User"
        self.messages: list[Message] = []

    async def start_user_input_loop(self):
        """Continuously prompts the user for input and handles responses."""
        while True:
            try:
                user_input = input("You: ")
                if user_input.lower() in ["exit", "quit"]:
                    print("Conversation ended.")
                    break
                user_message = Message(sender=self.user_name, content=user_input)
                self.messages.append(user_message)
                print(user_message)
                agent_messages = await self.agent.generate_response(self.messages)
                for message in agent_messages:
                    self.messages.append(message)
                    print(message)
            except KeyboardInterrupt:
                print("\nConversation interrupted by user.")
                break
