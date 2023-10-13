from get_all_txt_files import find_txt_files
from first_level  import extract_and_split_to_text



def clear_list (input_list):
    #input_list = ['', '    [ANTONIO],', '    [JUAN] ', ' ']

    # Use a list comprehension to remove empty strings and strip whitespace from the remaining strings
    output_list = []  # [item.strip() for item in input_list if item.strip()]
    for item in input_list: 
        if item.strip():  # checks if the stripped string is non-empty. This condition filters out empty strings.
            output_list.append(item.strip())

    return (output_list)



def list_duplicates(original_list):
    # input : original_list = ['A', 'B', 'C', 'A', 'D', 'E', 'B']
    # output : ['A', 'B', 'C', 'A_2', 'D', 'E', 'B_2']
    # Create a new list to store the renamed elements
    new_list = []

    # Create a dictionary to keep track of counts
    count_dict = {}

    # Iterate through the original list
    for item in original_list:
        if item in count_dict:
            # If the item is a duplicate, increment its count and rename it
            count_dict[item] += 1
            new_item = f'{item}_{count_dict[item]}'
            new_list.append(new_item)
        else:
            # If the item is not a duplicate, add it as is to the new list
            count_dict[item] = 1
            new_list.append(item)

    return new_list



def store_file_with_name(titlex_auxiliar, lista_listas_contenido, directory): 
    # Open the file in write mode
    # Iterate through both lists and write the data to the file

    for title_list, text_list in zip(titlex_auxiliar, lista_listas_contenido):
        with open(directory + title_list, 'w') as title:
            title.write(f"{text_list}\n")




def get_title ( titles_list): 

    titlex_auxiliar = []
    for titles_list in titles_of_file:
        title_part = []
        for title in titles_list: 
            title = title.replace("]", "")
            title = title.replace("[", "")
            title = title.replace(",", "")
            title = title.replace("\t", " ")
            title = title.replace(" ", "")

            parts = title.split('/')
            title_part.append(parts[-1]) # cogemos la ultima posicion y quitamos corchetes
        titlex_auxiliar.append(title_part)
    
    return titlex_auxiliar



################################################################################################
############ MAIN ############
################################################################################################

folder_path = "C://Users//inigo.arriazu//Desktop//ORIGEN"
txt_files = find_txt_files(folder_path)



# ejemplo simple 
#file = 'C://Users//inigo.arriazu//Desktop//ORIGEN\ExtractTransform\Adjustmens\QVD Level 1\F_AJ_LEDGER - copia.txt'
# ejemplo merge 
file = 'C://Users//inigo.arriazu\Desktop\POLAND\SOURCES_MMISSING//text_processor//merge/merged.txt'
 


################################################################################################
## extraemos texto 
################################################################################################
pattern_aux = 'LOAD'
pattern_aux2 = 'FROM'
pattern =  pattern_aux +  r'(.*?)' + pattern_aux2 # importante no traernos texto extra para el load delimitar inicio y fin 

text_inside = extract_and_split_to_text(file , pattern )  # Uppercase

print ('\n The content is : ')
print (text_inside)


lista_listas_contenido = []

for text in text_inside:
    lista_listas_contenido.append(clear_list(text))



################################################################################################
## extraemos titulo
################################################################################################
pattern_aux ='FROM '+ r'\['+'LIB:'
pattern_aux2 = '.QVD'
pattern =   pattern_aux +  r'(.*?)' + pattern_aux2  

titles_of_file = extract_and_split_to_text(file , pattern )  # Uppercase


print ('\n The titles_of_file are : ')
for title in titles_of_file: 
    print (title)


# cogemos la ultima posicion y quitamos corchetes
titlex_auxiliar = get_title(titles_of_file)

# Using list comprehension to flatten the list
flat_list_titles = [item for sublist in titlex_auxiliar for item in sublist] # nested_list = [['F_AJ_LEDGER'], ['F_AJ_LEDGER']]  [item for sublist in nested_list for item in sublist] 
flat_list_titles = (list_duplicates(flat_list_titles))



################################################################################################
#### guardamos 
################################################################################################
directory = 'C://Users//inigo.arriazu\Desktop\POLAND\SOURCES_MMISSING//text_processor//qlik_extracts_level1/'
directory = 'text_processor//qlik_extracts_level1/'

if len(titles_of_file)  == len(text_inside):
    print ('works ')
    store_file_with_name (flat_list_titles, lista_listas_contenido, directory)

else: 
    print("################################")
    print("DIFFERENT LENGTH: ")
    print(len(titles_of_file))
    print(len(text_inside))
    print("################################")












