import PyPDF2
from pdf2image import convert_from_path
from PIL import Image
import os

# Open the PDF file in read-binary mode
with open('example.pdf', 'rb') as pdf_file:
    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    
    # Create a directory to store the extracted images
    os.makedirs('extracted_images', exist_ok=True)
    
    # Loop through each page of the PDF
    for page_num in range(pdf_reader.getNumPages()):
        # Extract the page as an image
        images = convert_from_path('example.pdf', first_page=page_num+1, last_page=page_num+1)
        
        # Save each image
        for idx, image in enumerate(images):
            image_path = f'extracted_images/page{page_num + 1}_image{idx + 1}.png'
            image.save(image_path, 'PNG')
            print(f'Saved image: {image_path}')

print('Images saved to extracted_images directory.')
