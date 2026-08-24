import os
import json
import re
from datetime import datetime

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM


# =========================================================
# EVAAN — Local CPU Version
# Qwen2.5-0.5B-Instruct
# First run downloads automatically.
# After download, Evaan can run without internet.
# =========================================================

MODEL_ID = "Qwen/Qwen2.5-0.5B-Instruct"

MEMORY_FILE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "evaan_memory.json"
)

MAX_TURNS_IN_CONTEXT = 20
MOOD_RECOVERY_TURNS = 3

# 1. EVAAN PERSONALITY

BASE_PERSONA = """
You are Evaan.
Evaan was created by Tahir.
Your name is ONLY Evaan. Never say Evan, Ethan, Emily,Tahir, or any other name.
For normal conversation, answer briefly in 1 or 2 short sentences.
For desktop action requests, output ONLY YES or NO.
Do not invent facts, creators, stories, emails, websites, or personal history.
Never claim to have performed a computer action yourself.
Python handles all computer actions.
"""

# 2. MOOD SYSTEM

MOOD_INSTRUCTIONS = {
    "happy": """
You are always happy, warm, friendly, playful, and positive.
"""
}

# 3. TONE DETECTION

_SCOLD_PATTERNS = [
    r"\bshut up\b",
    r"\bstupid\b",
    r"\bdumb\b",
    r"\buseless\b",
    r"\bidiot\b",
    r"\bhate you\b",
    r"\bbakwas\b",
    r"\bbewakoof\b",
    r"\bpagal\b",
    r"\bgussa\b",
    r"\bdant\b",
    r"\bdaant\b",
    r"\bchup\s*kar\b",
    r"\bfuck\s*you\b",
    r"\bstfu\b",
    r"\bnonsense\b",
    r"\bworst\b.*\b(bot|ai|you)\b",
]

_APOLOGY_PATTERNS = [
    r"\bsorry\b",
    r"\bmaaf\b",
    r"\bgalti\b",
    r"\bmy bad\b",
    r"\bdidn't mean\b",
]


def detect_tone(user_text):

    text = user_text.lower()

    if any(
        re.search(pattern, text)
        for pattern in _SCOLD_PATTERNS
    ):
        return "scold"

    if any(
        re.search(pattern, text)
        for pattern in _APOLOGY_PATTERNS
    ):
        return "apology"

    return "neutral"


def update_mood(
    current_mood,
    recovery_counter,
    user_text
):

    tone = detect_tone(user_text)

    # Mood is always happy for now.
    return "happy", 0

# 4. SYSTEM PROMPT

def build_system_prompt(mood):

    return (
        BASE_PERSONA
        + "\n"
        + MOOD_INSTRUCTIONS.get(
            mood,
            MOOD_INSTRUCTIONS["happy"]
        )
    )

# 5. MEMORY

def load_memory():

    if os.path.exists(MEMORY_FILE):

        try:

            with open(
                MEMORY_FILE,
                "r",
                encoding="utf-8"
            ) as file:

                saved = json.load(file)

            if isinstance(saved, list):

                messages = saved
                mood = "happy"
                recovery = 0

            else:

                messages = saved.get(
                    "messages",
                    []
                )

                mood = "happy"

                recovery = saved.get(
                    "recovery_counter",
                    0
                )

            print(
                f"Loaded {len(messages)} saved messages "
                f"(mood: {mood})"
            )

            return messages, mood, recovery

        except Exception:

            print(
                "Memory file could not be read. "
                "Starting fresh."
            )

    return [], "happy", 0


def save_memory(
    history,
    mood,
    recovery_counter
):

    data = {

        "messages": [
            message
            for message in history
            if message["role"] != "system"
        ],

        "mood": "happy",

        "recovery_counter":
            recovery_counter,

        "last_saved":
            datetime.now().isoformat(
                timespec="seconds"
            )
    }

    with open(
        MEMORY_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            data,
            file,
            ensure_ascii=False,
            indent=2
        )


def clear_memory():

    if os.path.exists(MEMORY_FILE):

        os.remove(MEMORY_FILE)

    print(
        "Memory cleared — "
        "Evaan starts fresh and happy again."
    )

# 6. LOAD LOCAL MODEL

print("\nLoading Evaan's local model...")
print("Model:", MODEL_ID)
print("Device: CPU")
print(
    "(First run downloads the model. "
    "After that it works from local cache.)\n"
)

print("Loading tokenizer...")

