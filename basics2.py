import cv2
from imutils import paths
import numpy as np
'''
#reading images from images folder --- images folder contain subfolder containing images
imagepaths = list(paths.list_images("C:\\Users\\Asha Kalara\\Desktop\\Images") )

print(len(imagepaths))

for i in imagepaths:
    image=cv2.imread(i)
    cv2.imshow("image",image)
    cv2.waitKey()

cv2.destroyAllWindows()
'''


'''
image= cv2.imread("surya_munjal.png")
cv2.imshow("imaage",image)
cv2.waitKey()
cv2.destroyAllWindows()

'''
'''
#conversion of image to grayscale
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("gray",gray)
cv2.waitKey()
cv2.destroyAllWindows()

'''

'''
# conversion to HSV FORMAT ( hsv format is useful in masking task)

hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
cv2.imshow("hsv",hsv)
cv2.waitKey()
cv2.destroyAllWindows()

'''
'''
#Image Masking
#lets do masking of our video capture

low_green=np.array([25,52,72])
high_green=np.array([102,255,255])

low_red=np.array([0,100,20])
high_red=np.array([10,255,255])

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    cv2.imshow("frame", frame)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # cv2.imshow("hsv", hsv)
    mask=cv2.inRange(hsv,low_orange,high_orange)
    cv2.imshow("mask",mask)
    key = cv2.waitKey(1)  # specifies for how much time each frame should wait
    if key == ord("w"):
        break
cap.release()
cv2.destroyAllWindows()
'''

#drawing contours ( boundaries on object)

'''

low_red=np.array([0,100,20])
high_red=np.array([10,255,255])

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # cv2.imshow("hsv", hsv)
    mask = cv2.inRange(hsv,low_red,high_red)
    cv2.imshow("maskedframe", mask)

    contours,heirarchy =cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)


    cv2.drawContours(frame,contours,-1,(0,0,255),2)
    cv2.imshow("frame",frame)

    key = cv2.waitKey(1)  # specifies for how much time each frame should wait
    if key == ord("w"):
        break
cap.release()
cv2.destroyAllWindows()

'''

#noise removal

low_red=np.array([0,100,20])
high_red=np.array([10,255,255])

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # cv2.imshow("hsv", hsv)
    mask = cv2.inRange(hsv,low_red,high_red)
    cv2.imshow("maskedframe", mask)

    contours,heirarchy =cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    for c in contours:
        area = cv2.contourArea(c)
        if area > 4000:
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)  # drawing a rectangle
            cv2.drawContours(frame, c, -1, (0, 0, 255), 2)
            cv2.imshow("frame",frame)

    key = cv2.waitKey(1)  # specifies for how much time each frame should wait
    if key == ord("w"):
        break
cap.release()
cv2.destroyAllWindows()

