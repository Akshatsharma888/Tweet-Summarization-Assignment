''' **Tweet Summarization App** '''

from flask import Flask, request, jsonify, make_response, render_template
from transformers import pipeline
from cachetools import cached, TTLCache
import os

# Disable symlinks warning
os.environ['HF_HUB_DISABLE_SYMLINKS_WARNING'] = '1'

# Initialize Flask application
app = Flask(__name__)

# Create a summarization pipeline
summarizer = pipeline("summarization", model="t5-base")

# Create a cache with a Time-To-Live (TTL) of 1 hour and a maximum of 1000 items
cache = TTLCache(maxsize=1000, ttl=3600)

@cached(cache)
def generate_summary(text):
    """
    Generate a summary for the given text using the summarization pipeline.
    
    Args:
        text (str): Input text to be summarized.
        
    Returns:
        str: Generated summary.
    """
    # Use the summarizer model to generate a summary
    summary = summarizer(text, max_length=100, min_length=30, do_sample=False)
    # Extract the generated summary from the result
    summary_text = summary[0]['summary_text']
    return summary_text

@app.route('/')
def index():
    """
    Render the index.html template for the home page.
    """
    return render_template('index.html')

@app.route('/upload-tweet', methods=['POST'])
def upload_tweet():
    """
    Receive a tweet from a POST request, summarize it, and return the summary as JSON response.
    """
    # Get the tweet from the request
    tweet = request.form['tweet']

    # Summarize the tweet
    summary_text = generate_summary(tweet)

    # Return the generated summary as JSON response
    response_data = jsonify({"summary": summary_text})
    response = make_response(response_data)
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

if __name__ == '__main__':
    # Run the Flask application in debug mode
    app.run(debug=True)
