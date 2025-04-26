import matplotlib.pyplot as plt
from wordcloud import WordCloud
import streamlit as st

def display_wordcloud(feedback_list, title):
    if not feedback_list:  # In case the list is empty
        st.write(f"No {title.lower()} feedbacks to display.")
        return
    
    text = ' '.join(feedback_list)
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    
    st.subheader(f"{title} Word Cloud")
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    st.pyplot(fig)  
