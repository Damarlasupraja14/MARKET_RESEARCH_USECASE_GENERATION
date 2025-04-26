def generate_use_cases(sentiment_results):
    positive_feedbacks = [d['feedback'] for d in sentiment_results if d['sentiment_label'] == 'Positive']
    negative_feedbacks = [d['feedback'] for d in sentiment_results if d['sentiment_label'] == 'Negative']

    use_cases = []

    if positive_feedbacks:
        use_cases.append("Consider expanding features or services that customers praised.")
    
    if negative_feedbacks:
        use_cases.append("Review customer complaints to improve areas of concern.")
    
    if len(positive_feedbacks) > len(negative_feedbacks):
        use_cases.append("Build on the positive feedback and enhance strengths.")
    
    if len(negative_feedbacks) > len(positive_feedbacks):
        use_cases.append("Focus on addressing weaknesses and customer pain points.")

    return use_cases
