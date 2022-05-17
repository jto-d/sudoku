import cv2
from imutils import contours
import numpy as np

path = "sudoku.png"

# load image with cv2 and adaptive threshold
img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
thresh = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 57,5)
# thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]


# isolate boxes
cnts = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]
for c in cnts:
    area = cv2.contourArea(c)
    if area < 1000:
        cv2.drawContours(thresh, [c], -1, (0,0,0), -1)

# straighten lines if not a perfect board
vertical_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1,5))
thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, vertical_kernel, iterations=9)
horizontal_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,1))
thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, horizontal_kernel, iterations=4)

# iterate through boxes
invert = 255 - thresh
cnts = cv2.findContours(invert, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]
(cnts, _) = contours.sort_contours(cnts, method="top-to-bottom")


board = []
row = []
for i, c in enumerate(cnts, 1):
    area = cv2.contourArea(c)
    if area < 50000:
        row.append(c)
    if i % 9 == 0:
        (cnts, _) = contours.sort_contours(cnts, method="left-to-right")
        board.append(cnts)
        row = []

for row in board:
    for square in row:
        mask = np.zeroes(img.shape, dtype=np.uint8) 
        cv2.drawContours(mask, [c], -1, (255,255,255), -1)
        result = cv2.bitwise_and(img, mask)
        result[mask==0] = 255
        cv2.imshow('result',result)
        cv2.waitKey(100)

cv2.imshow('thresh', thresh)
cv2.waitKey()








#possible area check
# area = cv2.contourArea(c)
# if area < 50000:


# mask = np.ones(img.shape[:2], dtype="uint8") * 255
# for c in cnts:
#     # get the bounding rect
#     x, y, w, h = cv2.boundingRect(c)
#     if w*h>1000:
#         cv2.rectangle(mask, (x, y), (x+w, y+h), (0, 0, 255), -1)

# res_final = cv2.bitwise_and(img, img, mask=cv2.bitwise_not(mask))

# cv2.imshow("boxes", mask)
# cv2.imshow("final image", res_final)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# cv2.imshow("Sudoku Puzzle", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
