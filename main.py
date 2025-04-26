from visualization import generate_wordcloud, display_subplots, save_wordcloud
from researcher import get_user_feedback, analyze_sentiment
from use_case_generator import generate_use_cases
from resource_collection import collect_resources

def main():
    # Step 1: Get user feedback
    feedbacks = get_user_feedback()  # Get feedback from the user
    
    # Step 2: Analyze sentiment of feedbacks
    sentiment_results = analyze_sentiment(feedbacks)  # Analyze sentiment of the feedbacks

    # Step 3: Display sentiment results
    print("\nSentiment Analysis Results:")
    for res in sentiment_results:
        print(res)

    # Step 4: Prepare feedbacks for WordCloud
    positive_feedbacks = [d['feedback'] for d in sentiment_results if d['sentiment_label'] == 'Positive']
    negative_feedbacks = [d['feedback'] for d in sentiment_results if d['sentiment_label'] == 'Negative']

    # Step 5: Generate WordClouds for Positive and Negative feedback
    positive_wc = generate_wordcloud(positive_feedbacks, 'Positive')
    negative_wc = generate_wordcloud(negative_feedbacks, 'Negative')

    # Step 6: Display both WordClouds side by side as subplots
    display_subplots(positive_wc, negative_wc)
    
    # Step 7: Save the WordCloud images
    save_wordcloud(positive_wc, 'positive_feedback_wordcloud.png')
    save_wordcloud(negative_wc, 'negative_feedback_wordcloud.png')

    # Step 8: Generate Use Cases based on the feedback
    use_cases = generate_use_cases(sentiment_results)
    print("\nSuggested Use Cases:")
    for case in use_cases:
        print(case)

    # Step 9: Collect Resources for the feedback sentiment
    resources = collect_resources(sentiment_results)
    print("\nRecommended Resources for Improvement:")
    for resource in resources:
        print(resource)

if __name__ == "__main__":
    main()
