import cv2 as cv


def rescaleFrame(frame, scale=0.75):			# video nun yada photo'nun boyutunu değiştirmek için bir fonksiyon kurduk.

# bu fonksiyondaki metod images, videos, live videos için geçerli.

	width = int(frame.shape[1] * scale)
	height = int(frame.shape[0] * scale)

	dimensions = (width, height)

	return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


def changeRes(width, height):

# bu fonksiyondaki metod sadece live videos için geçerli.

	capture.set(3,width)
	capture.set(4,height)


img = cv.imread("../1-photos/cat.jpg")
cv.imshow("cat", img)

img_resized = rescaleFrame(img)
cv.imshow("cat resized", img_resized)

capture = cv.VideoCapture("../2-videos/dog.mp4")

while True:
	isTrue, frame = capture.read()
	cv.imshow("video", frame)

	frame_resized = rescaleFrame(frame)
	cv.imshow("video resized", frame_resized)



	if cv.waitKey(20) & 0xFF==ord("d"):
		break

capture.release()
cv.destroyAllWindows()

