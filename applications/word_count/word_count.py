def word_count(s):
    # Your code here
    cache = {}

    split_words = s.lower().split()

    ignored_chars = {
        '"': True,
        ':': True,
        ';': True,
        ',': True,
        '.': True,
        '-': True,
        '+': True,
        '=': True,
        '/': True,
        # "\": True,
        '|': True,
        '[': True,
        ']': True,
        '{': True,
        '}': True,
        '(': True,
        ')': True,
        '*': True,
        '^': True,
        '&': True,
            }

    for word in split_words:
        
        
        for letter in word:
            # print(letter, 'each letter')
            # build the string as you go
            
            if letter in ignored_chars:
                # word.replace(f"{letter}", '')
                continue
            else:
                x = "".join(letter)
        
        print(x)
        

        if word not in cache:
            cache[word] = 1
        else:
            cache[word] += 1

    # return cache


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))