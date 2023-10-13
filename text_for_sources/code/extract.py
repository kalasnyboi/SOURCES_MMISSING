# import re 

import re

# Open the file for reading
file_path = "text_for_sources/code/example.txt"  # Replace with the path to your file
try:
    with open(file_path, 'r') as file:
        # Read the entire content of the file
        content = file.read()
        print("File content:")
        print(content)
except FileNotFoundError:
    print(f"File not found: {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")





 

try:
    with open(file_path, 'r') as file:
        content = file.read()
        print("File content:")
        print(content)

        # Use regex to find NUMBER(6, 3) patterns
        number_pattern = r"NUMBER\(\d{1,3}, \d{1,3}\)"
        numbers = re.findall(number_pattern, content)

        if numbers:
            print("Found NUMBER(6, 3) patterns:")
            for number in numbers:
                print(number)
        else:
            print("No NUMBER(6, 3) patterns found in the file.")
except FileNotFoundError:
    print(f"File not found: {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")




 

# Write the content to an output file
output_file_path = "text_for_sources/code/output.txt"

try:
    with open(output_file_path, 'w') as output_file:
        output_file.write(content)
        print(f"Content has been written to {output_file_path}")
except Exception as e:
    print(f"An error occurred while writing to the output file: {e}")
