from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob

# Define the function
def label_sentiment(vader_compound_score):
    if vader_compound_score >= 0.05:
        return "Positive"
    elif vader_compound_score <= -0.05:
        return "Negative"
    else:
        return "Neutral"

# Function to analyze sentiment for user feedback
def analyze_sentiment(feedbacks):
    analyzer = SentimentIntensityAnalyzer()
    
    results = []

    for feedback in feedbacks:
        vader_score = analyzer.polarity_scores(feedback)
        textblob_score = TextBlob(feedback).sentiment
        sentiment_label = label_sentiment(vader_score['compound'])

        if 'good' in feedback.lower() or textblob_score.polarity > 0:
            sentiment_label = 'Positive'
        else:
            sentiment_label = 'Negative'


        result = {
            "feedback": feedback,
            "vader_score": vader_score,
            "textblob_score": textblob_score,
            "sentiment_label": sentiment_label
        }
        results.append(result)

    return results

# Get feedback from the user
def get_user_feedback():
    feedbacks = []
    print("Enter feedbacks to analyze sentiment. Type 'exit' to finish.")

    while True:
        feedback = input("Enter feedback: ")
        if feedback.lower() == 'exit':
            break
        feedbacks.append(feedback)
    
    return feedbacks

# For testing
if __name__ == "__main__":
    feedbacks = get_user_feedback()  # Get user feedback
    sentiment_results = analyze_sentiment(feedbacks)  # Analyze sentiment

    # Display results
    for res in sentiment_results:
        print(res)
