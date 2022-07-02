# light-detector
This is a light level detector. 
This works best when used in a dark room. Use a small light source such as a phone flashlight and hold it up to the camera. 
If the code says 'rotate right', rotate the camera relative to your right and vice versa for 'rotate left'.
This is not a darkness detector, holding up a black object will not make the code rotate in the opposite direction(it might sometimes though this is unreliable).

This code draws 5 lines on each half of the screens and averages the brightness of each pixel on each line.
Then combines each line on the respective half of the screen and averages that and returns that value as that half's average brightness. 
The code will then tell you to rotate the camera towards the brighter half of the screen.
