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
name = st.text_input('Enter your topic for reddit scraper')
button = st.button("click to start process")
if button:
	
	st.success(f'Welcome to the reddit scraper for , {name} topic!')
	subreddit = reddit.subreddit(name)
	
        
        posts_dict = {"Title": [], "Post Text": [],
          "ID": [], "Score": [],
          "Total Comments": [], "Post URL": []}
	for submission in subreddit.hot(limit=3):
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
		
      # Title of each post
      
	
    
      
    	df = pd.DataFrame(posts_dict) 
	
    	st.title('Reddit Posts Search Filter')

    # Search input
    	search_word = st.text_input('Enter a search word:')
	
	
    	button2 = st.button("click to filter")
    # Filter the dataframe if a search word is entered
    	if button2:
		mask = df.applymap(lambda x: search_word.lower() in str(x).lower()).any(axis=1)
		filtered_df = df[mask]
		st.write(mask)

    	else:
		filtered_df = df
		st.dataframe(filtered_df)
		

    
