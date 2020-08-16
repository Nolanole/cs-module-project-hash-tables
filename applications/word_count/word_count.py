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


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))