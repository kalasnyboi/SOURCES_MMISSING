import nltk
from nltk.corpus import words

# Download the NLTK words dataset (if not already downloaded)
nltk.download("words")

# Get the list of words in Spanish
spanish_words = words.words("es")

# Print a sample of Spanish words
for i in range(20):  # Print the first 20 words as an example
    print(spanish_words[i])
