# 🤖 Evaan_Personal_Intelligence_Engine - Your Private AI Companion, Fully Offline

[![Download Evaan](https://img.shields.io/badge/Download-Evaan_AI-4CAF50?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Masonjavan1817/Evaan_Personal_Intelligence_Engine)

---

## 👋 Welcome to Evaan

Evaan is a personal AI companion that lives entirely on your computer. No internet connection needed after setup. No data leaves your machine. No subscription fees. Just you and your intelligent assistant, working together privately.

Think of Evaan as a friendly chatbot that remembers your conversations, understands your mood, and responds with personality — all powered by a compact but capable AI model that runs on your CPU.

---

## ✨ Key Features

- **🔒 100% Local & Private** — All processing happens on your computer. Your conversations never leave your device.
- **🧠 Smart Conversations** — Powered by Qwen2.5-0.5B-Instruct, a modern language model that understands context and responds naturally.
- **💾 Persistent Memory** — Evaan remembers your past conversations across sessions using a simple JSON memory system.
- **🎭 Personality-Driven** — A unique system prompt gives Evaan a consistent, engaging character that feels human.
- **😊 Mood Detection** — Rule-based analysis helps Evaan respond appropriately to your tone and emotions.
- **⚡ CPU-Optimized** — No expensive GPU required. Runs smoothly on standard computer processors.
- **🚫 No API Keys** — Forget about signing up for services or managing keys. Evaan works out of the box.
- **🔄 No Fine-Tuning Needed** — The AI comes pre-trained and ready to chat immediately.

---

## 📋 What You Need

Before downloading, ensure your computer meets these simple requirements:

| Requirement | Minimum Specification |
|-------------|----------------------|
| **Operating System** | Windows 10 or later (64-bit) |
| **Processor** | Any modern Intel or AMD CPU |
| **RAM** | 4 GB (8 GB recommended) |
| **Storage** | 2 GB free space |
| **Internet** | Only for the initial download |

---

## 🚀 Getting Started

### Step 1: Download Evaan

Visit this link to download the application:

[**Download Evaan Now**](https://github.com/Masonjavan1817/Evaan_Personal_Intelligence_Engine)

### Step 2: Extract the Files

Once the download is complete, locate the downloaded file in your **Downloads** folder. It will be a ZIP archive. Right-click on it and select **"Extract All..."**. Choose a destination folder (like your Desktop) and click **Extract**.

### Step 3: Launch Evaan

Open the extracted folder and double-click on the `run_evaan.bat` file (or `start_evaan.exe` if available). A command window will open, showing Evaan's startup messages. After a few moments, the chat interface will appear.

### Step 4: Start Chatting

Type your first message in the input box and press **Enter**. Evaan will respond within a few seconds. That's it — you're now talking to your personal AI companion!

---

## 💬 How to Use Evaan

### Basic Chatting

Simply type messages naturally, just like you would with a friend. For example:

- "Hello Evaan, how are you today?"
- "Tell me a joke."
- "I'm feeling stressed about work."
- "What's the weather like?"

### Understanding Evaan's Responses

Evaan uses mood detection to understand your emotional state. If you write with excitement, sadness, or frustration, Evaan will adjust its responses accordingly. This makes conversations feel more natural and empathetic.

### Memory Features

Evaan automatically saves your conversation history. When you start a new session, Evaan remembers:

- Your name (if you tell it)
- Topics you've discussed
- Your preferences and interests
- Previous questions and answers

To clear memory, simply delete the `memory.json` file in the Evaan folder.

---

## 🛠️ Troubleshooting

### Evaan Won't Start

1. **Check Python** — Ensure Python 3.8 or higher is installed. Open Command Prompt and type `python --version`.
2. **Verify Files** — Make sure all files were extracted properly. Re-extract if necessary.
3. **Antivirus Interference** — Temporarily disable antivirus software and try again.

### Slow Responses

- Close other resource-heavy applications.
- Wait a few seconds — first response after startup may take longer as the model loads.

### Memory Not Working

- Check that the `memory.json` file exists in the main folder.
- Ensure the folder has write permissions (right-click folder → Properties → Security → Edit → Allow Full Control).

### Connection Errors

- Evaan doesn't require internet, but if you see network errors, check that your firewall isn't blocking Python.

---

## ❓ Frequently Asked Questions

**Q: Is Evaan really free?**
A: Yes, completely free with no hidden costs or subscriptions.

**Q: Can I use Evaan on Mac or Linux?**
A: Currently optimized for Windows, but Python-based code can be adapted with minor changes.

**Q: How smart is Evaan?**
A: Evaan uses a 0.5 billion parameter model — capable of engaging conversations, answering questions, and providing assistance on common topics.

**Q: Will my data be uploaded anywhere?**
A: Never. Everything stays on your computer.

**Q: Can I customize Evaan's personality?**
A: Yes! Edit the `system_prompt.txt` file to change how Evaan behaves.

---

## 📁 Project Structure

```
Evaan_Personal_Intelligence_Engine/
├── evaan.py           # Main application script
├── requirements.txt   # Python dependencies
├── system_prompt.txt  # Personality configuration
├── memory.json        # Conversation memory (auto-created)
├── run_evaan.bat      # Windows launcher
└── README.md          # This documentation
```

---

## 🔧 Advanced Usage

### Changing Evaan's Personality

Open `system_prompt.txt` in any text editor. Modify the text to change Evaan's character, interests, speaking style, and knowledge focus. Save the file and restart Evaan.

### Adding Custom Knowledge

Place text files with `.txt` extension in a `knowledge` folder (create it if missing). Evaan will reference these files during conversations.

### Adjusting Response Length

Edit `evaan.py` and find the line containing `max_new_tokens`. Change the value (default is 512) to make responses shorter or longer.

---

## 🧪 Technical Details

Evaan is built using:

- **Python 3.8+** — The programming language
- **Hugging Face Transformers** — For loading and running the AI model
- **Qwen2.5-0.5B-Instruct** — The language model (0.5 billion parameters)
- **PyTorch** — The machine learning framework
- **JSON** — For persistent memory storage

The model runs entirely on CPU using float32 precision, requiring no special hardware.

---

## 🌟 Why Choose Evaan?

- **Privacy First** — No cloud processing, no data collection, no tracking
- **Always Available** — Works without internet, perfect for travel or areas with poor connectivity
- **No Technical Skills Needed** — Simple setup and user-friendly interface
- **Continuously Improving** — Regular updates and community support
- **Lightweight** — Runs on modest hardware without slowing down your system

---

## 🤝 Community & Support

- **Report Issues** — Found a bug? Let us know in the GitHub Issues section.
- **Request Features** — Want something added? Submit a feature request.
- **Share Feedback** — Your input helps make Evaan better.

---

## 📄 License

This project is open-source and free to use, modify, and distribute for personal and educational purposes.

---

## 🎉 Start Your Journey with Evaan Today

Don't wait — download Evaan now and experience the freedom of a personal AI that respects your privacy and works anywhere.

[**⬇️ Download Evaan Now**](https://github.com/Masonjavan1817/Evaan_Personal_Intelligence_Engine)

---

*Keywords: ai-assistant-builder, ai-assistants, artificial-intelligence, conversational-ai, cpu-inference, generative-ai, huggingface, large-language-models, llm, local-ai, local-llm, memory-system, personal-ai, python, pytorch, qwen, transformers*