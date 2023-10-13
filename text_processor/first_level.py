import re
import string


# Function to extract text between 'LOAD' and 'FROM' using regular expressions and split the results
def extract_and_split_to_text (file_path, pattern ):
    with open(file_path, 'r') as file:
        content = file.read()
        content = content.upper()       # we put all in uppercase
      
        content_procesed = content.strip() # removes the spaces at the beginning and end of the string.

    # Use a regular expression to find all matches
    matches = re.findall(pattern, content_procesed, re.DOTALL)
    
    # Split the matches further, for example, using a newline character
    split_results = [match.split('\n') for match in matches]
    
    return split_results




"""

    split_results = []
    # Iterate through the split results
    for match in matches:
        print(match)
        print("---")  # Add a separator between matches
  
        for line in match:
            match.split('\n')
            print(line)

            

def extract_store (file_path, file_store):

    result_all = extract_and_split_to_text(file_path)

    # The '\n' adds a newline character to the end of the text to start a new line.
    count = 0
    for result in result_all: 
        file_to_store = ( str(file_store) + str(count) +'.txt')

        with open(file_to_store, 'w') as file:
            my_string = '\n'.join(result)  # Use a space as a delimiter
            file.write( my_string )

        count = count + 1
            
"""
 







 