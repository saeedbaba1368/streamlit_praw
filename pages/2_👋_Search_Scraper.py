import streamlit as st
import pandas as pd 
from get_reddit import get_reddit
# Reddit API credentials
reddit=get_reddit()

# Title and header  
st.title("Credit Subreddit Search")
subreddit_term = st.text_input("Enter subreddit term")
search_term = st.text_input("Enter search term")
limit= st.number_input('Result Nunmber', min_value=0, max_value=100, value=10, step=1)

results = []

if search_term and subreddit_term:
    subreddit = reddit.subreddit(subreddit_term)
    search_results = subreddit.search(search_term, limit=limit)
    
    for result in search_results:
        results.append([result.title, 
                       result.selftext,
                       result.score,
                       result.num_comments,
                       result.author,
                       result.url,
                       result.subreddit])

    df = pd.DataFrame(results, columns=["Title", "Snippet", "Score", "Num Comments", "Author","Url","Subreddit"])
    
    st.dataframe(df)