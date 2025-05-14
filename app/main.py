import pandas as pd
import random
from fastapi import FastAPI

app = FastAPI()
markov_chain = {}

def build_markov_chain(texts):
    chain = {}
    for text in texts:
        words = text.strip().split()
        for i in range(len(words) - 1):
            key = words[i]
            next_word = words[i + 1]
            if key not in chain:
                chain[key] = []
            chain[key].append(next_word)
    return chain

def generate_text(chain, length=100):
    if not chain:
        return ""
    word = "gang"
    output = ["the", "gang"]
    for _ in range(length - 1):
        next_words = chain.get(word)
        if not next_words:
            word = random.choice(list(chain.keys()))
        else:
            word = random.choice(next_words)
        output.append(word)
    return " ".join(output)

@app.on_event("startup")
def load_data():
    df = pd.read_csv("descriptions.csv")
    texts = df['Description'].dropna().tolist()
    global markov_chain
    markov_chain = build_markov_chain(texts)

@app.get("/generate/")
def get_generated_text(length: int = 100):
    return {"text": generate_text(markov_chain, length)}