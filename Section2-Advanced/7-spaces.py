import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("../1-photos/park.jpg")
cv.imshow("park", img)

# BGR to Grayscale;
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

# BGR to HSV;
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("hsv", hsv)

# BGR to LAB == BGR to l*a*b	LAB can also be represented like L*A*B;
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow("lab", lab)

# BGR to RGB;
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow("rgb", rgb)

# HSV to BGR;									# direkt olarak HSV 'den Grayscale'e dönüştüremeyiz. önce BGR'a sonra dönüştürmek istediğimiz formata.
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow("hsv to bgr", hsv_bgr)


# grafik olarak gösterme;
#plt.imshow(img)			# BGR ve RGB farklarından kaynaklı
#plt.show()				# matplotlib 'in default u rgb
						# OpenCV 'nin default u bgr

#plt.imshow(rgb)			# BGR ve RGB farklarından kaynaklı
#plt.show()


cv.waitKey(0)