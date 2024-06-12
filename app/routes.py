from flask import Blueprint, render_template, request
from app.utils.scraper import get_reviews
from app.utils.sentiment import analyze_sentiments

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/analyze', methods=['POST'])
def analyze():
    restaurant_name = request.form['restaurant_name']
    reviews = get_reviews(restaurant_name)
    sentiments = analyze_sentiments(reviews)
    return render_template('analysis.html', sentiments=sentiments, restaurant_name=restaurant_name)

