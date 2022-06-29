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
    print(int(light_detector(gray)))
    time.sleep(1)
    cv2.imshow("capturing",gray)
    left_screen = numpy.mean(gray[220][0:300])
    right_screen = numpy.mean(gray[-220][-0:-300])

    key = cv2.waitKey(1000)
    if key == ord('q'):
        break

    elif left_screen > right_screen:
        print("Rotate left")
    elif right_screen > left_screen:
        print("Rotate right")
    else:
        print("Error")

video.release()
cv2.destroyAllWindows()
