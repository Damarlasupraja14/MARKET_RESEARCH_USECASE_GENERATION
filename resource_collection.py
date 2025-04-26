def collect_resources(sentiment_results):
    resources = []

    positive_feedbacks = [d['feedback'] for d in sentiment_results if d['sentiment_label'] == 'Positive']
    negative_feedbacks = [d['feedback'] for d in sentiment_results if d['sentiment_label'] == 'Negative']

    # Resources for improvement based on negative feedback
    if negative_feedbacks:
        resources.append("Consider reviewing tutorials on customer satisfaction improvement.")
        resources.append("Look into articles about complaint management and conflict resolution.")

    # Resources for maintaining positive feedback
    if positive_feedbacks:
        resources.append("Check out articles on enhancing customer experience and loyalty.")
        resources.append("Review case studies on successful businesses excelling in customer satisfaction.")

    return resources
