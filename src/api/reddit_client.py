import praw
from dotenv import load_dotenv
import os

load_dotenv()  # Carrega as variáveis do .env

class RedditClient:
    def __init__(self):
        self.reddit = praw.Reddit(
            client_id=os.getenv("REDDIT_CLIENT_ID"),
            client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
            user_agent=os.getenv("REDDIT_USER_AGENT")
        )

    def fetch_posts(self, subreddit="soccer", query="transfer", limit=10, sort="relevance", time_filter="day"):
        """
        Busca posts de um subreddit usando uma query.
        """
        subreddit_ref = self.reddit.subreddit(subreddit)
        posts = subreddit_ref.search(query, sort=sort, time_filter=time_filter, limit=limit)
        results = []
        for post in posts:
            results.append({
                "title": post.title,
                "score": post.score,
                "created_utc": post.created_utc,
                "url": post.url,
                "id": post.id,
                "author": str(post.author),
                "selftext": post.selftext,
                "num_comments": post.num_comments
            })
        return results
