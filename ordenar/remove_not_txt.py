import os

def remove_non_text_files(directory):
    for root, _, files in os.walk(directory, topdown=False):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            if not (file_name.endswith('.txt') or os.path.isdir(file_path)):
                os.remove(file_path)

# Specify the directory path where you want to remove non-text files

directory_to_clean = 'C://Users//inigo.arriazu//Desktop//ORIGEN//ExtractTransform_txt'

directory_to_clean = 'C://Users//inigo.arriazu//Desktop//POLAND\SOURCES_MMISSING//text_processor\qlik_test_files'



def remove_non_colum_text_files(directory):
    for root, _, files in os.walk(directory, topdown=False):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            if not (file_name.endswith('columnas.sql') or os.path.isdir(file_path)):
                os.remove(file_path)


# Call the function to remove non-text files
#remove_non_text_files(directory_to_clean)
remove_non_colum_text_files(directory_to_clean)
print(f'Non-text files in "{directory_to_clean}" have been removed.')
