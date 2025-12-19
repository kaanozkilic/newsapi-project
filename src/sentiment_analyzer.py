"""
sentiment analyzer of the text
"""

from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


class SentimentAnalyzer:
    """analyzes sentiment using textBlob and vader"""
    
    def __init__(self):
        # init vader
        self.vader = SentimentIntensityAnalyzer()
        # print("sentiment analyzer inited")
    
    def analyze_textblob(self, text):
        """
        analyze sentiment using TextBlob
        
        args:
            text: text to analyze
        
        returns:
            tuple: (polarity, subjectivity)
            polarity: -1 (negative) to +1 (positive)
            subjectivity: 0 (objective) to 1 (subjective)
        """
        if not text:
            return 0, 0
        
        blob = TextBlob(text)
        return blob.sentiment.polarity, blob.sentiment.subjectivity
    
    def analyze_vader(self, text):
        """
        analyze sentiment using VADER
        
        args:
            text: text to analyze
        
        returns:
            float: compound score from -1 (negative) to +1 (positive)
        """
        if not text:
            return 0
        
        scores = self.vader.polarity_scores(text)
        return scores['compound']
    
    def get_sentiment_label(self, score):
        """
        convert sentiment score to label
        
        args:
            score: sentiment score
        
        returns:
            str: 'Positive', 'Negative', or 'Neutral'
        """

        if score >= 0.1:
            return 'Positive'
        elif score <= -0.1:
            return 'Negative'
        else:
            return 'Neutral'
    
    def analyze_article(self, article):
        """
        analyze a complete article
        
        args:
            article: article dictionary with 'title' and 'description'
        
        returns:
            dict: sentiment analysis results
        """
        # combining title and description for analysis
        title = article.get('title', '')
        description = article.get('description', '')
        full_text = f"{title} {description}"
        
        # getting both sentiment scores
        tb_polarity, tb_subjectivity = self.analyze_textblob(full_text)
        vader_score = self.analyze_vader(full_text)
        
        # calculating average sentiment
        avg_sentiment = (tb_polarity + vader_score) / 2
        
        # getting sentiment label
        label = self.get_sentiment_label(avg_sentiment)
        
        return {
            'textblob_polarity': round(tb_polarity, 3),
            'textblob_subjectivity': round(tb_subjectivity, 3),
            'vader_compound': round(vader_score, 3),
            'avg_sentiment': round(avg_sentiment, 3),
            'sentiment_label': label
        }


# testing the analyzer
if __name__ == "__main__":
    analyzer = SentimentAnalyzer()
    
    # testing with sample texts
    test_texts = [
        "This is amazing news! Great progress in AI technology.",
        "Terrible disaster causes widespread damage and concern.",
        "The meeting was held yesterday at the conference center."
    ]
    
    print("\ntesting sentiment analysis:\n")
    
    for text in test_texts:
        print(f"text: {text}")
        
        # creating a fake article
        article = {'title': text, 'description': ''}
        result = analyzer.analyze_article(article)
        
        print(f"  sentiment: {result['sentiment_label']}")
        print(f"  score: {result['avg_sentiment']}")
        print()
    
    print("sentiment analyzer working")