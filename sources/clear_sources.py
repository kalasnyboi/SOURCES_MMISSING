
def filter_lines(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    filtered_lines = [line for line in lines if line.lstrip().startswith("FROM")]

    with open(output_file, 'w') as f:
        f.writelines(filtered_lines)

input_file = 'sources.txt'  
output_file = 'sources_output.txt'   

filter_lines(input_file, output_file)