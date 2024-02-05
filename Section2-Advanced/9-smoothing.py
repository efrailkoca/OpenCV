import cv2 as cv

img = cv.imread("../1-photos/cats.jpg")
cv.imshow("cats", img)

# Averaging;
average = cv.blur(img, (7,7))
cv.imshow("average blur", average)

# Gaussian Blur;
gauss = cv.GaussianBlur(img, (7,7), 0)
cv.imshow("gaussian blur", gauss)

# Median Blur;
median = cv.medianBlur(img, 7)
cv.imshow("median blur", median)

# Bilateral;
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow("bilateral", bilateral) 

cv.waitKey(0)