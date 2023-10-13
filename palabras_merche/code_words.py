"""
code with a imput of a list in the following example 

list = [a, r, z, o, z]

check all the words that exist wiht all that letters in spanish language 

output = [ arroz, zar  , ... ]


GETIRROS 

GLODUNIT

"""


# Spanish dictionary
spanish_words = ["arroz", "rozar", "zorra", "rosa", "zar"]

# Input list of letters
input_letters = ['a', 'r', 'z', 'o', 'z']

# Function to check if a word can be formed using all the input letters
def can_form_word_with_all_letters(word, letters):
    letter_count = {}
    for letter in letters:
        letter_count[letter] = letter_count.get(letter, 0) + 1
    for letter in word:
        if letter not in letter_count or letter_count[letter] == 0:
            return False
        letter_count[letter] -= 1
    return True

# Find words that can be formed with all input letters
valid_words = [word for word in spanish_words if can_form_word_with_all_letters(word, input_letters)]

# Output the valid words
if valid_words:
    print("Valid words:", valid_words)
else:
    print("No valid words can be formed with all the given letters.")
