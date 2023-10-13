import os
from function_rename_macro import change_code_macro

def get_all_files_in_directory(directory):
    file_list = []
    for root, directories, files in os.walk(directory):
        for filename in files:
            file_list.append(os.path.join(root, filename))
    return file_list

# Specify the root directory to start the search
root_directory = "change_macro/Local-Poland"

file_list = get_all_files_in_directory(root_directory)

for file in file_list:
    print(file)



####################################################################
# Specify the root directory to start the search
####################################################################
def get_all_file_titles_in_directory(directory):
    file_titles = []
    for root, _, files in os.walk(directory):
        for filename in files:
            file_titles.append(filename)
    return file_titles

 

file_titles = get_all_file_titles_in_directory(root_directory)


# Read input text from a file
input_file_path = "change_macro/Local-Poland/"  # Replace with the path to your input file C:\Users\inigo.arriazu\Desktop\POLAND\SOURCES_MMISSING\change_macro\input.sql
output_file_path = "change_macro/local_pl_output/"  # Replace with the desired output file path
replacement_string = "remove_double_quotes_and_trim"




for title in file_titles:
    print(title)
    change_code_macro(input_file_path + title,output_file_path + title, replacement_string )
