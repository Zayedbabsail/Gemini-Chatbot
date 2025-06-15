import streamlit as st
import google.generativeai as genai
import time
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get API key from .env
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    st.error("❌ Please set GOOGLE_API_KEY in your .env file")
    st.stop()

try:
    genai.configure(api_key=api_key)
except Exception as e:
    st.error(f"❌ API configuration failed: {str(e)}")
    st.stop()

# Initialize model with automatic fallback
def initialize_model():
    model_name = "gemini-1.5-flash-latest"  
    
    try:
        start_time = time.time()
        model = genai.GenerativeModel(model_name)
        # Quick test with timeout to fail fast if not working
        model.generate_content("Connection test", request_options={"timeout": 5})
        latency = time.time() - start_time
        
        st.sidebar.success(f"✅ Connected to {model_name} (Latency: {latency:.2f}s)")
        return model
        
    except Exception as e:
        st.sidebar.error(f"❌ Failed to connect to {model_name}: {str(e)}")
        return None

model = initialize_model()
if not model:
    st.error("🚨 Failed to connect to any Gemini model. Please check your API key or try again later.")
    st.stop()

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I'm your Gemini assistant. How can I help you today?"}
    ]

# Display chat messages
for message in st.session_state.messages:
    avatar = "🤖" if message["role"] == "assistant" else "👤"
    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])

# Function to get Gemini response
def get_gemini_response(prompt):
    try:
        # Start fresh chat but include history as context
        chat = model.start_chat(history=[])
        
        # Add all previous messages as context
        for msg in st.session_state.messages[:-1]:  # exclude the current prompt
            if msg["role"] == "user":
                chat.send_message(msg["content"])
            elif msg["role"] == "assistant":
                # For assistant messages, we need to manually add to history
                chat.history.append(
                    {
                        "role": "model",
                        "parts": [msg["content"]]
                    }
                )
        
        # Send the current prompt
        response = chat.send_message(prompt)
        return response.text
    except Exception as e:
        return f"❌ Error: {str(e)}"

# User input
if prompt := st.chat_input("Type your message..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user", avatar="👤"):
        st.markdown(prompt)
    
    # Display assistant response
    with st.chat_message("assistant", avatar="🤖"):
        message_placeholder = st.empty()
        full_response = ""
        
        # Get response
        response = get_gemini_response(prompt)
        
        # Simulate streaming
        for chunk in response.split():
            full_response += chunk + " "
            time.sleep(0.05)
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})

# Sidebar controls
with st.sidebar:
    st.header("Controls")
    if st.button("🧹 Clear Chat History"):
        st.session_state.messages = [
            {"role": "assistant", "content": "Hello! How can I help you today?"}
        ]
        st.rerun()
    
