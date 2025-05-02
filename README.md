## 🗣️ PDF to Audio Converter

Convert your PDF documents into high-quality audio using Text-to-Speech technology. This app extracts text from uploaded PDF files, converts it to speech using selectable system voices, and allows users to listen or download the audio file — all from a simple Streamlit web interface.

### 🚀 Features

* ✅ Upload PDF files directly
* ✅ Extract and clean text content
* ✅ Choose from **available system voices** (multi-language support)
* ✅ Select **speech rate** (Slow / Medium / Fast)
* ✅ Play generated audio inside the app
* ✅ Download as an `.mp3` audio file
* ✅ Friendly UI powered by Streamlit


### 📦 Requirements

* Python 3.7+
* The following Python packages:

```
streamlit
pyttsx3
pdfplumber
```

Install with:

```bash
pip install -r requirements.txt
```

---

### 🛠 How to Run

```bash
streamlit run pdf_to_audio_app.py
```

Then open the local URL provided by Streamlit (usually `http://localhost:8501`).

### 🧑‍💻 Usage Guide

1. Upload a PDF file via the uploader.
2. Choose:

   * **Voice** (from your system’s installed voices)
   * **Speech rate** (slow/medium/fast)

3. Click **"Convert to Audio"**.
4. 🎧 Listen to the generated audio directly in the app.
5. ⬇️ Download the `.mp3` file if you're satisfied.

### 🌐 Multi-Language Support

The app detects and lists available system voices including those for different languages. You can convert PDFs written in other languages using matching system voices (if installed).


### ❗ Troubleshooting

* **Male voice not working?** Some systems (especially macOS/Linux) have limited or no default male TTS voices. Consider installing additional voices or using a Windows system with SAPI support.
* **No text extracted?** The PDF may be scanned or image-based. This tool only works with **text-based PDFs**.


### 📦 Optional: Docker Support

*Coming Soon*: Containerize the app with Docker for easier deployment.
