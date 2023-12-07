client_secret="sCyU2xJ0AsGNfMKqZKorMfUyGJrUJg"
user_agent="Acceptable_Bill7915 "
client_id="I4EphV1-XBhKrTL8fIxf2Q"
import streamlit as st
import praw
import pandas as pd
import csv
from praw.models import MoreComments
reddit = praw.Reddit(client_id=client_id,
	             client_secret=client_secret,	
	             user_agent=user_agent,
                     check_for_async=False,
                     ratelimit_seconds=1)
col1, col2 = st.columns(2)
with col1:
    name = st.text_input('Enter your topic for reddit scraper')
with col2:
    limit= st.text_input('Enter your limit number  for posts')	
button = st.button("click to start process")
if button:
	
	st.success(f'Welcome to the reddit scraper for , {name} topic!')
	subreddit = reddit.subreddit(name)
	posts_dict = {"Title": [], "Post Text": [],
          "ID": [], "Score": [],
          "Total Comments": [], "Post URL": []}
	
        
        
	for submission in subreddit.hot(limit=limit):
		posts_dict["Title"].append(submission.title)
		posts_dict["Post Text"].append(submission.selftext)
		posts_dict["ID"].append(submission.id)
		posts_dict["Score"].append(submission.score)
		posts_dict["Total Comments"].append(submission.num_comments)
		posts_dict["Post URL"].append(submission.url)
	df = pd.DataFrame(posts_dict) 
	st.title('Reddit Posts Search Filter')
	search_word = st.text_input('Enter a search word:')
	button2 = st.button("click to filter")
	if button2:
		mask = df.applymap(lambda x: search_word.lower() in str(x).lower()).any(axis=1)
		filtered_df = df[mask]
		pd.DataFrame(filtered_df)
	else:
		filtered_df = df
		pd.DataFrame(filtered_df)
		

    
