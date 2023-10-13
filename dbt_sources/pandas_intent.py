
import pandas as pd

# Replace 'your_file.xlsx' with the path to your Excel file
excel_file = 'input.xlsx'

# Read the Excel file into a DataFrame
df = pd.read_excel(excel_file)

# Convert the DataFrame to a list of dictionaries
data_list = df.to_dict(orient='records')

# Now, 'data_list' contains your data from the Excel file as a list of dictionaries
print(data_list)
