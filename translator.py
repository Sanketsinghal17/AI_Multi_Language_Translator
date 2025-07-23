import streamlit as st
from transformers import MarianMTModel, MarianTokenizer
import torch
import textwrap

# ✅ Cache models to avoid reloading for every translation
@st.cache_resource
def load_translation_model(model_name):
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)
    return model, tokenizer

# ✅ All supported language pairs and models
def get_model_name(src_lang, tgt_lang):
    language_pair = f"{src_lang}-{tgt_lang}"

    # ✅ Language-pair to model mapping
    model_mapping = {
    "en-hi": "Helsinki-NLP/opus-mt-en-hi",
    "hi-en": "Helsinki-NLP/opus-mt-hi-en",
    "en-bn": "shhossain/opus-mt-en-to-bn",
    "bn-en": "Helsinki-NLP/opus-mt-bn-en",
    "en-fr": "Helsinki-NLP/opus-mt-en-fr",
    "fr-en": "Helsinki-NLP/opus-mt-fr-en",
    "en-de": "Helsinki-NLP/opus-mt-en-de",
    "de-en": "Helsinki-NLP/opus-mt-de-en",
    "en-es": "Helsinki-NLP/opus-mt-en-es",
    "es-en": "Helsinki-NLP/opus-mt-es-en"
}


    return model_mapping.get(language_pair, None)

# ✅ Main translate function
def translate(text, src_lang='en', tgt_lang='hi'):
    model_name = get_model_name(src_lang, tgt_lang)

    if not model_name:
        return f"❌ Unsupported translation: '{src_lang}' → '{tgt_lang}'"

    try:
        model, tokenizer = load_translation_model(model_name)

        # ✅ Split long text into chunks under max token length
        wrapper = textwrap.TextWrapper(width=200)
        lines = wrapper.wrap(text)

        translated_result = []

        for line in lines:
            if not line.strip():
                continue
            inputs = tokenizer(line, return_tensors="pt", padding=True, truncation=True, max_length=512)
            with torch.no_grad():
                tokens = model.generate(**inputs)
            translated = tokenizer.decode(tokens[0], skip_special_tokens=True)
            translated_result.append(translated)

        return "\n".join(translated_result)

    except Exception as e:
        return f"❌ Translation failed: {str(e)}"
