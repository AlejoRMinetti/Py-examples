import PyPDF2

# Open the PDF file
with open('C:/Users/Usuario/Desktop/Inoxidables modificaciones - cobalto y normas/ASTM A 276-04.pdf', 'rb') as file:
    # Create a PDF reader object
    reader = PyPDF2.PdfReader(file)
    # Iterate over each page
    for i in range(len(reader.pages)):
        # Extract the text from the page
        if i == 1:
            page = reader.pages[i]
            print(page.extract_text())