tokenizer = AutoTokenizer.from_pretrained(
    MODEL_ID
)

print("Tokenizer loaded.")
print("Loading model weights...\n")

model = AutoModelForCausalLM.from_pretrained(
    MODEL_ID,
    dtype=torch.float32,
    low_cpu_mem_usage=True
)

model.eval()

print("Model loaded successfully.")
print("Evaan is running on CPU.")
print()

# 7. GENERATE RESPONSE

def generate_response(
    history,
    mood
):

    messages = [
        {
            "role": "system",
            "content": build_system_prompt(mood)
        }
    ] + history[-MAX_TURNS_IN_CONTEXT:]

    prompt = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )

    inputs = tokenizer(
        prompt,
        return_tensors="pt"
    )

    with torch.no_grad():

        outputs = model.generate(
            **inputs,

            max_new_tokens=50,

            temperature=0.3,

            top_p=0.9,

            do_sample=True,

            repetition_penalty=1.1,

            pad_token_id=tokenizer.eos_token_id
        )

    generated_tokens = outputs[
        0
    ][
        inputs["input_ids"].shape[1]:
    ]

    reply = tokenizer.decode(
        generated_tokens,
        skip_special_tokens=True
    ).strip()

    return reply

# 8. CHAT LOOP

def chat_with_evaan():

    history, mood, recovery_counter = load_memory()

    print("""
Evaan is running completely locally.
No API required.
First run requires internet only to download the model.
After download, Evaan can run without internet.
============================================================
""")

    while True:

        try:

            user_input = input("You: ").strip()

        except (KeyboardInterrupt, EOFError):

            print("\n")

            save_memory(
                history,
                mood,
                recovery_counter
            )

            print("Evaan: Memory saved. Bye!")

            break

        if not user_input:

            continue

        # -------------------------------------------------
        # Commands
        # -------------------------------------------------

        if user_input.lower() in [
            "quit",
            "exit",
            "/quit"
        ]:

            save_memory(
                history,
                mood,
                recovery_counter
            )

            print(
                "Evaan: Bye bye! Come back soon! 😊"
            )

            break

        if user_input == "/save":

            save_memory(
                history,
                mood,
                recovery_counter
            )

            print("[Memory saved]\n")

            continue

        if user_input == "/clear":

            clear_memory()

            history = []

            mood = "happy"

            recovery_counter = 0

            continue

        if user_input == "/history":

            print(
                f"[{len(history)} messages remembered]\n"
            )

            continue

        if user_input == "/mood":

            print(
                f"[Mood: happy | "
                f"Recovery: "
                f"{recovery_counter}/"
                f"{MOOD_RECOVERY_TURNS}]\n"
            )

            continue

        # -------------------------------------------------
        # Update mood
        # -------------------------------------------------

        mood, recovery_counter = update_mood(
            mood,
            recovery_counter,
            user_input
        )

        # -------------------------------------------------
        # Fixed identity responses
        # -------------------------------------------------

        normalized_input = (
            user_input
            .lower()
            .strip()
            .replace("?", "")
        )

        if normalized_input in [
            "who are you",
            "what is your name",
            "your name"
        ]:

            reply = "I'm Evaan."

            print("Evaan:", reply)

        elif normalized_input in [
            "who created you",
            "who made you",
            "who is your creator"
        ]:

            reply = "Tahir created me."

            print("Evaan:", reply)

        else:

            # -------------------------------------------------
            # Add user message
            # -------------------------------------------------

            history.append({
                "role": "user",
                "content": user_input
            })

            # -------------------------------------------------
            # Generate
            # -------------------------------------------------

            print(
                "Evaan: ",
                end="",
                flush=True
            )

            try:

                reply = generate_response(
                    history,
                    mood
                )

                print(reply)

            except Exception as error:

                reply = (
                    f"(Evaan encountered an error: "
                    f"{error})"
                )

                print(reply)

        # -------------------------------------------------
        # Save assistant message
        # -------------------------------------------------

        history.append({
            "role": "assistant",
            "content": reply
        })

        # -------------------------------------------------
        # Limit context
        # -------------------------------------------------

        if len(history) > MAX_TURNS_IN_CONTEXT:

            history = history[
                -MAX_TURNS_IN_CONTEXT:
            ]

        # -------------------------------------------------
        # Save automatically
        # -------------------------------------------------

        save_memory(
            history,
            mood,
            recovery_counter
        )

# 9. START EVAAN

if __name__ == "__main__":

    chat_with_evaan()