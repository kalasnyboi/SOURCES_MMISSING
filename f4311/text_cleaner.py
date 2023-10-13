import re

# Read text from an input file  C:\Users\inigo.arriazu\Desktop\POLAND\SOURCES_MMISSING\f4311\input.txt
input_file_path = "f4311\input.txt"  # Replace with the path to your input file
output_file_path = "f4311\output.txt"  # Replace with the desired output file path

try:
    with open(input_file_path, 'r') as file:
        text = file.read()
except FileNotFoundError:
    print(f"Input file not found: {input_file_path}")
    exit()
except Exception as e:
    print(f"An error occurred while reading the input file: {e}")
    exit()


# Define a regular expression pattern to extract "name" and "data_type"
pattern = r"- name: (\w+)\s+data_type: ([\w()]+)"

matches = re.findall(pattern, text)

# Create a new text with the extracted information
output_text = ""
for match in matches:
    name, data_type = match
    output_text += f"{name} {data_type}\n"

# Write the updated content to an output file
try:
    with open(output_file_path, 'w') as file:
        file.write(output_text)
        print(f"Updated content has been written to {output_file_path}")
except Exception as e:
    print(f"An error occurred while writing to the output file: {e}")