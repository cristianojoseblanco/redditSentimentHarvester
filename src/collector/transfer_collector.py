from api.reddit_client import RedditClient

class TransferCollector:
    def __init__(self, reddit_client: RedditClient):
        self.reddit = reddit_client

    def search_transfers(self, query="transfer", subreddit="soccer", limit=20):
        print(f"🔍 Buscando posts com '{query}' em r/{subreddit}...")
        posts = self.reddit.search_posts(query=query, subreddit=subreddit, limit=limit)
        for post in posts:
            print(f"- {post['title']} ({post['score']} upvotes)")
        return posts
