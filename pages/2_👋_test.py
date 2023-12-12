
import streamlit as st
from df_global_search import DataFrameSearch
from get_reddit import get_reddit
from get_subreddit_date import get_subreddit_date

reddit=get_reddit()
df={}


import pprint

# assume you have a praw.Reddit instance bound to variable `reddit`
submission = reddit.submission("18fhrre")
st.write(submission.title)  # to make it non-lazy
a=pprint.pprint(vars(submission))
st.write(a)