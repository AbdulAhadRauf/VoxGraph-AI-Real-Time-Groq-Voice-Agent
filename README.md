# 🎙️ GroqVoiceRT – Real-Time AI Voice Agent

An ultra-low latency, real-time AI Voice Agent built using **FastRTC** and **Groq LLM APIs**.

This project demonstrates how to build a real-time conversational voice assistant that supports live voice streaming, ultra-fast LLM inference, and tool-augmented AI (like a Math Agent) via both web and phone interfaces.

---

## 🧠 Project Overview

GroqVoiceRT is designed to explore real-time AI voice systems with minimal latency. It integrates:
* **FastRTC** for real-time streaming
* **Groq API** for high-speed inference
* **Custom Tool Agent (Math Agent)** for function calling
* Environment-based configuration
* Modular and extensible architecture

**Ideal Use Cases:**
* Voice AI experimentation
* Agentic workflows
* Tool-integrated LLM systems
* Real-time AI assistant development

---

## ⚙️ Tech Stack

* Python 3.10+
* FastRTC
* Groq API
* Async streaming

---

## 📂 Project Structure

```text
fastrtc-groq-voice-agent/
├── src/
│   ├── fastrtc_groq_voice_stream.py # Main real-time voice app
│   ├── process_groq_tts.py          # Groq TTS processing
│   ├── simple_math_agent.py         # Tool-enabled math agent
│   └── .env                         # Environment variables
├── .env.example
├── pyproject.toml
└── README.md
```

## 🔐 Setup Instructions
1. Clone the Repository
```bash
git clone https://github.com/AbdulAhadRauf/GroqVoiceRT.git

cd GroqVoiceRT
```
2. Create Virtual Environment (Using uv)
```bash
uv venv
source .venv/bin/activate
uv sync
```
3. Configure Environment Variables
Copy the example file
```bash
cp .env.example .env
Add your Groq API key
```
```code
GROQ_API_KEY=your_api_key_here
```
## ▶️ Running the Application
Navigate to the source directory:

```bash
cd src
```

```bash
python fastrtc_groq_voice_stream.py
```
#### Run with Phone Interface:
```bash
python fastrtc_groq_voice_stream.py --phone
```
## 🧮 Example Voice Commands
Try speaking the following phrases to test the math agent:

"What is 5 plus 7?"

"Multiply 12 and 4."

"Calculate 123 plus 456."

The agent will interpret your speech, call the math tool if required, generate a response using the Groq LLM, and stream audio output in real-time.

## 🚀 Future Improvements
Add RAG integration

- Multi-tool agent support
- Conversational memory
- Deployment via FastAPI


## 👨‍💻 Author
Abdul Ahad Rauf
AI/ML Engineer specializing in LLM Systems, RAG, Agentic AI, and Full-Stack Applications.

Education: MBA (AMU) | BS Data Science (IIT Madras)


## 📜 License
MIT License

## ⭐ If You Found This Useful: Give this repository a ⭐ and feel free to contribute!
