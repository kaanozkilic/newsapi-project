## # News Sentiment Analysis Project

This project aims to automate the process of gathering news online through using API and making sentiment analysis on gathered news. The sentiment analysis returns if the news have a sentiment of positive, negative or neither. 

## Dependencies

- requests
- os
- python-dotenv
- textblob
- vaderSentiment
- matplotlib
- csv

## How the project works

1.  The user enters a topic.
    
2.  News articles are fetched from NewsAPI in JSON format. '.env' file variable for API key is required to be there for this process. 
    
3.  Fields from each article are extracted.
    
4.  Sentiment analysis is made to extracted texts.
    
5.  Results are saved to a CSV file and visualized by matplotlib.
    
## Sentiment analysis logic

Article titles and descriptions are analyzed using two sentiment models.

**TextBlob** and **VADER** is used for the sentiment analysis. TextBlob is more of a text-based NLP while VADER also evaluates stuff like emojis and capitalization of the words. In order to get a healthy result, both are implemented and an average result is taken into consideration.

## Project files

-   **main.py**  
    Program's entry point. Other scripts' instances are instantiated here.
    
-   **config.py**  
    Loads the API key from environment variables (.env file).
    
-   **data_fetcher.py**  
    Sends request via NewsAPI while using the key from config.py script.
    
-   **sentiment_analyzer.py**  
    Does the sentiment analysis on news text using TextBlob and VADER and gives a sentiment label.
    
-   **csv_writer.py**  
    Saves the results into a CSV file.
    
-   **graph_plotter.py**  
    Generates charts showing sentiment distribution and sentiment scores.

## Authors

Kaan Özkilic / @kaanic
Shuvojyoti Singha