import nltk

# Download the CESS_ESP corpus (if not already downloaded)
nltk.download('cess_esp')

# Access the Spanish words
spanish_words = nltk.corpus.cess_esp.words()

# Print a sample of Spanish words
for word in spanish_words[:20]:  # Print the first 20 words as an example
    print(word)


print( len(spanish_words))


