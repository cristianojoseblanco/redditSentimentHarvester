from src.api.reddit_client import RedditClient

client = RedditClient()
posts = client.get_posts("learnpython", limit=5)

for post in posts:
    print(f"{post['title'][:80]}...")  # mostra só o começo do título
