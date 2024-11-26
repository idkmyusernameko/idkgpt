import streamlit as st
import openai

# Replace with your API key
openai.api_key = your_api_key

st.title("idkgpt✨")
st.write("Ask me anything✨")

user_input = st.text_input("Your question:", "")

if user_input:
    with st.spinner("Thinking..."):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_input}]
        )
        answer = response.choices[0].message['content']
        st.write("**idkgpt:**", answer)
