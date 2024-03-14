import cv2
import numpy as np
import os
import random
import string
import datetime

# Function to generate a random filename
def random_filename():
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(10)) + '.png'

# Mouse callback function
drawing = False
ix, iy = -1, -1
line_counter = 0  # Counter for the number of lines drawn
n_lines_before_save = 2  # Number of lines to draw before saving, can be changed
counter = 0
def draw(event, x, y, flags, param):
    global ix, iy, drawing, line_counter, counter

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            cv2.line(img, (ix, iy), (x, y), (0, 0, 0), 5)
            ix, iy = x, y

    elif event == cv2.EVENT_LBUTTONUP:
        if drawing:
            cv2.line(img, (ix, iy), (x, y), (0, 0, 0), 5)
            drawing = False
            line_counter += 1
            counter+=1
            if line_counter >= n_lines_before_save:
                # Save the image
                filename = random_filename()
                cv2.imwrite(filename, img)
                print(f"Image {counter}: File saved: {os.path.abspath(filename)} at {datetime.datetime.now()}")
                # Clear the canvas and reset counter
                img[:] = [255, 255, 255]
                line_counter = 0

# Create a black canvas
img = np.ones((278, 278, 3), np.uint8)*255
cv2.namedWindow('Canvas')
cv2.setMouseCallback('Canvas', draw)

while True:
    cv2.imshow('Canvas', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # press 'q' to quit
        break

cv2.destroyAllWindows()
