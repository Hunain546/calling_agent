import os
import json
import requests
import streamlit as st
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Default Configurations
default_voice = 'alloy'
default_greeting = (
    "Hello! I am your AI voice assistant. "
    "I am here to assist you with your queries and provide helpful information. "
    "How can I assist you today?"
)

default_instructions = (
    "You are an AI assistant designed to provide accurate and concise responses "
    "to user queries. Maintain a professional and polite tone, and ensure clarity "
    "and relevance in your answers. Always strive to assist the user effectively."
)

default_temperature = 0.8

# Backend URL (Replace this with your backend URL)
BACKEND_URL = "https://b039aecc-96bc-4ba3-8f7e-cfff0daf4f3c-00-1bxu3qd60wp5b.janeway.replit.dev/update-config"

# Streamlit Page Configurations
st.set_page_config(
    page_title="Twilio AI Agent Customizer",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Header
st.markdown(
    """
    <h1 style="text-align: center; color: #4CAF50; font-family: Arial;">
        📞 Calling AI Agent Customizer
    </h1>
    <p style="text-align: center; color: #888; font-family: Arial; font-size: 16px;">
        Easily customize your Twilio AI voice assistant. Set its voice, behavior, and greeting with an intuitive interface.
    </p>
    <hr style="border-top: 2px solid #eee;">
    """,
    unsafe_allow_html=True,
)

# Horizontal Layout using Columns
col1, col2, col3 = st.columns([1.5, 2, 1.5])

with col1:
    st.subheader("🎤 Voice Configuration")
    voice = st.selectbox(
        "Choose a voice",
        options=["alloy"],
        index=["alloy", "ash", "coral"].index(default_voice),
        help="Select the AI voice for your assistant.",
    )

with col2:
    st.subheader("💬 Greeting Message")
    greeting = st.text_area(
        "Enter a custom greeting message:",
        value=default_greeting,
        placeholder="Enter a greeting message for the AI assistant...",
        help="This is the first message the AI will say to the user.",
    )

with col3:
    st.subheader("📜 Behavioral Instructions")
    instructions = st.text_area(
        "Define the assistant's behavior and tone:",
        value=default_instructions,
        placeholder="Write detailed instructions for the assistant...",
        help="This sets the assistant's personality and behavior.",
    )

st.markdown(
    """
    <hr style="border-top: 2px solid #eee;">
    """,
    unsafe_allow_html=True,
)

# Save Button Styling and Logic
st.markdown(
    """
    <style>
        div.stButton > button {
            display: block;
            margin: 0 auto;
            font-size: 20px;
            padding: 10px 30px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        div.stButton > button:hover {
            background-color: #45a049;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

if st.button("💾 Save Settings"):
    config = {
        "voice": voice,
        "greeting": greeting,
        "instructions": instructions,
    }
    try:
        # Save configurations to a JSON file
        with open("config.json", "w") as f:
            json.dump(config, f, indent=4)
        st.success("✅ Settings saved!")

        # Send configurations to the backend
        response = requests.post(
            BACKEND_URL,
            json=config,
        )
        if response.status_code == 200:
            st.success("✅ Call your agent at +1 218 757 7870 to test the updated settings!")
            # st.json(response.json())
        else:
            st.error(f"❌ Backend returned an error! Status code: {response.status_code}")
            st.write(response.text)
    except Exception as e:
        st.error("❌ Failed to save settings or connect to the backend.")
        st.write(e)

st.markdown(
    """
    <hr style="border-top: 2px solid #eee;">
    """,
    unsafe_allow_html=True,
)

# Footer
st.markdown(
    """
    <div style="text-align: center; margin-top: 50px;">
        <p style="color: #888; font-family: Arial;">
            Customize the Calling Agent according to your preferences.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)
