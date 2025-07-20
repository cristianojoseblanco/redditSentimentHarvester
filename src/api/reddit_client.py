import os
import praw
from dotenv import load_dotenv

class RedditClient:
    def __init__(self):
        load_dotenv()
        self.client_id = os.getenv("REDDIT_CLIENT_ID")
        self.client_secret = os.getenv("REDDIT_CLIENT_SECRET")
        self.user_agent = os.getenv("REDDIT_USER_AGENT")

        if not all([self.client_id, self.client_secret, self.user_agent]):
            raise ValueError("Algumas variáveis de ambiente estão faltando no .env")

        self.reddit = praw.Reddit(
            client_id=self.client_id,
            client_secret=self.client_secret,
            user_agent=self.user_agent
        )

    def get_posts(self, subreddit_name, limit=10):
        subreddit = self.reddit.subreddit(subreddit_name)
        posts = []
        for submission in subreddit.hot(limit=limit):
            posts.append({
                "title": submission.title,
                "selftext": submission.selftext,
                "score": submission.score,
                "created_utc": submission.created_utc,
                "id": submission.id,
                "url": submission.url
            })
        return posts
