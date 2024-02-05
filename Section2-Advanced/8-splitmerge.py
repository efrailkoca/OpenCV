import cv2 as cv
import numpy as np

img = cv.imread("../1-photos/park.jpg")
cv.imshow("park", img)

blank = np.zeros(img.shape[:2], dtype="uint8") 

b,g,r = cv.split(img)

blue = cv.merge([b, blank, blank])		# blue
green = cv.merge([blank, g, blank])		# green
red = cv.merge([blank, blank, r])		# red
cv.imshow("blue1", blue)
cv.imshow("green1", green)
cv.imshow("red1", red)

cv.imshow("blue", b)
cv.imshow("green", g)
cv.imshow("red", r)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged = cv.merge([b,g,r])
cv.imshow("merged image", merged)


cv.waitKey(0)