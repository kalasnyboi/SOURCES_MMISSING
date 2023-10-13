
import re

# Specify the file path
file_origen = 'C://Users//inigo.arriazu//Desktop//POLAND//SOURCES_MMISSING//text_processor//first_level//0.txt'
file_store = 'C://Users//inigo.arriazu//Desktop//POLAND//SOURCES_MMISSING//text_processor//second_level//0.txt'


###### main function
def trasform_level2 ( file_origen, file_store): 
    # Open the file in read mode
    with open(file_origen, 'r') as file:
        # Read the content of the file
        file_content = file.read()

    # Apply transformations to the text
    transformed_content = file_content.upper()  # Convert text to uppercase (you can apply your own transformations)

    ##filtered_lines = [line for line in transformed_content if "*TIMESTAMP*" not in line.upper()]  ## does not work 


    transformed_content = transformed_content.replace("]", "")
    transformed_content = transformed_content.replace("[", "")
    transformed_content = transformed_content.replace(",", "")
    transformed_content = transformed_content.replace("\t", " ")
    transformed_content = transformed_content.replace(" ", "")



    
    # SAVE the file 
    with open(file_store, 'w') as file:
        file.writelines(transformed_content)



trasform_level2 ( file_origen, file_store)