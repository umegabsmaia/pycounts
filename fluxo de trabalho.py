from string import punctuation
from collections import Counter

with open("zen.txt") as file:
        text = file.read()

text = text.lower()

for p in punctuation:
        text = text.replace(p, "")

words = text.split()

word_counts = Counter(words)
word_counts