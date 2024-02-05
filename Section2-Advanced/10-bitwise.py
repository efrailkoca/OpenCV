import cv2 as cv
import numpy as np

blank = np.zeros((400,400), dtype="uint8")

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)

cv.imshow("rectangle", rectangle)
cv.imshow("circle", circle)

# bitwise AND;	=> iki image'in kesişimlerini gösterir.
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow("bitwise AND", bitwise_and)

# bitwise OR;	=> iki image'i birleştirir.
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow("bitwise OR", bitwise_or)

# bitwise XOR;	=> iki image'in kesişmeyen yerlerini gösterir.
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow("bitwise XOR", bitwise_xor)

# bitwise NOT;	=> image harici yerleri gösterir. iki image aynı anda kullanılamaz.
bitwise_not = cv.bitwise_not(rectangle)
cv.imshow("bitwise rectangle NOT", bitwise_not)

bitwise_not = cv.bitwise_not(circle)
cv.imshow("bitwise circle NOT", bitwise_not)


cv.waitKey(0)