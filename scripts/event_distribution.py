import json
from collections import Counter

with open("ml/tokenizer/vocab.json","r") as f:
    vocab = json.load(f)

reverse_vocab = {v:k for k,v in vocab.items()}

events = []

with open(
    "data/raw/BGL/BGL.log",
    "r",
    encoding="utf-8",
    errors="ignore"
) as f:

    for i,line in enumerate(f):

        if i % 5000 == 0:
            events.append(i)

        if i > 500000:
            break

print("Sampled positions:", len(events))