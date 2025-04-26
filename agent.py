# agent.py

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from wordcloud import WordCloud
import matplotlib.pyplot as plt

class SentimentAgent:
    def __init__(self):
        self.analyzer = SentimentIntensityAnalyzer()

    def analyze_sentiment(self, text):
        sentiment_score = self.analyzer.polarity_scores(text)
        if sentiment_score['compound'] >= 0.05:
            return "Positive"
        elif sentiment_score['compound'] <= -0.05:
            return "Negative"
        else:
            return "Neutral"

class VisualizationAgent:
    def __init__(self):
        pass

    def create_wordcloud(self, positive_text, negative_text):
        positive_wc = WordCloud(
            width=800, 
            height=400, 
            background_color='white', 
            colormap='spring'
        ).generate(positive_text)

        negative_wc = WordCloud(
            width=800, 
            height=400, 
            background_color='white', 
            colormap='autumn'
        ).generate(negative_text)

        plt.figure(figsize=(14,7))

        plt.subplot(1, 2, 1)
        plt.imshow(positive_wc, interpolation='bilinear')
        plt.axis('off')
        plt.title('Positive Feedback', fontsize=18, color='green')

        plt.subplot(1, 2, 2)
        plt.imshow(negative_wc, interpolation='bilinear')
        plt.axis('off')
        plt.title('Negative Feedback', fontsize=18, color='red')

        plt.tight_layout()
        plt.show()
