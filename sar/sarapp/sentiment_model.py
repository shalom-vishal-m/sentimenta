from textblob import TextBlob
# Create your models here
def analyze_sentiment(text):
    blob=TextBlob(text)
    return blob.sentiment.polarity
