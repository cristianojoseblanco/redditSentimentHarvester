from src.api.reddit_client import RedditClient

if __name__ == "__main__":
    client = RedditClient()
    
    # Buscar por transferências no subreddit de futebol
    posts = client.fetch_posts(subreddit="soccer", query="transfer", limit=20)

    for i, post in enumerate(posts, 1):
        print(f"{i}. {post['title']} (Score: {post['score']})")
        print(f"URL: {post['url']}")
        print(f"Comments: {post['num_comments']}")
        print("-" * 60)
