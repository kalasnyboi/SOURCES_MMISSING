import pandas as pd
import yaml

# Assuming your Excel file is named 'input.xlsx' and is in the same directory as this script
excel_file = 'input.xlsx'

# Read the Excel data into a DataFrame
df = pd.read_excel(excel_file)

# Convert the 'ZASTAW' column to uppercase
df['Field'] = df['Field'].str.upper()
df['Data Type'] = df['Data Type'].str.upper()
df['Length'] = df['Length']

 
# Convert the DataFrame to a list of dictionaries
config_data = df.to_dict(orient='records')

# Write the data to a YAML file
output_file = 'output.txt'

with open(output_file, 'w') as file:
    yaml.dump(config_data, file, default_flow_style=False)

print(f"Data has been written to '{output_file}'.")



output_dict = {
    "name": df['Field'],
    "data_type": df['Data Type']+f"{' (' + str(df['Length'] ) + ')' }"
}
print(output_dict)
