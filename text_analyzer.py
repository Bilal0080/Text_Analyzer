import streamlit as st
from collections import Counter
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import re

# Download necessary NLTK data
nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()

# Function to analyze text
def analyze_text(text):
    words = re.findall(r'\w+', text.lower())
    word_count = len(words)
    char_count = len(text)
    frequent_words = Counter(words).most_common(5)
    sentiment = sia.polarity_scores(text)
    sentiment_result = (
        "Positive" if sentiment['compound'] > 0 else
        "Negative" if sentiment['compound'] < 0 else "Neutral"
    )
    
    return {
        'word_count': word_count,
        'char_count': char_count,
        'frequent_words': frequent_words,
        'sentiment': sentiment_result
    }

# Streamlit UI with creative styling
st.set_page_config(page_title="Text Analyzer", page_icon="📝", layout="wide")
st.markdown("""
    <style>
        body {
            background-color: #f4f4f4;
            font-family: Arial, sans-serif;
        }
        .main-title {
            text-align: center;
            font-size: 36px;
            font-weight: bold;
            color: #ff5733;
        }
        .stTextArea {
            border: 2px solid #ff5733;
            border-radius: 10px;
        }
        .result-box {
            background-color: #fff;
            padding: 15px;
            border-radius: 10px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='main-title'>📝 Text Analyzer</h1>", unsafe_allow_html=True)

text = st.text_area("Enter your text here:")
if st.button("Analyze", key="analyze_btn"):
    if text.strip():
        result = analyze_text(text)
        
        st.markdown("<div class='result-box'>", unsafe_allow_html=True)
        st.subheader("Analysis Results")
        st.write(f"**📌 Word Count:** {result['word_count']}")
        st.write(f"**🔠 Character Count:** {result['char_count']}")
        st.write(f"**🔥 Most Frequent Words:** {result['frequent_words']}")
        st.write(f"**💡 Sentiment:** {result['sentiment']}")
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.warning("⚠️ Please enter some text to analyze.")
