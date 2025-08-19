def engagement_ratio(likes, shares, comments, followers):
    """
    Calculate engagement ratio for a user/post.
    """
    total_engagement = likes + shares + comments
    return total_engagement / max(followers, 1)