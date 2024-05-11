'''# If there were no limitations for access,i would have used Twitter API directly for 
    fetching tweets instead of using OpenAI.'''

from flask import Flask, request, jsonify, make_response
from openai import OpenAI, OpenAIError
import tweepy
import tweepy.errors

app = Flask(__name__)

# OpenAI API key
client = OpenAI(api_key="sk-proj-1N9lBvFhAPoe3uvW9NHnT3BlbkFJov9UFFm0rbHtxgLVah7W")

# Twitter API credentials
consumer_key = "y30iT7FKbK7qOPBq2Uaaj2NLL"
consumer_secret = "KHWOWgYYS43kI7vsTkMuf5N1XO1B8jZc5vBTn8UY9FY8opkqVl "
access_token = "1787384338562039808-1l9A2LIYL5VLPWggPjfoMuoS47rNWb"
access_token_secret = "SBUgRhxFrkAoTmpBKQpOHpR7YaTlURvQJ3DIF3DqkkarX"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def generate_summary(text, model="gpt-3.5-turbo", max_tokens=150):
    try:
        response = client.chat.completions.create(
          model="gpt-3.5-turbo",
          messages=[
                {"role": "system", "content": "can you please generate a more professional summary approx 100 words"},
                {"role": "user", "content": text}
            ],
        temperature=0.7,
        max_tokens=50,
        top_p=1
        )
        summary_text = response.choices[0].message.content
        return summary_text
    except OpenAIError as e:
        return str(e)

@app.route('/generate-content', methods=['POST'])
def generate_content():
    # Check if 'username' field is in the request form
    if 'username' not in request.form:
        return jsonify({"error": "Missing 'username' field in request data"}), 400

    # Get the username from the request
    username = request.form['username']

    try:
        # Fetch the most recent tweet from the user's timeline
        tweets = api.user_timeline(screen_name=username, count=1)
        tweet_text = tweets[0].text if tweets else ''
    except tweepy.TweepError as e:
        return jsonify({"error": str(e)}), 400

    # Summarize the tweet text
    if tweet_text:
        summary_text = generate_summary(tweet_text)
    else:
        summary_text = "The user has no tweets to summarize."

    # Return the generated summary as JSON response
    response_data = jsonify({"summary": summary_text})
    response = make_response(response_data)
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

if __name__ == '__main__':
    app.run(debug=True)