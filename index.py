from PIL import Image
import pytesseract

# Open the image file
img = Image.open('your_scanned_image.png')

# Use pytesseract to do OCR on the image
text = pytesseract.image_to_string(img)

# Print the extracted text
print(text)

# Save the text to a Word document
with open('output.docx', 'w') as f:
    f.write(text)
