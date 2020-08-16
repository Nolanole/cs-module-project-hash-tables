# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here
import sys
from collections import Counter

filename = sys.argv[1]

with open(filename) as f:
    cipher = f.read()

c = Counter(cipher)
for char in list(c.keys()):
    if not char.isalpha():
        del c[char]

counts = list(c.items())
counts.sort(key = lambda x: -x[1])

char_order = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']

cipher_map = {}
for i, tup in enumerate(counts):
    cipher_map[tup[0]] = char_order[i]

decoded = ''
for char in cipher:
    if char in cipher_map:
        decoded += cipher_map[char]
    else:
        decoded += char

print(decoded)