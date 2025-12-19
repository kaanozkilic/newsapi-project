"""
simple graph plotter for sentiment analysis
"""

import matplotlib.pyplot as plt


BASE_DIR = "results/charts/"


class GraphPlotter:
    """creates simple graphs for sentiment analysis results"""
    
    def __init__(self):
        pass
    
    def plot_sentiment_distribution(self, analyzed_articles):
        """
        creates a pie chart of sentiment distribution
        
        args:
            analyzed_articles: list of analyzed article dictionaries
        """
        # counting sentiments
        positives = sum(1 for a in analyzed_articles if a['sentiment_label'] == 'Positive')
        negatives = sum(1 for a in analyzed_articles if a['sentiment_label'] == 'Negative')
        neutrals = sum(1 for a in analyzed_articles if a['sentiment_label'] == 'Neutral')
        
        # data for pie chart
        labels = ['Positive', 'Neutral', 'Negative']
        sizes = [positives, neutrals, negatives]
        colors = ['#90EE90', '#FFD700', '#FF6B6B']
        
        # creating pie chart
        plt.figure(figsize=(8, 6))
        plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
        plt.title('sentiment distribution')
        plt.axis('equal')
        plt.tight_layout()
        plt.savefig(BASE_DIR + 'sentiment_distribution.png')
        plt.close()
        
        print(f"Saved to {BASE_DIR}: sentiment_distribution.png")
    
    def plot_sentiment_scores(self, analyzed_articles):
        """
        creates a bar chart of average sentiment scores
        
        args:
            analyzed_articles: list of analyzed article dictionaries
        """
        # getting sentiment scores
        scores = [a['avg_sentiment'] for a in analyzed_articles]
        articles = [f"#{i+1}" for i in range(len(analyzed_articles))]
        
        # color based on sentiment
        colors = ['green' if s > 0.1 else 'red' if s < -0.1 else 'gray' for s in scores]
        
        # creating bar chart
        plt.figure(figsize=(12, 6))
        plt.bar(articles, scores, color=colors, alpha=0.7)
        plt.axhline(y=0, color='black', linestyle='-', linewidth=0.5)
        plt.axhline(y=0.1, color='green', linestyle='--', linewidth=0.5, alpha=0.3)
        plt.axhline(y=-0.1, color='red', linestyle='--', linewidth=0.5, alpha=0.3)
        plt.ylim(-1, 1)
        plt.xlabel('article number')
        plt.ylabel('sentiment score')
        plt.title('sentiment scores by article')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.savefig(BASE_DIR + 'sentiment_scores.png')
        plt.close()
        
        print(f"Saved to {BASE_DIR}: sentiment_scores.png")
    
    def plot_all(self, analyzed_articles):
        """
        creates all graphs
        
        args:
            analyzed_articles: list of analyzed article dictionaries
        """
        print("\nGenerating graphs...")
        self.plot_sentiment_distribution(analyzed_articles)
        self.plot_sentiment_scores(analyzed_articles)
        print("All graphs generated!\n")


# testing the plotter
if __name__ == "__main__":
    # fake data for testing
    test_data = [
        {'sentiment_label': 'Positive', 'avg_sentiment': 0.5},
        {'sentiment_label': 'Negative', 'avg_sentiment': -0.3},
        {'sentiment_label': 'Neutral', 'avg_sentiment': 0.05},
        {'sentiment_label': 'Positive', 'avg_sentiment': 0.7},
        {'sentiment_label': 'Negative', 'avg_sentiment': -0.6},
    ]
    
    plotter = GraphPlotter()
    plotter.plot_all(test_data)
    print("test complete!")