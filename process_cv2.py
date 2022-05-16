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

# # cv2.imshow("Sudoku Puzzle", img)
# # cv2.waitKey(0)
# # cv2.destroyAllWindows()