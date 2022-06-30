import cv2
import time
import numpy

video = cv2.VideoCapture(0)

def light_detector(gray):
    var1 = numpy.mean(gray[220][0:300])
    var2 = numpy.mean(gray[0][0:300])
    var3 = numpy.mean(gray[440][0:300])
    var_1 = numpy.mean(gray[-220][-0:-300])
    var_2 = numpy.mean(gray[-0][-0:-300])
    var_3 = numpy.mean(gray[-440][-0:-300])
    global right_screen
    global left_screen
    right_screen = var1 + var2 + var3 // 3
    left_screen = var_1 + var_2 + var_3 // 3
    return right_screen, left_screen

def rotate_right():
    if right_screen > left_screen:
        print("Rotate right")
def rotate_left():
    if left_screen > right_screen:
        print("Rotate left")

while True:
    check, frame = video.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    light_detector(gray)
    time.sleep(3)
    print(f"Left screen brightness: {int(left_screen)}")
    print(f"Right screen brightness: {int(right_screen)}")
    cv2.imshow("capturing",gray)

    rotate_right()
    rotate_left()

    key = cv2.waitKey(1000)
    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
