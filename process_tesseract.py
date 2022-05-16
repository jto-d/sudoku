import cv2
from pytesseract import pytesseract

path = "j.png"

pytesseract.tesseract_cmd= r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img = cv2.imread(path)

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

print(pytesseract.image_to_string(img_rgb))