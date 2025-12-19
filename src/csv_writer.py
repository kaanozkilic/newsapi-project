"""
handling CSV file operations
"""

import csv


class CSVWriter:
    
    def __init__(self, output_file="news_sentiment_results.csv"):
        self.output_file = output_file
    
    def save_articles(self, analyzed_articles):
        """
        save analyzed articles to a CSV file.
        
        args:
            analyzed_articles: list of dictionaries containing article data
            
        returns:
            bool: True if successful, False otherwise
        """
        if not analyzed_articles:
            print("No articles to save.")
            return False
        
        try:
            fieldnames = analyzed_articles[0].keys()
            
            with open(self.output_file, mode="w", newline="", encoding="utf-8") as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(analyzed_articles)
            
            print(f"\nResults saved to {self.output_file}")
            return True
            
        except Exception as e:
            print(f"Error saving CSV: {e}")
            return False