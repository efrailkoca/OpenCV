import cv2 as cv

img = cv.imread("../1-photos/park.jpg")
cv.imshow("park", img)

# 1-Converting to grayscale (gri tonlamaya dönüştürme);
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

# 2-Blur
blur = cv.GaussianBlur(img, (11,1), cv.BORDER_DEFAULT)
# (3,5) => ne kadar fazla blur olacağını ayarlamak için. 	1.sayı -> yataydaki blurlukla oynuyor.	 2.sayı -> dikeydeki blurlukla oynuyor.
# ayrıca blurluk derecesi tek sayı olmak zorunda.
cv.imshow("blur", blur)

# 3-Edge cascade (görüntüdeki nesnelerin kenarlarını çizdiriyor);
canny = cv.Canny(blur, 125, 175)
# blur => hangi görüntü üzerinde işlem yapılacağını beliten kısım.
cv.imshow("edge canny", canny)

# 4-Dilating the image (görüntüyü genişletme);
dilated = cv.dilate(canny, (99,92), iterations=3)		# görüntüdeki çizgileri kalınlaştırıyor.
cv.imshow("dilated", dilated)

# 5-Eroding (aşındırma);								# dilate 'in tersi.
eroded = cv.erode(dilated, (99,92), iterations=3)
cv.imshow("eroded", eroded)

# 6-Resize (yeniden boyutlandırma);
resized = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)	# interpolation 'un ne işe yaradığını anlamadım.
cv.imshow("resized", resized)

# 7-Cropping (kırpma);					görüntünün istediğimiz kısmını göstermek için.
cropped = img[50:200, 200:400]
cv.imshow("cropped", cropped)


cv.waitKey(0)