# Write a function find_longest_word() that takes a list of words and returns
# the length of the longest one.

def find_longest_word(word_list):
    longest_length = len(word_list[0])
    for word in word_list:
        if len(word) > longest_length:
            longest_length = len(word)

    return longest_length


word_list = ["apple", "banana", "cherry", "date"]
longest_length = find_longest_word(word_list)
print("Length of the longest word:", longest_length)

