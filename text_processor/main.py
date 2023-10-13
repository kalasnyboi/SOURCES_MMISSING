from get_all_txt_files import find_txt_files
from extract_specific_text import extract_and_split_text_between_load_and_from  ## hoja 2 

folder_path = "C://Users//inigo.arriazu//Desktop//ORIGEN"
txt_files = find_txt_files(folder_path)

for txt_file in txt_files:
    print(txt_file) 


####################################################################
### hoja 2 : texto de qlik
file_path = 'C://Users//inigo.arriazu//Desktop//ORIGEN\ExtractTransform\Adjustmens\QVD Level 1\F_AJ_LEDGER - copia.txt'  # Replace with the actual file path
result_qlik = extract_and_split_text_between_load_and_from(file_path)

# Print the split results -- da una lista 
for matches in result_qlik:
    for match in matches: 
        print(match.strip())
        result_qlik_txt= (match.strip())

 
print('result_qlik')
print(result_qlik)
print('result_qlik')
####################################################################

###  vamos a hacerlo al reves, vamos a extraer todos los archivos de carpeta de comparacion
folder_path = 'C://Users//inigo.arriazu//Desktop//test'
txt_files = find_txt_files(folder_path)

for txt_file in txt_files:
    print(txt_file) 

for txt_file in txt_files:
    result_dbt = extract_and_split_text_between_load_and_from(txt_file)

result_dbt2 = extract_and_split_text_between_load_and_from(txt_file)

# Print the split results -- da una lista 
for matches in result_dbt:
    for match in matches:
        print(match.strip())
####################################################################





def contains_all_elements(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    
    return set2.issubset(set1)

# Example usage:
list1 = matches
list2 = [5, 4, 3]
result = contains_all_elements(list1, list2)
print(result)  # Output will be True