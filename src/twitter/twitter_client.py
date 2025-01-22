"""A Twitter client that impersonate a user Twitter interaction."""

from tweepy.asynchronous import AsyncClient


class TwitterClient:
    """A Twitter client that impersonate a user Twitter interaction."""

    def __init__(
        self,
        bearer_token: str,
        api_key: str,
        api_secret_key: str,
        access_token: str,
        access_token_secret: str,
    ) -> None:
        self.client = AsyncClient(
            bearer_token=bearer_token,
            consumer_key=api_key,
            consumer_secret=api_secret_key,
            access_token=access_token,
            access_token_secret=access_token_secret,
        )

    async def post_tweet(self, text: str) -> None:
        """Post a tweet.

        Args:
            text (str): The text of the tweet.
        """
        await self.client.create_tweet(text=text)

    async def like_tweet(self, tweet_id: int) -> None:
        """Like a tweet.

        Args:
            tweet_id (int): The ID of the tweet to like.
        """
        await self.client.like(tweet_id)

    async def follow_user(self, user_id: int) -> None:
        """Follow a user.

        Args:
            user_id (int): The ID of the user to follow.
        """
        await self.client.follow_user(target_user_id=user_id)

    async def send_direct_message(self, recipient_id: int, text: str) -> None:
        """Send a direct message to a user.

        Args:
            recipient_id (int): The ID of the user to send the message to.
            text (str): The text of the message.
        """
        await self.client.create_direct_message(participant_id=recipient_id, text=text)

    async def get_user_timeline(self, user_id: int, max_results: int = 5) -> None:
        """Get the timeline of a user.

        Args:
            user_id (int): The ID of the user.
            max_results (int, optional): The maximum number of tweets to return.
                Defaults to 5.
        """
        response = await self.client.get_users_tweets(
            id=user_id, max_results=max_results
        )
        for tweet in response.data:
            print(tweet.text)

    async def search_tweets(self, query: str, max_results: int = 5) -> None:
        """Search for tweets.

        Args:
            query (str): The search query.
            max_results (int, optional): The maximum number of tweets to return.
                Defaults to 5.
        """
        response = await self.client.search_recent_tweets(
            query=query, max_results=max_results
        )
        for tweet in response.data:
            print(tweet.text)

    async def reply_to_tweet(self, tweet_id: int, text: str) -> None:
        """Reply to a tweet.

        Args:
            tweet_id (int): The ID of the tweet to reply to.
            text (str): The text of the reply.
        """
        await self.client.create_tweet(text=text, in_reply_to_tweet_id=tweet_id)

    async def retweet(self, tweet_id: int) -> None:
        """Retweet a tweet.

        Args:
            tweet_id (int): The ID of the tweet to retweet.
        """
        await self.client.retweet(tweet_id)

    async def quote_retweet(self, text: str, tweet_id: str) -> None:
        """Quote retweet a tweet.

        Args:
            text (str): The text of the quote retweet.
            tweet_id (str): The ID of the tweet to quote retweet.
        """
        await self.client.create_tweet(text=text, quoted_tweet_id=tweet_id)
