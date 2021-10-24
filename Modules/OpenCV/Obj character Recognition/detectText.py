# ejemplo de: https://medium.com/@MicroPyramid/extract-text-with-ocr-for-all-image-types-in-python-using-pytesseract-ec3c53e5fc3a

import Image
from tesseract import image_to_string

print image_to_string(Image.open('test.png'))
print image_to_string(Image.open('test-english.jpg'), lang='eng')