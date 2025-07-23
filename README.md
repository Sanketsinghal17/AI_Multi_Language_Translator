Certainly, Sanket! Here’s a **corrected and polished `README.md`** for your project, formatted cleanly for GitHub, with all technical and styling issues fixed.

# 🌐 AI-Powered Multi-Language Translator

A user-friendly web application enabling seamless, context-aware translation across major languages. Features modern NLP (Hugging Face models), voice and image recognition, and an interactive Streamlit UI.

## 🚀 Features

- **Text translation** between English, Hindi, Bengali, French, German, and Spanish
- **Voice-to-text**: Speak and instantly transcribe language
- **Image OCR**: Extract and translate text from images
- **AI-powered example sentence generator**
- **Smart UI**: Copy buttons, auto language detection, and more

## 📦 Setup

1. **Clone the repo**
    ```bash
    git clone https://github.com/Sanketsinghal17/AI_Multi_Language_Translator.git
    cd AI_Multi_Language_Translator
    ```

2. **Create a virtual environment** (recommended)
    ```bash
    python -m venv venv
    # Windows:
    venv\Scripts\activate
    # Mac/Linux:
    source venv/bin/activate
    ```

3. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```
    > On Windows, if `pyaudio` fails to install:  
    > - Run `pip install pipwin`  
    > - Then `pipwin install pyaudio`

4. **Run the app**
    ```bash
    streamlit run app.py
    ```
    - Then open [http://localhost:8501](http://localhost:8501) in your browser.

## 🎯 Usage

- Select the **input method**: Text, Voice, or Image
- Choose your **target language** from the sidebar
- Use **copy** buttons to grab any translation or generated text

## ✨ Technologies Used

| Technology                 | Purpose                           |
|----------------------------|-----------------------------------|
| Streamlit                  | Web UI Framework                  |
| transformers (Hugging Face)| Translation/generation models     |
| torch                      | Machine learning backend          |
| pytesseract                | Image-to-text (OCR)               |
| Pillow                     | Image handling                    |
| langdetect                 | Auto language detection           |
| SpeechRecognition + PyAudio| Voice input                       |

## 🛠️ Project Structure

| File/Folder           | Purpose                             |
|-----------------------|-------------------------------------|
| `app.py`              | Main Streamlit app                  |
| `translator.py`       | Translation logic and models        |
| `language_detector.py`| Text language detection             |
| `text_generator.py`   | Example sentence generation         |
| `image_to_text.py`    | Image OCR logic                     |
| `voice_input.py`      | Microphone-to-text features         |
| `requirements.txt`    | Python dependencies                 |
| `assets/`             | Logo/image assets (optional)        |

## 🙋‍♂️ Contributing

Pull requests and feedback are welcome! Open an issue to discuss improvements.

## 💬 Contact

Project by **Sanket Singhal** for IBM GenAI Internship 2025  
✉️ Email: sanketsinghal6@gmail.com

