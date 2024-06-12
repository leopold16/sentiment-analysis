from flask import Flask
import nltk

def create_app():
    app = Flask(__name__)

    # Ensure necessary NLTK data is downloaded
    nltk.download('vader_lexicon')

    from .routes import main
    app.register_blueprint(main)

    return app
