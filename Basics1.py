
import cv2
import os
from datetime import datetime
# reading image
#image = cv2.imread("surya_munjal.png")

# displaying image
#cv2.imshow("Image Frame", image)
#cv2.waitKey()
#cv2.destroyAllWindows()


# check image shape
'''
print(type(image))
print(image.shape)
'''

# saving an image#
#cv2.imwrite("saveimage.jpg", image )

'''
#accessing webcam video or stored video in laptop or any other video through ip address(like mobile's)

cap = cv2.VideoCapture(0)
# 0 -- for laptop camera
#  video path for stored video
# ip address for mobile's camera

while True:
    ret,frame = cap.read()
    now = datetime.now()
    current_time=now.strftime("%d/%m/%y , %H:%M:%S")

    cv2.putText(frame, "Hi surya", (1,20), cv2.FONT_HERSHEY_TRIPLEX, 1, (0, 0, 255), 2)
    cv2.putText(frame,current_time,(1,50),cv2.FONT_HERSHEY_TRIPLEX,1,(0,0,255),2)

    cv2.imshow("frame", frame)

    #lets put text on the frame


    key=cv2.waitKey(1) # specifies for how much time each frame should wait
    if key == ord("w"):
        break
cap.release()
cv2.destroyAllWindows()

'''
# creating your own data set using your camera
def save_frame_camera_key(device_num, dir_path, basename, ext='jpg', delay=1, window_name='frame'):
    cap = cv2.VideoCapture(device_num)

    if not cap.isOpened():
        return

    os.makedirs(dir_path, exist_ok=True)
    base_path = os.path.join(dir_path, basename)

    n = 0
    while True:
        ret, frame = cap.read()
        cv2.imshow(window_name, frame)
        key = cv2.waitKey(delay) & 0xFF
        if key == ord('c'):
            cv2.imwrite('{}_{}.{}'.format(base_path, n, ext), frame)
            n += 1
        elif key == ord('q'):
            break

    cv2.destroyWindow(window_name)


save_frame_camera_key(0, 'C:\\Users\\Asha Kalara\\Desktop\\Images', 'camera_capture')


cv2.destroyAllWindows()



