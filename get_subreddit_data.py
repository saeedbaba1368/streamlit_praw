import pandas as pd

def get_subreddit_data(attr, reddit, topic, limit,time_filter):
    subreddit = reddit.subreddit(topic)
    subreddit_dict = {
        "Title": [],
        "Post Text": [],
        "ID": [],
        "Score": [],
        "Total Comments": [],
        "Post URL": []
    }
    if attr == "top" or attr == "controversial" :
        submissions = getattr(subreddit, attr)(limit=int(limit),time_filter=time_filter)
    else:
        submissions = getattr(subreddit, attr)(limit=int(limit))
    for submission in submissions:
            subreddit_dict["Title"].append(submission.title)
            subreddit_dict["Post Text"].append(submission.selftext)
            subreddit_dict["ID"].append(submission.id)
            subreddit_dict["Score"].append(submission.score)
            subreddit_dict["Total Comments"].append(submission.num_comments)
            subreddit_dict["Post URL"].append(submission.url)

    return pd.DataFrame(subreddit_dict)
