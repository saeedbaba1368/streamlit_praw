def get_reddit():
    import os
    import praw
    from dotenv import load_dotenv, find_dotenv
    load_dotenv(find_dotenv(), override=True)
    client_secret = os.environ.get("client_secret")
    user_agent = os.environ.get("user_agent")
    client_id = os.environ.get("client_id")
    reddit = praw.Reddit(client_id=client_id,
                    client_secret=client_secret,	
                    user_agent=user_agent,
                        check_for_async=False,
                        ratelimit_seconds=5)
    print(user_agent)
    return reddit