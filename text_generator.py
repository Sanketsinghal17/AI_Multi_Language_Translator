import streamlit as st
from transformers import pipeline, set_seed

@st.cache_resource
def load_generator():
    generator = pipeline("text-generation", model="gpt2")
    set_seed(42)
    return generator

def generate_example_sentence(prompt):
    generator = load_generator()
    response = generator(prompt, max_length=50, num_return_sequences=1)
    return response[0]["generated_text"]
