import cv2
import numpy as np

def nothing(x):
    pass

cv2.namedWindow('Color Palette')
cv2.createTrackbar('B', 'Color Palette', 0, 255, nothing)
cv2.createTrackbar('G', 'Color Palette', 0, 255, nothing)
cv2.createTrackbar('R', 'Color Palette', 0, 255, nothing)

while True:
    b = cv2.getTrackbarPos('B', 'Color Palette')
    g = cv2.getTrackbarPos('G', 'Color Palette')
    r = cv2.getTrackbarPos('R', 'Color Palette')
    image = np.zeros((300, 300, 3), np.uint8)
    image[:] = [b, g, r]
    cv2.imshow('Color Palette', image)
    if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit
        break

cv2.destroyAllWindows()
