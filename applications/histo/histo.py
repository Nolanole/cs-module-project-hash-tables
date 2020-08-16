import sys

filename = sys.argv[1]

with open(filename) as f:
    words = f.read()

IGNORE_CHARS = '":;,.-+=/\|[]{}()*^&'

def word_count(s):
    word_counts = {}
    words = s.split()
    for word in words:
        cleaned_word = ''
        for char in word.lower():
            if char not in IGNORE_CHARS:
                cleaned_word += char
        if cleaned_word:
            if cleaned_word not in word_counts:
                word_counts[cleaned_word] = 1
            else:
                word_counts[cleaned_word] += 1
    return word_counts

word_counts = word_count(words)
longest_word = max([len(w) for w in word_counts])
word_counts = list(word_counts.items())
word_counts.sort(key=lambda x: (-x[1], x[0]))

for tup in word_counts:
    word = tup[0]
    spaces = ' ' * (longest_word - len(word) + 2)
    hashes = '#' * tup[1]
    print(word + spaces + hashes)