from nltk.sentiment.vader import SentimentIntensityAnalyzer

def analyze_sentiments(reviews):
    sia = SentimentIntensityAnalyzer()
    sentiments = {'positive': 0, 'neutral': 0, 'negative': 0}

    for review in reviews:
        score = sia.polarity_scores(review)
        if score['compound'] > 0.05:
            sentiments['positive'] += 1
        elif score['compound'] < -0.05:
            sentiments['negative'] += 1
        else:
            sentiments['neutral'] += 1

    return sentiments
