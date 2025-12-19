from data_fetcher import DataFetcher
from sentiment_analyzer import SentimentAnalyzer
from graph_plotter import GraphPlotter
from csv_writer import CSVWriter

# constants for files
OUTPUT_FILE_DIR = "results/"
OUTPUT_FILE = "news_sentiment_results.csv"


def main():
    # 1. init class instances
    fetcher = DataFetcher()
    analyzer = SentimentAnalyzer()
    plotter = GraphPlotter()
    csv_writer = CSVWriter(OUTPUT_FILE_DIR + OUTPUT_FILE)

    # 2. defining search topic
    topic = input("What news topic do you want to analyze: ")

    # 3. fetching articles
    articles = fetcher.fetch_news(topic, page_size=50)

    if not articles:
        print("No articles found. Exiting.")
        return

    print("\nAnalyzing sentiment...\n")

    analyzed_articles = []

    # 4. analyzing each article
    for article in articles:
        info = fetcher.get_article_info(article)
        sentiment = analyzer.analyze_article(info)

        # unpacking the dicts
        combined = {
            **info,
            **sentiment
        }

        analyzed_articles.append(combined)

        # quick result
        print(f"- {info['title'][:60]}...")
        print(f"Sentiment: {sentiment['sentiment_label']} ({sentiment['avg_sentiment']})\n")

    print(f"Analyzed {len(analyzed_articles)} articles.")

    # 5. saving to csv
    csv_writer.save_articles(analyzed_articles)

    # 6. sentiment analysis summary - cli
    positives = sum(1 for a in analyzed_articles if a['sentiment_label'] == 'Positive')
    negatives = sum(1 for a in analyzed_articles if a['sentiment_label'] == 'Negative')
    neutrals = sum(1 for a in analyzed_articles if a['sentiment_label'] == 'Neutral')

    print("\nSentiment Summary:")
    print(f"Positive: {positives}")
    print(f"Neutral:  {neutrals}")
    print(f"Negative: {negatives}")

    # 7. plotting graphs
    plotter.plot_all(analyzed_articles)


if __name__ == "__main__":
    main()