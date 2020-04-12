import datetime

def Post_format(posts):
    # Check if posts is list or not
    if isinstance(posts, list):
        new_posts = []
        for post in posts:
            dp = post["create_date"].split("-")
            df = datetime.datetime(int(dp[0]), int(dp[1]), int(dp[2]))
            post["create_date"] = df.strftime("%B %d, %Y")
            new_posts.append(post)
        return new_posts
    else:
        dp = posts["create_date"].split("-")
        df = datetime.datetime(int(dp[0]), int(dp[1]), int(dp[2]))
        posts["create_date"] = df.strftime("%B %d, %Y")
        return posts