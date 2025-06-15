# 💬 Gemini Chatbot using Streamlit

A sleek and interactive chatbot interface built with **Streamlit** and powered by **Google Gemini** (Generative AI). This app allows users to have a conversational experience with Google's LLM, featuring real-time interaction and chat history.

---

## 🚀 Features

- 🤖 **Conversational Interface** with role-based chat bubbles  
- 🔐 **Secure API Key** loading from `.env` using `dotenv`  
- 🛡️ **Automatic Model Fallback & Error Handling**  
- 💾 **Session-based Chat History**  
- 💡 **Latency Feedback** to indicate model response speed  
- 🧹 **Clear Chat Button** in sidebar

---

## ⚙️ Technologies Used

- **Streamlit** – For building the web interface  
- **Google Generative AI SDK** – For accessing Gemini models  
- **Python (.env, time, os)** – For configuration and runtime control  
- **Gemini-1.5-flash-latest** – Default model used


---

## ✅ Functionality Summary

- 🔐 Loads Gemini API key securely via `.env`
- ⚡ Initializes `gemini-1.5-flash-latest` model
- 📊 Shows latency info in the sidebar
- 💾 Stores message history using `st.session_state`
- 👤 Provides assistant and user avatars
- ⌨️ Simulates typing effect for responses
- 🧹 Sidebar button to clear the chat history

---

## 💡 Future Enhancements

- 🌐 Add support for multiple Gemini models
- 🧠 Save chat history to a database
- 🗃️ Export chat transcripts to `.txt` or `.md`
- 📱 Deploy on **Streamlit Cloud**
- 🔒 Add login/authentication system
