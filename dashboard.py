import streamlit as st

from scraper import extract_article_text
from sentiment_analysis import find_sentiment_intensity
from summarizer import summarize

st.set_page_config(layout='wide', page_title='Article Summarizer and Sentiment Analyzer', page_icon="📰")

with st.container():
    st.title("📰 Article Summarizer & Sentiment Analyzer")
    st.caption("Powered by Gemini, Trafilatura & NLTK | Analyze any article in seconds")


full_text = None

col1, col2, col3 = st.columns(3)

with col1:
    with st.form(key='form'):
        url = st.text_input('Enter URL:')
        submit = st.form_submit_button('Submit')

        if submit and url:
            full_text = extract_article_text(url)

            if full_text:
                st.success('Article extracted successfully!')

            else:
                st.error('Failed to extract article. Try a different URL.')

        elif submit and not url:
            st.warning('URL cannot be empty!')

with col2:
    st.subheader('Summary')

    if not full_text:
        st.info("Working on it!")

    else:
        st.markdown(summarize(full_text))

with col3:
    st.subheader('Sentiment Analysis')

    if not full_text:
        st.info("Sentiment analysis will appear here after extraction.")

    if full_text:
        sentiment = find_sentiment_intensity(full_text)
        st.bar_chart(sentiment)
        st.markdown('##### Understanding the Sentiment Values')
        st.info("""
                    The values ranges between -1 (negative sentiment) to 1 (positive sentiment).\n
                    The 'neg' column displays the negative intensity.\n
                    The 'neu' column displays the neutral intensity.\n
                    The 'pos' column displays the positive intensity.\n
                    The 'compound' column displays the overall intensity.\n
                    A higher value corresponds to a higher intensity of that index and vice-versa.
                    """)