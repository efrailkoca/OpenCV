import cv2 as cv
img = cv.imread("../1-photos/cats.jpg")
cv.imshow("cats", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

# simple thresholding;
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)		# 150 ne kadar fazla olursa beyazlık o kadar az olur.
cv.imshow("simple threshold", thresh)

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)		# beyaz ile siyahın yeri değişiyor.
cv.imshow("simple threshold inverse", thresh_inv)

# adaptive thresholding;
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow("adaptive thresholdind", adaptive_thresh)

adaptive_thresh_inv = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 11, 3)
cv.imshow("adaptive thresholdind inverse", adaptive_thresh_inv)


cv.waitKey(0)