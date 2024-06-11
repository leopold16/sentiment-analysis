from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/analyze')
def analyze():
    # Placeholder sentiment analysis result
    sentiments = {'positive': 10, 'neutral': 5, 'negative': 3}
    return render_template('analysis.html', sentiments=sentiments)
