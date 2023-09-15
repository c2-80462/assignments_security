# 7)Write a function filter_long_words() that takes a list of words and an integer
# len and returns the list of words that are longer than len.

def filter_long_words(input_words):
    longer_words = []


    for word in input_words:
        if len(word) > length:
            longer_words.append(word)

    return longer_words

input_words = ['Hello', 'world', 'qwerty', 'hi', 'dancers']
length = 5

result = filter_long_words(input_words)
print(f"Words longer than {length} characters: {result}")

