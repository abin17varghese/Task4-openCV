import cv2
import numpy

bg = numpy.zeros((512, 512, 3))
bg[:] = [255, 255, 255]

# line creation
cv2.line(bg, (128, 75), (384, 75), [255, 255, 0], 2)
cv2.line(bg, (128, 80), (384, 80), [255, 255, 0], 2)

# Text in the image
cv2.putText(bg, 
            '...Example!!!...', 
            (150, 70),
            fontFace=cv2.FONT_HERSHEY_TRIPLEX, 
            fontScale=0.8, 
            color=(0, 0, 255), 
            thickness=2)

# Drawing an emoji
# Face outline
cv2.circle(bg, (256, 256), radius=100, color=[0, 0, 0], thickness=2)
# Eyes
cv2.circle(bg, (220, 220), radius=10, color=[0, 0, 0], thickness=-1)
cv2.circle(bg, (286, 220), radius=10, color=[0, 0, 0], thickness=-1)
# Nose
cv2.circle(bg, (253, 270), radius=8, color=[0, 0, 0], thickness=-1)
cv2.line(bg, (245, 270), (253, 245), [0, 0, 0], 2)
cv2.line(bg, (261, 270), (253, 245), [0, 0, 0], 2)
# Mouth
cv2.ellipse(bg,(256,290),(60,30),0,0,180,0,-1)

cv2.putText(bg, 
            'Thank You.', 
            (350, 500),
            fontFace=cv2.FONT_HERSHEY_SIMPLEX, 
            fontScale=0.8, 
            color=(0, 0, 255), 
            thickness=2)
            
cv2.imshow('show_image', bg)
cv2.waitKey()
cv2.destroyAllWindows()

