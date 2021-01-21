import cv2
import numpy as np
import time

img = cv2.imread('test.JPG')

t1 = time.time()

img2 = cv2.resize(img , (int(1000), int(1000)))

img3 = cv2.rectangle(img2,(100,100),(150,150),(255,0,0))

img4 = cv2.flip(img3, 1)

gray = cv2.cvtColor(img4, cv2.COLOR_BGR2GRAY)

t2 = time.time()

cv2.imwrite('image2.jpg' , gray)

timeer = t2-t1
print('time')
print(timeer)