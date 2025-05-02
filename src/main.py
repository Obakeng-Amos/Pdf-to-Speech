import os
import re
import streamlit as st
import argparse
import pdfplumber
import pyttsx3
import tempfile
from pathlib import Path

# ========== TTS Configuration ==========
def get_available_voices():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    return voices

def init_tts_engine_by_id(voice_id, rate_label):
    engine = pyttsx3.init()
    
    # Set rate
    rate_map = {'slow': 125, 'medium': 175, 'fast': 225}
    engine.setProperty('rate', rate_map.get(rate_label, 175))
    
    engine.setProperty('voice', voice_id)
    return engine

# ========== Text Extraction ==========
def extract_text_from_pdf(pdf_file):
    text = ""
    try:
        with pdfplumber.open(pdf_file) as pdf:
            total_pages = len(pdf.pages)
            for i, page in enumerate(pdf.pages):
                st.info(f"📄 Processing page {i+1} of {total_pages}...")
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
    except Exception as e:
        st.error(f"❌ Failed to extract text: {e}")
    return text

# ========== Text Cleaning ==========
def clean_text(text):
    return re.sub(r'\s+', ' ', text).strip()

# ========== Text to Audio ==========
def text_to_audio(text, output_path, voice_id, rate_label):
    try:
        engine = init_tts_engine_by_id(voice_id, rate_label)
        engine.save_to_file(text, output_path)
        engine.runAndWait()
        return True
    except Exception as e:
        st.error(f"❌ Failed to convert text to audio: {e}")
        return False

# ========== Streamlit UI ==========
def main():
    st.set_page_config(page_title="PDF to Audio Converter", layout="centered")
    st.title("📄🔊 PDF to Audio Converter")
    st.markdown("Upload a PDF and convert it into audio. Listen before you download!")

    uploaded_file = st.file_uploader("📤 Upload a PDF file", type="pdf")
    
    rate = st.selectbox("🎚️ Speech Rate", ['slow', 'medium', 'fast'])

    # Voice Selection
    voices = get_available_voices()
    voice_names = [f"{v.name} | {v.languages[0].decode('utf-8') if v.languages else 'Unknown'}" for v in voices]
    selected_voice = st.selectbox("🗣️ Choose Voice", voice_names)
    selected_voice_id = voices[voice_names.index(selected_voice)].id

    if uploaded_file:
        file_name = os.path.splitext(uploaded_file.name)[0]
        st.success(f"✅ Uploaded: {uploaded_file.name}")

        if st.button("🎧 Convert to Audio"):
            with st.spinner("🧠 Extracting text from PDF..."):
                text = extract_text_from_pdf(uploaded_file)

            if not text:
                st.error("No text extracted from the PDF.")
                return

            cleaned_text = clean_text(text)
            
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tf:
                audio_path = tf.name

            with st.spinner("🔊 Converting text to speech..."):
                success = text_to_audio(cleaned_text, audio_path, selected_voice_id, rate)

            if success:
                st.success("✅ Conversion complete!")
                st.audio(audio_path, format="audio/mp3")
                with open(audio_path, "rb") as audio_file:
                    st.download_button(
                        label="⬇️ Download Audio",
                        data=audio_file,
                        file_name=f"{file_name}.mp3",
                        mime="audio/mp3"
                    )
            else:
                st.error("❌ Conversion failed.")

if __name__ == "__main__":
    main()

