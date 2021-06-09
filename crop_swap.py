import cv2

# swap of moon in sun image.
moon = cv2.imread('moon.jpg')
crop_moon = moon[132:291, 542:702]
sun[470:629, 430:590] = crop_moon
cv2.imshow('hi', sun)
cv2.waitKey()
cv2.destroyAllWindows()

# swap of sun in moon image.
sun = cv2.imread('sun.jpg')
crop_sun = sun[470:629, 430:590]
moon[132:291, 542:702] = crop_sun
cv2.imshow('hi', moon)
cv2.waitKey()
cv2.destroyAllWindows()
