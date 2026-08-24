## Code Description

**Evaan** is a fully local, CPU-based **conversational AI companion chatbot** built with **Python**, **PyTorch**, and Hugging Face **Transformers**, running on the **Qwen2.5-0.5B-Instruct** model. Unlike API-dependent chatbots, Evaan runs entirely on the user's own machine after a one-time model download, requiring no internet connection, no API key, and no external service for day-to-day conversation.

The project was built to explore how a small, efficient instruct-tuned language model can be wrapped with a persistent personality, mood system, and long-term memory to create a lightweight, always-available companion chatbot — without any model fine-tuning.

My contribution covers the **complete design and implementation** of the system — from the persona and tone-detection logic, to the mood-management system, to persistent JSON-based memory, to the CPU-optimized generation pipeline and the interactive terminal chat loop.

Unlike a simple prompt-response script, Evaan maintains **conversational state across sessions**: every exchange is saved to disk and reloaded on the next run, so the chatbot "remembers" recent conversation history between restarts.

The repository demonstrates how a base instruct model (no fine-tuning required) can be turned into a consistent, named AI persona using system-prompt engineering, rule-based tone detection, and structured memory management — all running on CPU-only hardware.

---

## System Workflow

The workflow begins the moment the script is run from the terminal. On startup, Evaan loads any previously saved conversation history and mood state from `evaan_memory.json`, then loads the **Qwen2.5-0.5B-Instruct** tokenizer and model weights into memory (downloading them automatically on first run, and using the local cache on every run after that).

Once ready, the user is dropped into an interactive chat loop. Every message the user types is first passed through a **tone-detection layer**, which scans for scolding language or apology language using regex pattern matching (supporting both English and Hindi/Hinglish phrases) to update Evaan's mood state.

Certain fixed questions — like "who are you" or "who created you" — are intercepted and answered directly with hardcoded identity responses, ensuring Evaan never invents an incorrect name or backstory. All other messages are appended to the conversation history and passed to the model, wrapped inside a **system prompt** that defines Evaan's persona, name rules, and behavior constraints.

The model generates a short, in-character reply using sampling-based generation (temperature and top-p controlled) with a repetition penalty to keep responses varied and natural. After each turn, the conversation history is automatically trimmed to the most recent turns and saved back to disk, so context length stays bounded and memory persists across sessions.

The user can also issue special commands — `/save`, `/clear`, `/history`, `/mood`, or `quit` / `exit` — to manage memory and session state directly from the terminal.

---

## Methods Implemented

This project combines prompt engineering, rule-based NLP, and local model inference to build a lightweight, persistent chatbot companion.

### Persona-Driven System Prompting

A fixed `BASE_PERSONA` system prompt defines Evaan's name, creator, and behavioral constraints (e.g., never inventing facts, never claiming to perform real computer actions), ensuring consistent identity across every generation call.

### Mood System

A mood-instruction dictionary (`MOOD_INSTRUCTIONS`) injects an additional personality layer into the system prompt, currently fixed to a **happy, warm, and playful** tone, with the underlying structure ready to support multiple moods.

### Rule-Based Tone Detection

Regex pattern lists detect **scolding** language (English and Hindi/Hinglish, e.g. "stupid", "bakwas", "gussa") and **apology** language (e.g. "sorry", "maaf", "galti") in user input, feeding into the mood-update logic.

### Persistent JSON Memory

Conversation history, mood state, and a recovery counter are serialized to `evaan_memory.json` after every turn, and safely reloaded (with error handling for missing or corrupted files) on the next run — giving Evaan continuity across sessions.

### Fixed Identity Guardrails

Common identity questions ("who are you", "who created you") are matched directly against normalized input and answered with hardcoded strings, bypassing the model entirely to guarantee accurate, consistent answers.

### CPU-Optimized Local Inference

The **Qwen2.5-0.5B-Instruct** model is loaded in `float32` with `low_cpu_mem_usage=True`, and generation is capped at 50 new tokens per turn with sampling parameters tuned for coherent, low-latency responses on CPU-only hardware.

### Bounded Context Window

Only the most recent `MAX_TURNS_IN_CONTEXT` (20) messages are sent to the model on each call, keeping inference fast and memory usage predictable as conversations grow.

---

## Key Features

* Fully **local, offline-capable** chatbot (internet needed only for first-time model download)
* Consistent **named persona** ("Evaan") enforced through system prompting and identity guardrails
* Rule-based **tone/mood detection** from user messages (English + Hindi/Hinglish)
* **Persistent memory** across sessions via `evaan_memory.json`
* Automatic **context trimming** to keep generation fast and bounded
* Interactive terminal commands: `/save`, `/clear`, `/history`, `/mood`
* Graceful handling of interrupts (`Ctrl+C`) with auto-save on exit
* No API key, no cloud dependency, no fine-tuning required
* Lightweight enough to run on a CPU-only laptop

---

## Project Workflow

<p align="center">
  <img src="https://img.shields.io/badge/1-Load%20Saved%20Memory-4CAF50?style=for-the-badge"/>
