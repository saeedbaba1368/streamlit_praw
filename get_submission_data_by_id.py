import pandas as pd
def get_submission_data_by_id(submission_id,reddit):
    # Initialize PRAW with a script-type authentication
    # Fetch the submission
    submission = reddit.submission(id=submission_id)

    # Scrape all available information about the submission
    submission_info = {
        'title': [submission.title],
        'score': [submission.score],
        'id': [submission.id],
        'url': [submission.url],
        'author': [str(submission.author)],
        'author_fullname': [submission.author_fullname],
        'num_comments': [submission.num_comments],
        'selftext': [submission.selftext],
        'created_utc': [submission.created_utc],
        'upvote_ratio': [submission.upvote_ratio],
        'subreddit': [str(submission.subreddit)],
        'link_flair_text': [submission.link_flair_text],
        'is_original_content': [submission.is_original_content],
        'over_18': [submission.over_18],
    }

    # Create a DataFrame for the submission
    df_submission = pd.DataFrame(submission_info)
    
    # Scrape all comments from the submission
    submission.comments.replace_more(limit=None)  # This line may take some time
    comments_data = []
    for comment in submission.comments.list():
        comments_data.append({
            'author': str(comment.author),
            'body': comment.body,
            'created_utc': comment.created_utc,
            'score': comment.score,
            'parent_id': comment.parent_id,
            'is_submitter': comment.is_submitter,
            'submission_id': submission_id,
        })

    # Create a DataFrame for the comments
    df_comments = pd.DataFrame(comments_data)

    return df_submission, df_comments
