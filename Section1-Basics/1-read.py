import cv2 as cv

# reading photo ; 

'''
img = cv.imread("../1-photos/cat.jpg")		# fotoğrafı okumak için. fotoğrafın dosya yolunu yazıyoruz.

cv.imshow("Cat", img)						# fotoğrafı görüntülemek için. tırnak içi:figür ismi 

cv.waitKey(0)	
# sıfır girildiğinde kullanıcı bir tuşa basana kadar çalışır. eğer başka bir sayı girilirse girilen sayı milisaniye kadar bekler ve kapanır.
'''





# reading video ; 

# parantez içine 0,1,2 gibi integer konulup webcam'i referans alabilirdik. o kısmı tam anlamadım dakika(8.40). kayıtlı olan bir video için örnekteki gibi;
capture = cv.VideoCapture("../2-videos/dog.mp4")

while True:
	isTrue, frame = capture.read() 			# kare kare videoyu okur.
	cv.imshow("video", frame)

	if cv.waitKey(20) & 0xFF==ord("d"):
		break

capture.release()							# capture 'u serbest bırakıyoruz(release).
cv.destroyAllWindows()
# İhtiyacımız olmayan tüm açık pencereleri kapatır.