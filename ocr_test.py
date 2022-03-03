from importlib.resources import path
from PIL import Image

import pytesseract
import os

# If you don't have tesseract executable in your PATH, include the following:
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
# Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

# Simple image to string
#print(pytesseract.image_to_string(Image.open('Differenz_Schwellwertschalter.png')))

#for image in path:
    #print(pytesseract.image_to_string(Image.open('Differenz_Schwellwertschalter_'+str(i)+'.png')))

#Image.open('Differenz_Schwellwertschalter.png').crop((0, 0, 250, 100)).save('test.png')

path = 'C:/Users/leoch/Desktop/ocr_test'

for file in os.listdir(path):
    current_file = os.path.join(path, file)
    if(current_file.endswith('.jpg')):
        print(current_file)
        print(pytesseract.image_to_string(Image.open(current_file), lang='ssd_alphanum_plus+ssd+7seg+ssd_int+ssd_plus'))