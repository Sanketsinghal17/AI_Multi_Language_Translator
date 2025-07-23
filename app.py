import streamlit as st
from translator import translate, get_model_name
from language_detector import detect_language
from PIL import Image
from image_to_text import extract_text_from_image
from text_generator import generate_example_sentence
from voice_input import record_voice_input
from translator import get_model_name

# ✅ Language Mappings
language_name_to_code = {
    "English": "en",
    "Hindi": "hi",
    "Bengali": "bn",
    "French": "fr",
    "Spanish": "es",
    "German": "de"
}

language_code_to_name = {code: name for name, code in language_name_to_code.items()}

# ✅ Streamlit Page Config
st.set_page_config(page_title="AI Multi-Language Translator", layout="centered")
st.title("🌐 AI-Powered Multi-Language Translator")

# ✅ Sidebar Language Settings
st.sidebar.header("Select Language Settings")
auto_detect = st.sidebar.checkbox("Auto-detect source language", value=True)

target_lang_name = st.sidebar.selectbox("Translate to:", list(language_name_to_code.keys()))
target_lang_code = language_name_to_code[target_lang_name]

# ✅ Initialize session state for voice input
if "voice_text" not in st.session_state:
    st.session_state.voice_text = ""

# ✅ UI Tabs
tab1, tab2, tab3, tab4 = st.tabs(["📄 Text", "🎤 Voice", "🖼️ Image", "💬 Generate Example"])

# ⌨️ Tab 1: Text Translation
with tab1:
    st.subheader("Text Translation")

    input_text = st.text_area("Enter text to translate")

    if st.button("🔍 Detect Language"):
        lang_code = detect_language(input_text)
        lang_name = language_code_to_name.get(lang_code, lang_code)
        st.success(f"Detected Language: **{lang_name}**")

    if st.button("🔁 Translate Text"):
        if auto_detect:
            src_lang_code = detect_language(input_text)
        else:
            src_lang_name = st.selectbox("Select source language:", list(language_name_to_code.keys()))
            src_lang_code = language_name_to_code[src_lang_name]

        if get_model_name(src_lang_code, target_lang_code):
            result = translate(input_text, src_lang=src_lang_code, tgt_lang=target_lang_code)
            st.success(result)
        else:
            st.error("❌ This language pair is not supported.")
    

# 🎤 Tab 2: Voice Input + Translation
with tab2:
    st.subheader("🎙️ Voice Input")

    # Step 1: Record voice
    if st.button("🎧 Record Speech"):
        try:
            st.session_state.voice_text = record_voice_input()
            st.info(f"📝 Recognized Text: {st.session_state.voice_text}")
        except Exception as e:
            st.error(f"❌ Error during voice input: {e}")

    # Step 2: Show Copy Button (if any text recognized)
    if st.session_state.voice_text:
        st.markdown("### 📋 Copy Recognized Text")
        st.code(st.session_state.voice_text, language="text")  # Shows in a styled code box

        # Display the copy button using basic JavaScript clipboard call
        st.markdown(
            f"""
            <button onclick="navigator.clipboard.writeText(`{st.session_state.voice_text}`)"
                    style="margin-top: 10px; padding: 6px 12px; background-color: #008CBA; color: white; border: none; border-radius: 5px; cursor: pointer;">
                📋 Copy Text
            </button>
            """,
            unsafe_allow_html=True
        )


# 🖼️ Tab 3: Image Upload and Translate
with tab3:
    st.subheader("🖼️ Image Translation")

    image_file = st.file_uploader("Upload an image (with readable text)", type=["png", "jpg", "jpeg"])

    if image_file is not None:
        image = Image.open(image_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        extracted_text = extract_text_from_image(image_file)
        st.info(f"Extracted Text: {extracted_text}")

        if st.button("🔁 Translate Extracted Text"):
            src_lang_code = detect_language(extracted_text) if auto_detect else "en"
            if get_model_name(src_lang_code, target_lang_code):
                result = translate(extracted_text, src_lang=src_lang_code, tgt_lang=target_lang_code)
                st.success(result)
            else:
                st.error("❌ This language pair is not supported.")


# 💬 Tab 4: AI Sentence Generation
with tab4:
    st.subheader("💡 Generate Example Sentence")

    prompt = st.text_input("Enter a topic or phrase")

    if st.button("✨ Generate"):
        if not prompt.strip():
            st.warning("Please enter a valid topic.")
        else:
            try:
                sentence = generate_example_sentence(prompt)
                st.success("✅ Generated Sentence:")
                st.code(sentence, language="text")

                # 📋 Copy button (HTML + JS): displayed as a real button, not as text!
                st.markdown(
                    f"""
                    <button onclick="navigator.clipboard.writeText(`{sentence.replace('`', '\\`')}`)"
                            style="margin-top: 10px; padding: 6px 12px;
                                   background-color: #008CBA; color: white; border: none;
                                   border-radius: 5px; cursor: pointer;">
                        📋 Copy Text
                    </button>
                    """,
                    unsafe_allow_html=True
                )

            except Exception as e:
                st.error(f"❌ Generation failed: {e}")


