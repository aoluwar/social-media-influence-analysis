from textblob import TextBlob

def analyze_sentiment(text):
    """
    Return sentiment polarity and subjectivity for the given text.
    """
    blob = TextBlob(text)
    return blob.polarity, blob.subjectivity