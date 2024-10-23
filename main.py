import streamlit as st
from utils import process_video

def main():
    st.title("AI-Generated Voice for Video")

    # Upload video file
    video_file = st.file_uploader("Upload a video file", type=["mp4", "mov"])
    
    if video_file is not None:
        # Save uploaded video
        video_path = "video/uploaded_video.mp4"
        with open(video_path, "wb") as f:
            f.write(video_file.getbuffer())
        
        st.video(video_file)

        if st.button("Transcribe and Replace Audio"):
            process_video(video_path)

if __name__ == "__main__":
    main()
