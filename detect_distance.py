import cv2
import pyrealsense2
from realsense_depth import *

width = 640
length = 480


point = (400, 300)

def show_distance(event, x, y, args, params):
    global point
    point = (x, y)

# Initialize Camera Intel Realsense, it is a class in realsense_depth
dc = DepthCamera()

# Create mouse event
cv2.namedWindow("Color frame")
cv2.setMouseCallback("Color frame", show_distance)

'''
while True:
    ret, depth_frame, color_frame = dc.get_frame()

    # Show distance for a specific point
    cv2.circle(color_frame, point, 4, (0, 0, 255))
    distance = depth_frame[point[1], point[0]]

    cv2.putText(color_frame, "{}mm".format(distance), (point[0], point[1] - 20), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 2)

    cv2.imshow("depth frame", depth_frame)
    cv2.imshow("Color frame", color_frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

'''

# Function to iterate over frame within the image and reaturn distance
# of the closest point

distance = 0
tracking_point_x = 0
tacking_point_y = 0

'''

This is a pretty simple loop that goes over the image and computes the depth
of the objects at a certain pixel. The depth of the the objects at these pixels
is gotten from the depth camera on the intel realsense and this value is gotten
using the intel realsense library from pyrealsense2. 

'''

while True:
    ret, depth_frame, color_frame = dc.get_frame()
    for i in range(0, width):
        y = 0
        for y in range (0, length):
            messured_distance = depth_frame[width, length]
            if messured_distance < distance:
                    distance = messured_distance
                    tracking_point_x = width
                    tracking_point_y = length
            y += 10
    i += 10
    cord_circle = (tracking_point_x, tracking_point_y)
    cv2.circle(color_frame, cord_circle, 10, (0, 0, 255))
