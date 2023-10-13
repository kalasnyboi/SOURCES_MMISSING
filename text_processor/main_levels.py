from first_level import extract_and_split_to_text
from second_level import trasform_level2






########## FIRST LEVEL ############
file_path_level1 = 'C://Users//inigo.arriazu//Desktop//ORIGEN//ExtractTransform//Adjustmens//QVD Level 1//F_AJ_LEDGER - copia.txt'  # Replace with the actual file path

## extraemos texto 
pattern_aux = 'LOAD'
pattern_aux2 = 'FROM'
pattern =  pattern_aux +  r'(.*?)' + pattern_aux2 # importante no traernos texto extra para el load delimitar inicio y fin 

text_in_file = extract_and_split_to_text(file_path_level1, pattern)  # Function to extract text between 'LOAD' and 'FROM' can be more than one element = list of list

## extraemos titulo
pattern_aux ='FROM '+ r'\['+'LIB:'
pattern_aux2 = '.QVD'
pattern =   pattern_aux +  r'(.*?)' + pattern_aux2  

titles_of_file = extract_and_split_to_text( file_path_level1 , pattern )  # Uppercase


## check the length of the list
if len(titles_of_file)  == len(text_in_file):
    print ('same length ')
else:
    print ('different length ')

print(text_in_file[1])



file_store_level1 = 'C://Users//inigo.arriazu//Desktop//POLAND//SOURCES_MMISSING//text_processor//first_level/'

####
file_path_level2 = 'C://Users//inigo.arriazu//Desktop//POLAND//SOURCES_MMISSING//text_processor//first_level//1.txt'
file_store_level2 = 'C://Users//inigo.arriazu//Desktop//POLAND//SOURCES_MMISSING//text_processor//second_level//1.txt'



trasform_level2 ( file_path_level2, file_store_level2)



### sources example dbt
file_path_sources_level1 = 'C://Users//inigo.arriazu//Desktop//POLAND//SOURCES_MMISSING//text_processor//sources_dbt//nombres.txt'  # Replace with the actual file path
file_store_sources_level1 = 'C://Users//inigo.arriazu//Desktop//POLAND//SOURCES_MMISSING//text_processor//sources_first_level/'

####
file_path_sources_level2 = 'C://Users//inigo.arriazu//Desktop//POLAND//SOURCES_MMISSING//text_processor//sources_first_level//0.txt'
file_store_sources_level2 = 'C://Users//inigo.arriazu//Desktop//POLAND//SOURCES_MMISSING//text_processor//sources_second_level//0.txt'

extract_store(file_path_sources_level1, file_store_sources_level1)
trasform_level2 ( file_path_sources_level2, file_store_sources_level2)






def contains_all_elements(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    
    return set2.issubset(set1)

# Example usage:
list1 = [1, 2, 3, 4, 5]
list2 = [5, 4, 3]
result = contains_all_elements(list1, list2)
print(result)  # Output will be True


# our case example 
with open(file_store_level2, 'r') as file:
    level_2 = file.read()

with open(file_store_sources_level2, 'r') as file:
    sources_level_2 = file.read()


print('########################## text ##########################')
print(level_2)
print('########################## Sources level 2 ##########################')
print(sources_level_2)
result = contains_all_elements(sources_level_2, level_2)
print(result)  # Output will be True
