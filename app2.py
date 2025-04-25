import numpy as np
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import seaborn as sns

df = pd.read_csv('expanded_eagle_island_sentiment_dataset.csv')
df['Date'] = pd.to_datetime(df['Date'])

st.title('Eagle Island Camp sentiment analysis project')
st.markdown('Explore different trends and patterns of sentiments in reviews by campers, parents and staff throughout camp season.')

# Sidebar Filters
with st.sidebar:
    st.header("Filter")
    program_filter = st.selectbox("Choose a program:", ["All"] + sorted(df['Program Name'].unique().tolist()))

# Apply filter
if program_filter != "All":
    df = df[df["Program Name"] == program_filter]

st.subheader('Sentiment trends over time')
sentiment_trend = df.groupby([df['Date'].dt.to_period('M'), 'Sentiment Label']).size().unstack().fillna(0)

months = ['June', 'July', 'August']
cols = {}
for i in sentiment_trend.columns:
    cols[f'{i}'] = trends[f'{i}']

x = np.arange(len(months))
width = 0.2
multiplier = 0


fig, ax = plt.subplots(layout='constrained')
for sentiment, count in cols.items():
    offset = width * multiplier
    rects = ax.bar(x + offset, count, width, label=sentiment)
    ax.bar_label(rects, padding=1)
    multiplier += 1
ax.set_title('Sentiment trends')
ax.set_xticks(x + width, months)
ax.set_ylabel('Count')
ax.legend();
st.pyplot(fig)
