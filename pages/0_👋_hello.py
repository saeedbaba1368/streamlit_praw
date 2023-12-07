client_secret="sCyU2xJ0AsGNfMKqZKorMfUyGJrUJg"
user_agent="Acceptable_Bill7915 "
client_id="I4EphV1-XBhKrTL8fIxf2Q"
import streamlit as st
import praw
import pandas as pd
import csv
from praw.models import MoreComments
reddit = praw.Reddit(client_id=client_id,		 # your client id
							client_secret=client_secret,	 # your client secret
							user_agent=user_agent,
              check_for_async=False,
              ratelimit_seconds=1)	 # your user agen
name = st.text_input('Enter your topic for reddit scraper')
button = st.button("click to start process")
if button:
    st.success(f'Welcome to the reddit scraper for , {name} topic!')
    subreddit = reddit.subreddit(name)
    posts_dict = {"Title": [], "Post Text": [],
          "ID": [], "Score": [],
          "Total Comments": [], "Post URL": []
          }
    for submission in subreddit.hot(limit=3):
      # Title of each post
      posts_dict["Title"].append(submission.title)

      # Text inside a post
      posts_dict["Post Text"].append(submission.selftext)

      # Unique ID of each post
      posts_dict["ID"].append(submission.id)

      # The score of a post
      posts_dict["Score"].append(submission.score)

      # Total number of comments inside the post
      posts_dict["Total Comments"].append(submission.num_comments)

      # URL of each post
      posts_dict["Post URL"].append(submission.url)
      
    df = pd.DataFrame(posts_dict) 

st.header('Filtered Dataframe')

# Add a multiselect widget to filter the dataframe
selected_titles = st.multiselect('Filter by Title', df['Title'].unique())

# Filter the dataframe
filtered_df = df[df['Title'].isin(selected_titles)]

# Display the filtered dataframe
st.dataframe(filtered_df)

