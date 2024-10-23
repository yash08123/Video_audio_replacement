# AI-Powered Video Audio Replacement

## Overview

This project is a Proof of Concept (PoC) that replaces the audio of a video file with AI-generated speech. The process involves:

1. **Transcribing the audio** of the video using a local Speech-to-Text model.
2. **Correcting grammatical mistakes** in the transcription using the Azure OpenAI GPT-4o model.
3. **Generating a new AI-based audio** using Google's Text-to-Speech model with the Journey voice.
4. **Replacing the original audio** in the video with the AI-generated audio.

The app is built using **Streamlit** and is designed to run locally, providing a user-friendly interface for video processing.

## Features

- Transcribe audio from video files.
- Correct grammatical errors and remove filler words ("umms", "hmms", etc.).
- Generate AI audio using the corrected transcription.
- Sync and replace the original audio in the video with the AI-generated voice.
- Built with Python, Streamlit, and MoviePy for video/audio processing.

## Technologies Used

- **Python 3.12**
- **Streamlit** for the web interface.
- **MoviePy** for handling video and audio.
- **SpeechRecognition** for local speech-to-text transcription.
- **Azure OpenAI GPT-4o** for text correction.
- **Google Text-to-Speech** (gTTS) for generating AI audio.

## Folder Structure

```plaintext
video_audio_replacement/
│
├── audio/                    # Directory to store extracted and generated audio files
├── video/                     # Directory to store processed and final video files
├── main.py                   # Main Streamlit app
├── utils.py                  # Helper functions for video/audio processing
├── requirements.txt          # Python dependencies
├── .env                      # Environment variables (API keys and endpoints)
├── README.md                 # Project documentation
└── .gitignore                # Files and directories to ignore in version control
```

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/video_audio_replacement.git
cd video_audio_replacement
```
### 2. Create a Virtual Environment

```bash
python -m venv venv
```
### 3. Activate the Virtual Environment
Windows:
```bash
venv\Scripts\activate
```
macOS/Linux:
```bash
source venv/bin/activate
```
### 5. Install Dependencies
```bash
pip install -r requirements.txt
```
### 6. Set Up Environment Variables
Create a .env file in the root directory with the following content:

```bash
OPEN_AI=your_openai_api_key
ENDPOINT=https://your_openai_endpoint
```
Make sure to replace your_openai_api_key and your_openai_endpoint with actual values from your Azure OpenAI account.

### 6. Install FFmpeg
Windows: Download and install FFmpeg, and add it to your system PATH.
macOS:
```bash
brew install ffmpeg
```
Linux:
```bash
sudo apt install ffmpeg
```
### 7. Run the Streamlit App
```bash
streamlit run main.py
```
### 8. Process a Video
Upload a video file in the Streamlit app.
Click "Transcribe and Replace Audio".
The AI-generated audio will replace the original audio, and the final video can be downloaded.
