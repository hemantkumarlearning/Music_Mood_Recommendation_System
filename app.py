import random
import googleapiclient.discovery
import googleapiclient.errors
import webbrowser
import speech_recognition as sr
from textblob import TextBlob
import streamlit as st
import streamlit.components.v1 as components

def get_youtube_service():
    api_service_name = "youtube"
    api_version = "v3"
    api_key = "AIzaSyD6Ba_OT5xlBvgL-RUiVHkdj6Ma0BNzicY" 

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=api_key)
    
    return youtube

def search_songs(mood,category):
    youtube = get_youtube_service()
    
    request = youtube.search().list(
        part="snippet",
        q=f"{mood} {category} songs", 
        type="video",
        maxResults=10
    )
    
    response = request.execute()

    video_urls = []
    for item in response['items']:
        video_url = f"https://www.youtube.com/watch?v={item['id']['videoId']}"
        video_urls.append(video_url)
    
    return video_urls

def play_random_song(mood, category):
    video_urls = search_songs(mood,category)
    
    if not video_urls:
        st.write("No songs found for the given mood.")
        return
    
    random_video = random.choice(video_urls)
    video_id = random_video.split('v=')[1]
    youtube_embed_url = f"https://www.youtube.com/embed/{video_id}?autoplay=1"

   
    components.iframe(youtube_embed_url, height=400)

st.title("Mood-Based Song Recommender")

st.write("""
    This app recommends songs based on your mood. You can speak your mood, and the app will suggest songs for you.
""")
category = st.sidebar.radio("Select Song Category", ['Indian', 'Hollywood', 'Bollywood', 'K-pop'])

if st.button('Start Listening'):
    recognizer = sr.Recognizer()

    with st.spinner("Listening for your mood..."):
        with sr.Microphone() as source:
            audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        st.write('you said this:',text)

        blob = TextBlob(text)
        sentiment = blob.sentiment.polarity

        if sentiment > 0:
            mood1 = 'joy'
        elif sentiment < 0:
                mood1 = 'sad'
        else:
            mood1 = 'relaxed'

        st.write(f"Detected mood: {mood1}")

        mood_to_genre = {
            "joy": ["pop", "dance", "rock"],
            "sad": ["classical", "indie", "acoustic"],
            "angry": ["metal", "hard rock", "punk"],
            "relaxed": ["chill", "ambient", "jazz"],
        }

        genre = mood_to_genre.get(mood1,[])
        mood = random.choice(genre)
        play_random_song(mood,category)

    except sr.UnknownValueError:
        st.write("Sorry, I couldn't understand.")
    except sr.RequestError:
        st.write("Speech service unavailable.")