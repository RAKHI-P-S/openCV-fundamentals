import cv2


img =cv2.imread("img_2.png")
#img =cv2.imread("img_2.png",cv2.IMREAD_COLOR) # change colour during loading
resize=cv2.resize(img,None,fx=0.5,fy=0.5) #scale change one of the type of resizer
#resize=cv2.resize(img,(300,200)) #format for width and height
#gray=cv2.cvtColor(resize,cv2.COLOR_BGR2GRAY)
gray= cv2.cvtColor(img, cv2.COLOR_BGR2HSV)   # BGR → HSV
#cvt2 = cv2.cvtColor(resize, cv2.COLOR_BGR2LAB)   # BGR → HSV
cv2.rectangle(gray,(10,10),(150,150),(0,255,0),3) #cv2.rectangle(image, start_point, end_point, color, thickness)
cv2.circle(gray,(70,70),(50),(255,0,0),5)
cv2.line(gray,(0,0),(100,100),(0,0,255),5)
cv2.putText(gray,"its me RAKHI",(100,100),cv2.FONT_ITALIC,1,(0,255,0),1)

cv2.imshow("myfirstimage",gray)
cv2.waitKey(0)
cv2.destroyAllWindows()