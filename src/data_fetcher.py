"""
data retriever from newsAPI
"""

import requests
from config import Config


class DataFetcher:
    def __init__(self):
        # getting API key from config
        config = Config()
        self.api_key = config.get_api_key()
        self.base_url = "https://newsapi.org/v2/everything"
    
    def fetch_news(self, query, language='en', page_size=100):
        """
        fetches news articles
        
        args:
            query: search keyword (e.g., "sakarin villapaita")
            language: language code (default: 'en')
            page_size: number of articles (max 100)
        
        returns:
            list of articles, empty list if error
        """
        # parameters
        params = {
            'q': query,
            'apiKey': self.api_key,
            'language': language,
            'pageSize': page_size,
            'sortBy': 'relevancy'
        }
        
        print(f"\nFetching articles about '{query}'...")
        print(f"Language: {language}")
        print(f"Max articles: {page_size}")
        
        try:
            # making API request
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            
            # parsing response
            data = response.json()
            
            if data['status'] == 'ok':
                articles = data['articles']
                print(f"retrieved {len(articles)} articles")
                return articles
            else:
                print(f"API error: {data.get('message', 'unknown error')}")
                return []
        
        except requests.exceptions.RequestException as e:
            print(f"request failed: {e}")
            return []
    
    def get_article_info(self, article):
        """getting basic info from the article"""
        return {
            'title': article.get('title', 'N/A'),
            'source': article.get('source', {}).get('name', 'N/A'),
            'author': article.get('author', 'N/A'),
            'published': article.get('publishedAt', 'N/A'),
            'description': article.get('description', 'N/A'),
            'url': article.get('url', 'N/A'),
            'content': article.get('content', 'N/A')
        }


# testing the fetcher
if __name__ == "__main__":
    try:
        fetcher = DataFetcher()
        
        # fetching news
        articles = fetcher.fetch_news("artificial intelligence", page_size=5)
        
        if articles:
            print(f"\ntest successful!")
            print(f"\nfirst article:")
            info = fetcher.get_article_info(articles[0])
            print(f"title: {info['title']}")
            print(f"source: {info['source']}")
        else:
            print("\nno articles retrieved")
    
    except Exception as e:
        print(f"error: {e}")