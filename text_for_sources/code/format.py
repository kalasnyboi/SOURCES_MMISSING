import re

# Function to update the NUMBER pattern
def update_number(match):
    x, y = map(int, match.groups())
    new_x = x + y
    return f"NUMBER({new_x}, {y})"

# Open the input file for reading
input_file_path = "text_for_sources/code/example.txt"  # Replace with the path to your input file
try:
    with open(input_file_path, 'r') as input_file:
        content = input_file.read()
except FileNotFoundError:
    print(f"Input file not found: {input_file_path}")
    exit()
except Exception as e:
    print(f"An error occurred while reading the input file: {e}")
    exit()

# Define the regex pattern to match NUMBER(X, Y)
number_pattern = r"NUMBER\((\d+), (\d+)\)"

# Use re.sub to replace the matched patterns with the updated version
updated_content = re.sub(number_pattern, update_number, content)

# Write the updated content to an output file
output_file_path = "text_for_sources/code/output2.txt"

try:
    with open(output_file_path, 'w') as output_file:
        output_file.write(updated_content)
        print(f"Updated content has been written to {output_file_path}")
except Exception as e:
    print(f"An error occurred while writing to the output file: {e}")
