def no_dups(s):
    # Your code here
    cache = {}

    split_words = s.split()
    new_sentence = []

    for word in split_words:
        if word not in cache:
            cache[word] = 1
            new_sentence.append(word)
        else:
            cache[word] += 1
    # join method works by the first thing before the join method
    # being what you want to be inbetween the items you want to join to be one
    # you then provide an iterable inside the join method and then work with that to produce
    # the result you want
    
    x = " ".join(new_sentence) 

    return x


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))