import nltk
from nltk.corpus import words

# Download the NLTK words dataset (if not already downloaded)
nltk.download("words")


# Download the CESS_ESP corpus (if not already downloaded)
nltk.download('cess_esp')

# Access the Spanish words
spanish_words = nltk.corpus.cess_esp.words()

# Input list of letters
#input_letters = ['a', 'r', 'z', 'o', 'r']  ##  GETIRROS
#input_letters = ['g', 'e', 't', 'i', 'r', 'r', 'o', 's']  ##  GETIRROS
input_letters = ['g', 'l', 'o', 'd', 'u', 'n', 'i', 't']  ##  GLODUNIT


# Desired length of words
desired_length = len(input_letters)

# Get the list of English words
#english_words = words.words()

# Find words that contain all the input letters and have the desired length
matching_words = [word for word in spanish_words if len(word) == desired_length and all(letter in word for letter in input_letters)]

# Output the matching words
if matching_words:
    print("Matching words:", matching_words)
else:
    print("No matching words found.")
