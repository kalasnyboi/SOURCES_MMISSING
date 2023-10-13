import os
import glob

def find_txt_files(folder_path):
    txt_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".txt"):
                txt_files.append(os.path.join(root, file))
    return txt_files






# Function to concatenate and merge text files
def concatenate_files(input_directory, output_file):
    with open(output_file, 'w') as output:
        for root, _, files in os.walk(input_directory):
            for file_name in files:
                if file_name.endswith('.txt'):
                    file_path = os.path.join(root, file_name)
                    with open(file_path, 'r') as input_file:
                        output.write(input_file.read())


file = 'C://Users//inigo.arriazu//Desktop//ORIGEN\ExtractTransform\Adjustmens\QVD Level 1\F_AJ_LEDGER - copia.txt'

# Specify the input directory containing text files
input_directory = 'C://Users//inigo.arriazu//Desktop//ORIGEN//ExtractTransform_txt/'

# Specify the output file where the merged content will be saved
directory = 'C://Users//inigo.arriazu\Desktop\POLAND\SOURCES_MMISSING//text_processor//merge/'
name = 'merged.txt'
output_file = directory + name
# Call the function to concatenate and merge the files 
concatenate_files(input_directory, output_file)

print(f'Files in "{input_directory}" have been merged into "{output_file}".')


# deleted 
## CUSTOMER SERVICE 131 vs 134 
#//DATAFILES/ADJUSTMENTS_LVL1.QVW.LOG 97 vs 98
 