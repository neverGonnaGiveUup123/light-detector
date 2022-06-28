import cv2
import time
import numpy

video = cv2.VideoCapture(0)


def light_detector(gray):
    global light
    light = 0
    for i in gray:
        light = light + numpy.mean(i)
    return light // 1000
while True:
    check, frame = video.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    print(light_detector(gray))
    time.sleep(1)
    cv2.imshow("capturing",gray)

    key = cv2.waitKey(1000)
    if key == ord('q'):
        break
video.release()
cv2.destroyAllWindows()