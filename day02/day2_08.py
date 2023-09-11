vowels = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]

char = input("Enter the character")


def check_vowels_consonant():
    for c in vowels:
        if char == c:
            print(f"{char} is a vowel")
            return
    print(f"{char} is a consonant")

check_vowels_consonant()