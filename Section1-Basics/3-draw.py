import cv2 as cv
import numpy as np

'''
# Boş bir image oluşturmak;
blank = np.zeros((500,500), dtype="uint8")
cv.imshow("blank", blank)
'''


blank = np.zeros((500,500,3), dtype="uint8")		# belli renkte oluştururken 2 tane sayının yanına 3 yazılması lazım.
cv.imshow("blank", blank)

'''
# 1.belirli bir renkte oluşturmak için;
blank[:] = 0,255,0 				# yeşil
cv.imshow("green", blank)

blank[200:300, 300:400] = 0,0,255 				# kırmızı.		belirli pixel aralıklarında olması için ':' ile beraber aralıkları belirtmeliyiz.
cv.imshow("red", blank)
'''

# 2.dörtgen çizdirme;
# rectangle(img, point1, point2, color, thickness, lineType, shift, /)
cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness=2)
# (0,0) => originden başlatmak için. (250,250) => x,y eksenindeki uzunluklar. (0,255,0) => renk. thickness => çizginin kalınlığı.
# "thickness=cv.FILLED" == " thickness=-1" 		=> Bu şekilde yaparsak dörtgenin içini boyar.
# (250,250) => Bunun yerine -> (blank.shape[1]//2, blank.shape[0]//2) => bunu da kullanabiliriz. örneği "3.daire çizdirmede" mevcut.
cv.imshow("rectangle", blank)

# 3.daire çizdirme;
# circle(img, center, radius, color, thickness, lineType, shift, /)
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=-1)
cv.imshow("circle", blank)

# 4.çizgi çektirmek;
# line(img, point1, point2, color, thickness, lineType, shift, /)
cv.line(blank, (0,0), (250,250), (255,255,255), thickness=3)
cv.imshow("line", blank)

# 5.metin yazdırmak;
# putText(img, text, org, fontFace, fontScale, color, thickness, lineType, bottomLeftOrigin, /)
cv.putText(blank, "hello", (225,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)
cv.imshow("text", blank)
# (225,225) == org => metnin yazılacağı yer.

cv.waitKey(0)