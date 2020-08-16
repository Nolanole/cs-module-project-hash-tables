import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

word_dict = {}
word_list = words.split()

for i, word in enumerate(word_list):
    if i == len(word_list)-2:
        break
    if word in word_dict:
        word_dict[word].append(word_list[i+1])
    else:
        word_dict[word] = [word_list[i+1]]

# TODO: construct 5 random sentences
# Your code here

START_WORDS = []
STOP_CHARS = '.?!'
STOP_WORDS = []

for word in word_dict:
    if word[-1] in STOP_CHARS or (word[-1] == '"' and word[-2] in STOP_CHARS):
        STOP_WORDS.append(word)
    else:
        if word[0].isupper() or (word[0] == '"' and word[1].isupper()):
            START_WORDS.append(word)

sentences = []
for _ in range(5):
    sentence = ''
    start = random.choice(START_WORDS)
    sentence += start + ' '
    next_word = random.choice(word_dict[start])
    
    while next_word not in STOP_WORDS:
        sentence += next_word + ' '
        next_word = random.choice(word_dict[next_word])

    sentence += next_word
    sentences.append(sentence)
for sentence in sentences:
    print(sentence + '\n')