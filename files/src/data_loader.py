import pandas as pd

def load_data(filepath):
    """
    Load the social media dataset from a CSV file.
    """
    return pd.read_csv(filepath)