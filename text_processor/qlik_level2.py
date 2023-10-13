from second_level import trasform_level2
import re
import os

# Specify the file path
 

file_origen = 'SOURCES_MMISSING/text_processor/qlik_extracts_level1/D_ITEM'
file_store = 'SOURCES_MMISSING/text_processor/qlik_extracts_level2/D_ITEM.txt'

import re

input_string = 'ISO3CODE AS [__ISO3CODE]'

# Use regular expression to extract the field name
match = re.search(r'(\w+)\s+AS\s+\[.*\]', input_string)

if match:
    field_name = match.group(1)
    print(field_name)
else:
    print("Pattern not found")


### 
def list_cleaning ( list_all_names):
    aux = []
    for input_string in list_all_names:
        #print(field)
        match = re.search(r'(\w+)\s+AS\s+\[.*\]', input_string)

        if match:
            field = match.group(1)
        else:
            field = input_string

        field = field.split('.')
        field = field[-1]

        field = field.replace("]", "")
        field = field.replace("[", "")
        field = field.replace(",", "")
        field = field.replace(" ", "")
        field = field.replace("'", "")

        field = field.replace("\"", "")
        field = field.replace("\t", "")

        # linea mas importante: quitar null 
        if field.strip():  # checks if the stripped string is non-empty. This condition filters out empty strings.
            aux.append(field.strip())
    
    return aux


def read_qlik_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        content = content.upper()  # Convert text to uppercase (you can apply your own transformations)

        field_names = content.split(',')

    return field_names


def contains_all_elements(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    
    return set2.issubset(set1)


"""
input
ISO3CODE AS [__ISO3CODE]

output
ISO3CODE

generate text 2 


for file_qlik_origen in file_qlik_list: 

    field_qlik_names = read_qlik_file((folder_qlik_path+ file_qlik_origen))
    field_qlik_names = list_cleaning ( field_qlik_names)
    print("########################")
    print(field_qlik_names)

    with open(file_path_store+file_qlik_origen, 'w') as file:
        for item in field_qlik_names:
            file.write(item + '\n')


"""

###### main function

folder_qlik_path = 'SOURCES_MMISSING/text_processor/qlik_extracts_level2/'
file_qlik_list = os.listdir(folder_qlik_path) # Use os.listdir() to get a list of all files in the directory


folder_dbt_path = 'SOURCES_MMISSING/text_processor/qlik_test_files/'
file_dbt_list = os.listdir(folder_dbt_path) # print(file_dbt_list[0])


# Specify the file path where you want to save the data
file_path_store =  'SOURCES_MMISSING/text_processor/qlik_extracts_level2/'





for file_qlik_origen in file_qlik_list: 

    field_qlik_names = read_qlik_file((folder_qlik_path+ file_qlik_origen))
    field_qlik_names = list_cleaning ( field_qlik_names)

    # leemos archivos DBT
    for file_dbt_origen in file_dbt_list: 

        field_dbt_names = read_qlik_file((folder_dbt_path+ file_dbt_origen))
        field_dbt_names = list_cleaning ( field_dbt_names)

        if contains_all_elements( field_qlik_names , field_dbt_names  ): # ( field_dbt_names, field_qlik_names ): ## checkea si el elemento 2 esta contenido en el 1 
            print((folder_qlik_path+ file_qlik_origen)+" , "+(file_dbt_origen+ file_dbt_origen)) 



"""
for file_qlik_origen in file_qlik_list: 

    field_qlik_names = read_qlik_file((folder_qlik_path+ file_qlik_origen))
    field_qlik_names = list_cleaning ( field_qlik_names)

    # leemos archivos DBT
    for file_dbt_origen in file_dbt_list: 

        field_dbt_names = read_qlik_file((folder_dbt_path+ file_dbt_origen))
        field_dbt_names = list_cleaning ( field_dbt_names)

        if contains_all_elements( field_dbt_names, field_qlik_names ): ## checkea si el elemento 2 esta contenido en el 1 
            print((folder_qlik_path+ file_qlik_origen)+" , "+(file_dbt_origen+ file_dbt_origen)) 


     
store list like this ['A', 'B', 'c']      
in a file with this format 

A
B
C

###################################
print(field_names)



print("#################################################")
dbt_names = read_qlik_file(folder_dbt_path+file_dbt_list[0])
dbt_names = list_cleaning ( dbt_names)

print("#################################################")
#print(field_names)
print(dbt_names)

file_origen = 'SOURCES_MMISSING/text_processor/qlik_test_files/D_ITEM_3'
 
file_path = file_origen 

dbt_names = read_qlik_file(file_path)
dbt_names = list_cleaning ( dbt_names)

print("#################################################")
print(field_names)
print(dbt_names)
# Example usage:
result = contains_all_elements(   dbt_names, field_names) ## checkea si el elemento 2 esta contenido en el 1 
print(result)  # Output will be True

"""
