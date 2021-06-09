import cv2
import numpy

# read images
img1 = cv2.imread('img1.jpg')
img2 = cv2.imread('img2.jpg')
img3 = cv2.imread('img4.jpg')

# crop images
crop_1 = img1[:499, :800]
crop_2 = img2[:, 368:]
crop_3 = img3[400:640, 340:1520]

# collage in making
final = numpy.hstack((crop_1, crop_2))
final = numpy.vstack((crop_3, final))

# show image
cv2.imshow('hi', final)
cv2.waitKey()
cv2.destroyAllWindows()
