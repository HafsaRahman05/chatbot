# 💬 AI Chatbot (Streamlit + OpenAI GPT)

A simple and interactive AI chatbot built with **Streamlit** and **OpenAI GPT-3.5 API**.  
Users can chat in real-time with an AI assistant directly from a web interface.

---

## 🌐 Live Demo
👉 https://chatbot-es4tj6aqqbzzjkkvyjtte7.streamlit.app/

---

## 📌 Features

- 💬 Real-time AI chat interface
- 🤖 Powered by OpenAI GPT-3.5 Turbo
- 🧠 Maintains chat history in session
- 🔐 Secure API key input
- ⚡ Streaming responses (live typing effect)
- 🚨 Error handling (rate limit & authentication)
- 📱 Simple and clean UI using Streamlit

---

## 🛠️ Tech Stack

- Python 3
- Streamlit
- OpenAI API
- Chat Completions API

---

## 📂 Project Structure

```
chatbot/
│── streamlit_app.py      # Main Streamlit app
│── requirements.txt      # Dependencies
│── .gitignore
│── LICENSE
│── README.md
│── .devcontainer/
```

---

## 🚀 Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/HafsaRahman05/chatbot.git
cd chatbot
```

### 2️⃣ Create virtual environment (optional)
```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run the app
```bash
streamlit run streamlit_app.py
```

---

## 🔑 API Key Setup

To use this chatbot, you need an OpenAI API key:

👉 Get your API key: https://platform.openai.com/account/api-keys

Then enter it in the app when prompted.

---

## 💡 How It Works

1. User enters a message in chat input
2. Message is stored in session state
3. Entire conversation is sent to OpenAI API
4. GPT-3.5 generates response
5. Response is streamed back in real-time
6. Chat history is preserved during session

---

## ⚠️ Error Handling

The app handles:
- ❌ Invalid API key (AuthenticationError)
- ⚠️ Rate limit exceeded (RateLimitError)
- ❗ Unexpected API errors

---

## 🚀 Future Improvements

- 🔐 Add login authentication
- 🧠 Upgrade to GPT-4 / GPT-4o
- 💾 Save chat history in database
- 🎨 Improve UI with themes & avatars
- 🌐 Multi-language support
- 📱 Mobile responsive chat UI

---

## 👩‍💻 Author

**Hafsa Rahman**  
Software Engineering Student  
Passionate about AI, Data Science & Web Development

---

## ⭐ Acknowledgements

- OpenAI API for GPT models  
- Streamlit for amazing UI framework  

---
