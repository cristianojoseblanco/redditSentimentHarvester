import sys
import os

# Garante que o diretório raiz do projeto esteja no sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.api.reddit_client import RedditClient

def test_client_initialization():
    client = RedditClient()
    assert client is not None
    print("✅ RedditClient foi inicializado com sucesso!")
    posts = client.fetch_posts()
    for post in posts:
        print(f"{post['title'][:80]}...")  # mostra só o começo do título

if __name__ == "__main__":
    test_client_initialization()