</p>

<p align="center">⬇️</p>

<p align="center">
  <img src="https://img.shields.io/badge/2-Load%20Tokenizer%20%26%20Model-2196F3?style=for-the-badge"/>
</p>

<p align="center">⬇️</p>

<p align="center">
  <img src="https://img.shields.io/badge/3-User%20Sends%20Message-FF9800?style=for-the-badge"/>
</p>

<p align="center">⬇️</p>

<p align="center">
  <img src="https://img.shields.io/badge/4-Tone%20Detection%20%26%20Mood%20Update-E91E63?style=for-the-badge"/>
</p>

<p align="center">⬇️</p>

<p align="center">
  <img src="https://img.shields.io/badge/5-Identity%20Guardrail%20Check-9C27B0?style=for-the-badge"/>
</p>

<p align="center">⬇️</p>

<p align="center">
  <img src="https://img.shields.io/badge/6-Build%20System%20Prompt-00BCD4?style=for-the-badge"/>
</p>

<p align="center">⬇️</p>

<p align="center">
  <img src="https://img.shields.io/badge/7-Generate%20Response%20(CPU)-795548?style=for-the-badge"/>
</p>

<p align="center">⬇️</p>

<p align="center">
  <img src="https://img.shields.io/badge/8-Trim%20Context%20History-607D8B?style=for-the-badge"/>
</p>

<p align="center">⬇️</p>

<p align="center">
  <img src="https://img.shields.io/badge/9-Auto%20Save%20Memory-3F51B5?style=for-the-badge"/>
</p>

---

## Technologies Used

<p align="center">
  <img src="https://skillicons.dev/icons?i=python" alt="Python"/>
  <img src="https://skillicons.dev/icons?i=pytorch" alt="PyTorch"/>
  <img src="https://skillicons.dev/icons?i=vscode" alt="VS Code"/>
  <img src="https://skillicons.dev/icons?i=git" alt="Git"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white"/>
  <img src="https://img.shields.io/badge/Transformers-FFD21E?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Qwen2.5--0.5B--Instruct-00A67E?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/JSON-000000?style=for-the-badge&logo=json&logoColor=white"/>
  <img src="https://img.shields.io/badge/CPU%20Only-4B5563?style=for-the-badge"/>
</p>

---

## Project Structure

```text
Evaan
│
├── evaan_chat.py                 # Main chatbot script (persona, mood, memory, chat loop)
├── evaan_chat_v3.code-workspace  # VS Code workspace configuration
└── evaan_memory.json             # Auto-generated persistent conversation memory
```

---

## Core Modules

The application is organized around a set of functional components inside `evaan_chat.py` that together define Evaan's identity, state, and behavior.

### Persona & Prompting

- `BASE_PERSONA`
- `MOOD_INSTRUCTIONS`
- `build_system_prompt()`

### Tone & Mood System

- `_SCOLD_PATTERNS`, `_APOLOGY_PATTERNS`
- `detect_tone()`
- `update_mood()`

### Memory Management

- `load_memory()`
- `save_memory()`
- `clear_memory()`

### Model & Generation

- Tokenizer and model loading (`Qwen2.5-0.5B-Instruct`)
- `generate_response()`

### Chat Interface

- `chat_with_evaan()` — main interactive terminal loop with `/save`, `/clear`, `/history`, `/mood`, and `quit`/`exit` commands

---

## Output

After successful setup and execution, the project provides:

* A fully functional **terminal-based chatbot** named Evaan, running locally on CPU.
* A **persistent memory file** (`evaan_memory.json`) that preserves conversation history and mood state between sessions.
* Consistent, **guardrailed identity responses** for common questions about who Evaan is and who created it.
* A **mood-aware conversational layer** that adapts based on detected user tone.
* An offline-capable chat experience after the initial one-time model download.

---

## Applications

The Evaan chatbot architecture can directly support several real-world and experimental use cases, including:

* Personal AI companion / assistant chatbots
* Offline, privacy-friendly conversational agents
* Lightweight CPU-only chatbot deployments
* Base for future multimodal companions (e.g., voice, video, or image generation front-ends)
* Prototyping persona-driven chatbots without fine-tuning
* Educational reference for prompt-engineered, memory-persistent LLM apps

---

## Acknowledgements

This project, **Evaan**, was designed and developed as a fully local, CPU-friendly conversational AI companion, built entirely by **Tahir**.

All persona design, mood logic, memory handling, and generation pipeline code were implemented using **Python**, **PyTorch**, and **Hugging Face Transformers** to deliver a lightweight, offline-capable chatbot.

---

## Conclusion

This project represents a **local, persona-driven conversational AI companion** built entirely on open-source tooling — from **rule-based tone detection**, through **persistent JSON memory**, to **CPU-optimized local inference** using the Qwen2.5-0.5B-Instruct model.

By combining prompt engineering, lightweight state management, and a bounded-context generation pipeline into a single reproducible Python script, Evaan provides a solid foundation for building further AI companion projects — including future integration with video, song, or voice generation APIs.
