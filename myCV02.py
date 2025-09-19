import cv2
import numpy as np


img=cv2.imread("img_1.png")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
gray_bgr=cv2.cvtColor(gray,cv2.COLOR_HSV2BGR)

resize01=cv2.resize(gray,(400,400))
resize02=cv2.resize(gray_bgr,(400,400))

combines=np.hstack((resize01,resize02))
combine=np.vstack((resize01,resize02))
cv2.line(combine, (50, 50), (450, 50), (0, 255, 0), 3)
cv2.circle(combines , (250, 250), 80, (0, 0, 255), -1)

cv2.imshow("myimage",combine)
cv2.imshow("image",combines)
cv2.waitKey(0)
cv2.destroyAllWindows()
