import cv2

# face recognition
'''
face_classifier= cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

image=cv2.imread("surya_munjal.png")

#conversion of image to grayscale for easier process
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

faces=face_classifier.detectMultiScale(gray,1.2,7)   #returns  all faces in an array
print(type(faces))

print(len(faces))

print(faces)  #returns 4 cordinates

for (x,y,w,h) in faces:
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),2)
    cv2.imshow("detected",image)
    cv2.waitKey(0)

cv2.destroyAllWindows()
'''

#eyes detection

face_classifier= cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eye_classifier= cv2.CascadeClassifier("haarcascade_eye.xml")

image=cv2.imread("surya_munjal.png")

#conversion of image to grayscale for easier process
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

faces=face_classifier.detectMultiScale(gray,1.2,7)   #returns  all faces in an array
print(type(faces))

print(len(faces))

if len(faces) < 0:
   print("no faces available")

for (x,y,w,h) in faces:
    gray_image=gray[y:y+h,x:x+w]
    # cv2.imshow("gray_image",gray_image)
    color_image=image[y:y+h,x:x+w]
    eyes = eye_classifier.detectMultiScale(gray_image)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(color_image, (ex,ey), (ex + ew, ey + eh), (0, 0, 255), 2)
    cv2.imshow("detected eyes",image)

    cv2.waitKey()

cv2.destroyAllWindows()







