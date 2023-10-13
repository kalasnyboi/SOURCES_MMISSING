import pandas as pd

# Specify the path to your Excel file
excel_file = 'input.xlsx'

# Read the Excel file into a DataFrame
df = pd.read_excel(excel_file)

# Access the columns using their names
column1 = df['Field'].str.upper()  # Replace 'Column1' with the actual name of your first column
column2 = df['Data Type'].str.upper() # Replace 'Column2' with the actual name of your second column
column3 = df['Length'] # Replace 'Column3' with the actual name of your third column
column4 = df['Decimals'] # Replace 'Column3' with the actual name of your third column

# You can also convert these columns to lists if needed
list1 = column1.tolist()
list2 = column2.tolist()
list3 = column3.tolist()
list4 = column4.tolist()
 
 
output_file = "output_sources.txt"

# Open the output file in write mode
with open(output_file, "w") as file:

    # Use the zip function to iterate through the lists simultaneously
    for item1, item2, item3, item4 in zip(list1, list2, list3, list4):

    # first numbers:
        if item2 == 'NUMERIC':
            file.write('        - name: ' + item1 +'\n')
            file.write('          data_type: NUMBER(' + str(item3) +', '+str(item4) +')\n')
        elif item2 == 'INTEGER':
            file.write('        - name: ' + item1 +'\n')
            file.write('          data_type: NUMBER(' + str(item3) +', '+str(item4) +')\n')

    # second strings : 
        elif item2 == 'CHARACTER':
                file.write('        - name: ' + item1 +'\n')
                file.write('          data_type: VARCHAR(' + str(item3) +')\n')


        elif item2 == 'STRING':
                file.write('        - name: ' + item1 +'\n')
                file.write('          data_type: VARCHAR(' + str(item3) +')' +'\n')

        elif item2 == 'VARIABLE STRING':
                file.write('        - name: ' + item1 +'\n')
                file.write('          data_type: VARCHAR(' + str(item3) +')' +'\n')

    # dates : 
        elif item2 == 'DATE':
                file.write('        - name: ' + item1 +'\n')
                file.write('          data_type:  VARCHAR (6)' +'\n')

        elif item2 == 'JDE UTIME':
                file.write('        - name: ' + item1 +'\n')
                file.write('          data_type: VARCHAR (11)' +'\n')
 