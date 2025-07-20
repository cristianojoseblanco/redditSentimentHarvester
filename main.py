import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.api.reddit_client import RedditClient
from src.collector.transfer_collector import TransferCollector


# ✅ Personalize sua busca
query = "football transfers"
subreddit = "soccer"
limit = 10

# ✅ Instancia o cliente do Reddit
reddit = RedditClient()

# ✅ Busca os dados
posts = reddit.search_posts(query=query, subreddit=subreddit, limit=limit)

# ✅ Mostra os resultados
for i, post in enumerate(posts, start=1):
    print(f"\nPost {i}")
    print(f"Title: {post['title']}")
    print(f"Score: {post['score']}")
    print(f"Created UTC: {post['created_utc']}")
    print(f"URL: {post['url']}")
