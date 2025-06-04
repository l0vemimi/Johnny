import requests
import json
import random
import os

from god_says import god_says

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATASET_PATH = os.path.join(SCRIPT_DIR, "terry_dataset.jsonl")

def ask_ollama(prompt, model='mistral'):
    url = 'http://localhost:11434/api/generate'
    payload = {
        "model": model,
        "prompt": f"You are Terry Davis the creator of templeOS.\n\nUser: {prompt}\nTerry:",
        "stream": True,
        "stop": ["User:", "Terry:"]
    }

    response = requests.post(url, json=payload, stream=True)
    
    print("\nTerry:", end=' ', flush=True)
    collected = ""
    for line in response.iter_lines():
        if line:
            try:
                data = json.loads(line.decode('utf-8'))
                chunk = data.get("response", "")
                print(chunk, end='', flush=True)
                collected += chunk
            except json.JSONDecodeError:
                pass
    return collected

def generate_terry_response(prompt):
    if "god" or "templeos" in prompt.lower():
        response = god_says()
        return response
def save_to_dataset(prompt, response):
    with open("terry_dataset.jsonl", "a") as f:
        entry = {"instruction": prompt, "response": response}
        f.write(json.dumps(entry) + "\n")

def main():
    quotes = [
    "God said the temple must be 640x480, 16 colors.",
    "I am not mentally ill. I had God talk to me, and that's different.",
    "It's not a bug, it's a message from God.",
    "I'm working on God's temple operating system. It has to be perfect.",
    "C is for communists. I use HolyC.",
    "Linux is cancer.",
    "God told me to write TempleOS. I do what I'm told.",
    "You're not supposed to masturbate.",
    "There is a divine intellect in the Bible. It is the word of God.",
    "TempleOS is a clean room, 100% me. No stolen code, no GNU bullshit.",
    "I am the high priest of TempleOS.",
    "It’s a sin to use more than 640x480. God said so.",
    "Look at the beauty of this code. It’s divine inspiration.",
    "I made my own compiler. How many people can say that?",
    "TempleOS has a command line. You type in prayers.",
    "I got a message from God in the random number generator.",
    "This is not schizophrenia. This is prophecy.",
    "God's voice comes through my speakers.",
    "I am building the third temple, and it runs at 60 FPS.",
    "The CIA hacked my brain, but I beat them with assembler.",
    ]

    print(random.choice(quotes))

    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        reply = ask_ollama(user_input)
        save_to_dataset(user_input, reply)

if __name__ == '__main__':
    main()
