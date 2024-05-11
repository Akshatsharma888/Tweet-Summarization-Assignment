# Tweet-Summarization-Assignment
Flask app for tweet summarization. Utilizes Hugging Face transformers library. Includes alternative Twitter API integration. API limitations acknowledged.
# Tweet Summarization

## Description
This Flask application provides tweet summarization functionality. It leverages the Hugging Face transformers library to generate summaries. An alternative approach using the Twitter API is included, though limited by access restrictions.

## Installation
1. Clone this repository.
2. Install required dependencies using `pip install -r requirements.txt`.
3. Set up Twitter API credentials if opting for the alternative approach.
4. Run the Flask application using `python app.py`.

## Usage
- Access the application through a web browser at `http://localhost:5000`.
- Input tweet text for manual summarization or utilize the Twitter API integration for real-time summarization.

## How It Works
- Manual Summarization: Users input tweet text, and the application generates a summary using transformers.
- Twitter API Integration: Fetches tweets from Twitter Spaces and summarizes them using the same method.

## Dependencies
- Flask
- transformers
- tweepy (for alternative Twitter API integration)

## API Limitations
Due to access restrictions, the full potential of Twitter API integration is not realized. The provided alternative approach serves as a demonstration.

## Additional Information
- This project is developed as an assignment submission.
- Suggestions for enhancements include improved error handling and scalability.
