import requests
import streamlit as st
import os
import speech_recognition as sr
from gtts import gTTS
import moviepy.editor as mp

def process_video(video_path):
    # Extract audio and perform Speech-to-Text
    transcription = transcribe_audio_locally(video_path)

    # Use GPT-4o for correction
    corrected_text = correct_transcription(transcription)

    # Use Text-to-Speech (Journey voice)
    new_audio_path = generate_speech(corrected_text)

    # Replace audio in the original video
    replace_audio_in_video(video_path, new_audio_path)

def transcribe_audio_locally(video_file):
    # Step 1: Extract audio from the video
    audio_output = "audio/audio.wav"
    video_clip = mp.VideoFileClip(video_file)
    video_clip.audio.write_audiofile(audio_output)

    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(audio_output) as source:
            audio_data = recognizer.record(source)
            # Step 2: Use Google Speech Recognition to transcribe the audio
            transcription = recognizer.recognize_google(audio_data)
            return transcription
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio.")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None

def correct_transcription(transcription):
    azure_openai_key = os.getenv("OPEN_AI") 
    azure_openai_endpoint = os.getenv("ENDPOINT")

    if azure_openai_key and azure_openai_endpoint:
        headers = {
            "Content-Type": "application/json",
            "api-key": azure_openai_key
        }

        data = {
            "messages": [{"role": "user", "content": f"Correct this text: {transcription}"}],
            "max_tokens": 500
        }

        response = requests.post(azure_openai_endpoint, headers=headers, json=data)
        
        if response.status_code == 200:
            result = response.json()
            corrected_text = result["choices"][0]["message"]["content"].strip()
            st.write("Corrected Transcription:")
            st.write(corrected_text)
            return corrected_text
        else:
            st.error(f"Error in GPT-4o API: {response.status_code}")
            return transcription
    else:
        st.warning("Missing API Key or Endpoint")
        return transcription

def generate_speech(text):
    # (locally using gTTS for now)
    tts = gTTS(text, lang='en')
    new_audio_path = "audio/new_audio.mp3"
    tts.save(new_audio_path)

    st.success("Generated new audio.")
    return new_audio_path

def replace_audio_in_video(video_path, new_audio_path):
    video = mp.VideoFileClip(video_path)
    new_audio = mp.AudioFileClip(new_audio_path)

    # Set the new audio to the video
    final_video_path = "video/final_video.mp4"
    final_video = video.set_audio(new_audio)
    final_video.write_videofile(final_video_path, codec="libx264", audio_codec="aac")

    st.success("Replaced audio in the video.")
    st.video(final_video_path)
