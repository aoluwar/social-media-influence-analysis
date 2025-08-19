def compute_influence_score(row):
    """
    Compute an influence score based on engagement metrics.
    """
    score = row['likes'] + row['shares'] + row['comments']
    return score