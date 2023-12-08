client_secret="sCyU2xJ0AsGNfMKqZKorMfUyGJrUJg"
user_agent="Acceptable_Bill7915 "
client_id="I4EphV1-XBhKrTL8fIxf2Q"
import streamlit as st
import praw
import pandas as pd
import csv
import time
from praw.models import MoreComments
from df_global_search import DataFrameSearch

reddit = praw.Reddit(client_id=client_id,
	             client_secret=client_secret,	
	             user_agent=user_agent,
                     check_for_async=False,
                     ratelimit_seconds=1)
posts_dict = {"Title": [], "Post Text": [],
          "ID": [], "Score": [],
          "Total Comments": [], "Post URL": []}
df={}
def get_reddit_data(topic, limit):

	subreddit = reddit.subreddit(topic)
	for submission in subreddit.hot(limit=int(limit)):
		posts_dict["Title"].append(submission.title)
		posts_dict["Post Text"].append(submission.selftext)
		posts_dict["ID"].append(submission.id)
		posts_dict["Score"].append(submission.score)
		posts_dict["Total Comments"].append(submission.num_comments)
		posts_dict["Post URL"].append(submission.url)
	return pd.DataFrame(posts_dict)

col1, col2 = st.columns(2)
with col1:
    topic = st.text_input('Enter your topic for reddit scraper')
with col2:
    limit= st.number_input('Enter your limit number  for posts', min_value=0, max_value=100, value=4, step=1)
button = st.button("click to start process")

if button:
	st.success(f'Welcome to the reddit scraper for , {topic} topic!')
	

if topic :
    
	
	df = get_reddit_data(topic,limit)

    	
	search_bar_columns = st.columns((0.1, 1, 0.75, 0.75, 1))
	with search_bar_columns[1]:
		search_text = st.text_input(
				"Search", label_visibility="collapsed", placeholder="Search Text"
			)
	with search_bar_columns[2]:
			is_regex = st.toggle("Regex", value=False)
	with search_bar_columns[3]:
			case_sensitive = st.toggle("Case Sensitive", value=False)
	with search_bar_columns[4]:
			highlight_match = st.toggle("Highlight Matching Cells", value=True)

	with DataFrameSearch(
			dataframe=df,
			text_search=search_text,
			case_sensitive=case_sensitive,
			regex_search=is_regex,
			highlight_matches=highlight_match,
		) as df:
			st.dataframe(data=df, use_container_width=True, hide_index=True)
else:
    st.write("hello")
