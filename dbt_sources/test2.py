import pandas as pd

# Replace 'your_file.xlsx' with the path to your Excel file
excel_file = 'input.xlsx'

# Read the Excel file into a DataFrame
df = pd.read_excel(excel_file)

# Convert the DataFrame to a list of dictionaries
data_list = df.to_dict(orient='records')

# Now, 'data_list' contains your data from the Excel file as a list of dictionaries
print(data_list)



# Input data as a tab-separated string
input_data = "ZASTAW\tCharacter\t1\t0"

# Split the input data into fields
fields = input_data.split("\t")

fields = data_list

# Extract the relevant information
name = fields[0]
data_type = fields[1]
length = int(fields[2]) if fields[2].isdigit() else None  # Convert length to an integer

# Create a dictionary with the extracted information
output_dict = {
    "name": name,
    "data_type": f"VARCHAR{' (' + str(length) + ')' if length else ''}"
}

# Print the output as YAML
print("- name:", output_dict["name"])
print("  data_type:", output_dict["data_type"])
