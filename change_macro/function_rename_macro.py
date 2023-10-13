import re

# Read input text from a file
input_file_path = "change_macro\input.sql"  # Replace with the path to your input file C:\Users\inigo.arriazu\Desktop\POLAND\SOURCES_MMISSING\change_macro\input.sql
output_file_path = "change_macro\output.sql"  # Replace with the desired output file path
replacement_string = "extra_de_patatas"



def change_code_macro(input_file_path,output_file_path,replacement_string ):
    try:
        with open(input_file_path, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"Input file not found: {input_file_path}")
        exit()
    except Exception as e:
        print(f"An error occurred while reading the input file: {e}")
        exit()

    # Use regular expressions to replace the text
    #updated_content = re.sub(r'ref\((.*?)\)', r'extra( ref(\1) )', content) 

    # Use regular expressions to replace the text
    pattern = r'ref\((.*?)\)'
    updated_content = re.sub(pattern, f'{replacement_string}( ref(\\1) )', content)


    # Write the updated content to the output file
    try:
        with open(output_file_path, 'w') as file:
            file.write(updated_content)
            print(f"Updated content has been written to {output_file_path}")
    except Exception as e:
        print(f"An error occurred while writing to the output file: {e}")



 

change_code_macro(input_file_path,output_file_path,replacement_string )

 