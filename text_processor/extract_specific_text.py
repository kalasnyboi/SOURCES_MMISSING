import re
import string

# Function to extract text between 'LOAD' and 'FROM' using regular expressions and split the results
def extract_and_split_text_between_load_and_from(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        content = content.upper()       # we put all in uppercase
      
        content_procesed = content.strip() # removes the spaces at the beginning and end of the string.



    # Use a regular expression to find all matches
    pattern = r'LOAD(.*?)FROM'
    matches = re.findall(pattern, content_procesed, re.DOTALL)
    
    # Split the matches further, for example, using a newline character
    split_results = [match.split('\n') for match in matches]
    
    return split_results

# recibe una lista y modifica su contenido 
def clean_text(list_of_elements):
    cleaned_elements = []
    for content in list_of_elements:

        content = content.replace("]", "")
        content = content.replace("[", "")
        content = content.replace(",", "")
        content = content.replace("\t", " ")
        content = content.replace(" ", "")
        cleaned_elements.append(cleaned_elements)

    return cleaned_elements


 
def clean_text(list_of_elements):
    cleaned_elements = []
    for content in list_of_elements:
        # Remove spaces and special characters
        cleaned_content = content.replace("]", "").replace("[", "").replace(",", "").replace("\t", "").replace(" ", "")
        cleaned_elements.append(cleaned_content.strip())  # Removes spaces at the beginning and end of the string.
    return cleaned_elements









# Specify the path to your file
file_path = 'C://Users//inigo.arriazu//Desktop//ORIGEN\ExtractTransform\Adjustmens\QVD Level 1\F_AJ_LEDGER - copia.txt'  # Replace with the actual file path

# Extract and split the text between 'LOAD' and 'FROM' patterns
result = extract_and_split_text_between_load_and_from(file_path)


######### test de que entrega 
print("result") 
print(result) 
print("result") 


 

print("clean_list") 
print(clean_text(result)) 
print("clean_list") 


# Print the split results -- da una lista 
for matches in result:
    for match in matches:
        print(match.strip())