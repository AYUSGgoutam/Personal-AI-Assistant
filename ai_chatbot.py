import os
import time
import streamlit as st
from groq import Groq, RateLimitError
from dotenv import load_dotenv

load_dotenv()


def render_chatbot():

    st.title("🤖 Ayush AI Assistant")
    st.caption("Powered by Groq AI")

    api_key = os.getenv("GROQ_API_KEY")
    model = os.getenv("GROQ_MODEL", "openai/gpt-oss-20b")

    if not api_key:
        st.error("Groq API key not found in .env")
        return

    client = Groq(
        api_key=api_key,
        max_retries=0,
        timeout=30.0
    )

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    if st.button("🗑️ Clear Chat"):
        st.session_state.chat_history = []
        st.rerun()

    for msg in st.session_state.chat_history:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    user_input = st.chat_input("Ask Ayush AI anything...")

    if user_input:

        st.session_state.chat_history.append({
            "role": "user",
            "content": user_input
        })

        with st.chat_message("user"):
            st.markdown(user_input)

        messages = [
            {
                "role": "system",
                "content": (
                    "You are Ayush AI Assistant. "
                    "Help with Python, SQL, AI/ML, job search, "
                    "interview preparation and professional emails. "
                    "Use simple Hinglish when appropriate. "
                    "Keep answers clear and concise."
                )
            }
        ]

        for msg in st.session_state.chat_history[-8:]:
            messages.append({
                "role": msg["role"],
                "content": msg["content"]
            })

        try:
            with st.chat_message("assistant"):

                with st.spinner("Ayush AI is thinking..."):

                    stream = client.chat.completions.create(
                        model=model,
                        messages=messages,
                        temperature=0.5,
                        max_tokens=700,
                        stream=True
                    )

                    answer = st.write_stream(
                        chunk.choices[0].delta.content
                        for chunk in stream
                        if chunk.choices and
                        chunk.choices[0].delta.content
                    )

            st.session_state.chat_history.append({
                "role": "assistant",
                "content": answer
            })

        except RateLimitError:
            st.warning(
                "Groq API limit reached. Please wait "
                "for your rate limit to reset."
            )

        except Exception as e:
            st.error(f"Groq API Error: {e}")

