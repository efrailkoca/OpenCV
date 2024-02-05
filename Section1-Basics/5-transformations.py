import cv2 as cv
import numpy as np

img = cv.imread("../1-photos/park.jpg")
cv.imshow("park", img)

# 1-Translation	(taşımak için fonksiyon);
def translate(img, x, y):
	transMat = np.float32([[1,0,x], [0,1,y]])
	dimensions = (img.shape[1], img.shape[0])
	return cv.warpAffine(img, transMat, dimensions)

'''
-x => left 	,	x => right	,	-y => up	,	y => down
'''
translated = translate(img, 100, -100)
cv.imshow("translated", translated)

# 2-Rotation (döndürmek için fonksiyon);
# angle; -(eksi) => saat yönünün tersi, +(artı) => saat yönü
def rotate(img, angle, rotPoint=None):
	(height, width) = img.shape[:2]

	if rotPoint is None:
		rotPoint = (width//2, height//2)

	rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
	dimensions = (width, height)

	return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, 45)
cv.imshow("rotated", rotated)

rotated_rotated = rotate(rotated, 45)
cv.imshow("rotated rotated", rotated_rotated)

# 3-Resizing;
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow("resized", resized)

# 4-Flipping (ters çeivrme);
flip = cv.flip(img, 0)
# 0 = hem x hem y eksenine göre ters çevirme	1 = y eksenine göre ters çevirme 	-1 = x eksenine göre ter çevirme
cv.imshow("flip", flip)

# 5-Cropping (kırpma);
cropped = img[200:400, 300:400]
cv.imshow("cropped", cropped)



cv.waitKey(0)