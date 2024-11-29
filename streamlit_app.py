import streamlit as st
import anthropic
client = anthropic.Client(api_key = unknown)
user_input = st.text_input("Ask me something")

response = client.completions.create(
    model = "claude-1",
    prompt = user_input,
    max_tokens_to_sample = 1000,
    temperature = 0.3
)
st.write(response["choices"][0]["text"])
