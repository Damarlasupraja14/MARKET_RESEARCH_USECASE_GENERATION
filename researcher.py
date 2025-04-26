from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob

def get_user_feedback():
    feedbacks = []
    print("Enter feedbacks to analyze sentiment. Type 'exit' to finish.")
    while True:
        feedback = input("Enter feedback: ")
        if feedback.lower() == 'exit':
            break
        feedbacks.append(feedback)
    return feedbacks

def analyze_sentiment(feedbacks):
    analyzer = SentimentIntensityAnalyzer()
    sentiment_results = []

    for feedback in feedbacks:
        vader_score = analyzer.polarity_scores(feedback)
        textblob_score = TextBlob(feedback).sentiment

        sentiment_label = "Neutral"
        if vader_score['compound'] >= 0.05 or textblob_score.polarity > 0.1:
            sentiment_label = "Positive"
        elif vader_score['compound'] <= -0.05 or textblob_score.polarity < -0.1:
            sentiment_label = "Negative"

        sentiment_results.append({
            'feedback': feedback,
            'vader_score': vader_score,
            'textblob_score': textblob_score,
            'sentiment_label': sentiment_label
        })
    
    return sentiment_results
