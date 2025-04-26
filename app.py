# app.py

import streamlit as st
from use_case_generator import generate_use_cases 
from resource_collection import collect_resources
from sentiment_analysis import analyze_sentiment, label_sentiment, get_user_feedback
from visualization import display_wordcloud

# Streamlit App
st.set_page_config(page_title="Multi-Agentic Feedback Analyzer", layout="wide")

st.title("🧠 Multi-Agentic Sentiment Analyzer")

# Step 1: Get user feedback
st.header("Step 1: Enter your Feedback")

feedback_input = st.text_area("Enter feedbacks separated by a new line (press Shift+Enter for new line)", height=300)

if st.button("Analyze Feedbacks"):
    if feedback_input.strip() == "":
        st.error("Please enter some feedbacks first.")
    else:
        # Split the input into feedbacks
        feedbacks = feedback_input.strip().split('\n')

        # Step 2: Analyze Sentiment
        sentiment_results = analyze_sentiment(feedbacks)
        
        # Display Sentiment Analysis Results
        st.header("Step 2: Sentiment Analysis Results")
        for res in sentiment_results:
            sentiment_color = 'green' if res['sentiment_label'] == 'Positive' else 'red' if res['sentiment_label'] == 'Negative' else 'black'
            st.markdown(f"<p style='color:{sentiment_color}; font-size:18px;'>➤ {res['feedback']} — <strong>{res['sentiment_label']}</strong></p>", unsafe_allow_html=True)
        
        # Step 3: Use Case Generation
        use_cases = generate_use_cases(sentiment_results)
        st.header("Step 3: Suggested Use Cases")
        for case in use_cases:
            st.success(f"✔️ {case}")

        # Step 4: Resource Collection
        resources = collect_resources(sentiment_results)
        st.header("Step 4: Recommended Resources")
        for resource in resources:
            st.info(f"📚 {resource}")

        # Step 5: Wordcloud Visualization
        st.header("Step 5: Wordcloud Visualization")

        positive_feedbacks = [d['feedback'] for d in sentiment_results if d['sentiment_label'] == 'Positive']
        negative_feedbacks = [d['feedback'] for d in sentiment_results if d['sentiment_label'] == 'Negative']

        if positive_feedbacks or negative_feedbacks:
            pos_wc = display_wordcloud(positive_feedbacks, 'Positive') if positive_feedbacks else None
            neg_wc = display_wordcloud(negative_feedbacks, 'Negative') if negative_feedbacks else None

            if pos_wc and neg_wc:
                st.subheader("Positive and Negative Wordclouds")
                # Display using subplots
                import matplotlib.pyplot as plt
                plt.figure(figsize=(14, 7))
                plt.subplot(1, 2, 1)
                st.pyplot(display_wordcloud(pos_wc, 'Positive'))
                plt.subplot(1, 2, 2)
                st.pyplot(display_wordcloud(neg_wc, 'Negative'))
                plt.tight_layout()
            elif pos_wc:
                st.subheader("Positive Feedback Wordcloud")
                st.pyplot(display_wordcloud(pos_wc, 'Positive'))
            elif neg_wc:
                st.subheader("Negative Feedback Wordcloud")
                st.pyplot(display_wordcloud(neg_wc, 'Negative'))

