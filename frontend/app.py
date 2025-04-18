import streamlit as st
import requests

st.title("AI Travel Assistant 🌍")
question = st.text_input("Ask a travel question")

if st.button("Submit"):
    with st.spinner("Thinking..."):
        try:
            res = requests.post("http://localhost:9000/api/ask", json={"question": question})
            res.raise_for_status()  # Will raise an error for bad HTTP responses
            answer = res.json().get("answer", "No answer")
            st.markdown(answer)
        except requests.exceptions.RequestException as e:
            st.error(f"Error: {e}")
