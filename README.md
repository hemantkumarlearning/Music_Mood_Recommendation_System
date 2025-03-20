# Music Mood Recommendation System

This project is a music mood recommendation system that uses speech recognition, sentiment analysis, and the YouTube API to recommend videos based on the mood of the user's voice. The system analyzes the sentiment of the user's speech (e.g., happy, sad, relaxed) and fetches relevant YouTube videos in real time. It is integrated into a Streamlit app for user interaction.

## Table of Contents

- Features
  
- Installation
  
- Dependencies
  
- How to Use

## Features

- Speech Recognition: Captures the user's voice through a microphone.
- Sentiment Analysis: Analyzes the mood of the user's speech (happy, sad, relaxed) using TextBlob.
- YouTube Video Recommendations: Uses the YouTube Data API v3 to fetch videos based on the detected mood.
- Streamlit UI: An interactive web application built using Streamlit to provide a user-friendly interface.
  
## Installation

Follow these steps to set up and run the project:

#### 1 .Clone the repository:

```
git clone https://github.com/hemantkumarlearning/Music_Mood_Recommendation_System.git
cd Music_Mood_Recommendation_System
```

#### 2. Create a virtual environment (optional but recommended):

```
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

#### 3. Install the required dependencies:

```
pip install -r requirements.txt
```

## Dependencies

This project uses the following libraries:

- speechrecognition – For speech-to-text conversion.
- textblob – For sentiment analysis to determine the mood of the user.
- google-api-python-client – To interact with YouTube Data API v3.
- streamlit – For building the web interface.
- pyaudio – Required for capturing audio input (used by SpeechRecognition).
- requests – To make HTTP requests when fetching YouTube videos.
- google-auth – For authentication to interact with Google APIs.
  
## How to Use

#### 1. Set up YouTube API credentials:

Create a project on Google Cloud Console.

Enable the YouTube Data API v3.

Create an API key and save it in a file named config.py like this:

```
YOUTUBE_API_KEY = 'YOUR_YOUTUBE_API_KEY'
```

#### 2. Run the Streamlit app:

Once the dependencies are installed, run the Streamlit app:

```
streamlit run app.py
```

#### 3. Interact with the app:

- The app will prompt you to speak.
- It will process your speech to determine the sentiment (happy, sad, relaxed, etc.).
- Based on your mood, it will recommend a YouTube video and display it in the app.
