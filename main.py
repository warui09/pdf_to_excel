#!/usr/bin/python3
"""
Read data from a pdf file and write it to an excell spreadsheet
"""
import PyPDF2
import pandas as pd

# Open the PDF file in read-binary mode
with open('example.pdf', 'rb') as pdf_file:
    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    
    # Initialize variables to store the extracted data
    data = []

    # Loop through each page of the PDF
    for page_num in range(pdf_reader.getNumPages()):
        # Extract text from the current page
        page = pdf_reader.getPage(page_num)
        text = page.extractText()
        
        # Split the text into lines and append to the data list
        lines = text.split('\n')
        data.extend(lines)

# Create a DataFrame from the extracted data
df = pd.DataFrame({'Data': data})

# Save the DataFrame to an Excel file
excel_writer = pd.ExcelWriter('output.xlsx', engine='openpyxl')
df.to_excel(excel_writer, sheet_name='Sheet1', index=False)
excel_writer.save()

print('Data saved to Excel file: output.xlsx')
