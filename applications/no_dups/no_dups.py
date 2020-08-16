def no_dups(s):
    word_set = set()
    new_s = ''
    for word in s.split():
        if word not in word_set:
            word_set.add(word)
            new_s += word + ' '    
    return new_s[:-1]


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))