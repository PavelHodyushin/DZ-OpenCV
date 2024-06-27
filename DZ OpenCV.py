import cv2
import numpy as np

photo = np.zeros((800, 800, 3), dtype="uint8")
for i in range(100):
    cv2.rectangle(photo, (i, i), (photo.shape[1]-i, photo.shape[0]-i), (22, 150, 22+i), thickness=cv2.FILLED)

cv2.rectangle(photo, (0, 0), (photo.shape[1], photo.shape[0]), (255, 255, 255), thickness=3)
cv2.line(photo, (200, 200), (300, 200), (0, 0, 255), thickness=5)
cv2.line(photo, (500, 200), (600, 200), (0, 0, 255), thickness=5)
cv2.line(photo, (500, 200), (500, 400), (255, 0, 0), thickness=5)
cv2.line(photo, (600, 200), (600, 400), (255, 0, 0), thickness=5)
cv2.line(photo, (300, 200), (300, 400), (255, 0, 0), thickness=5)
cv2.line(photo, (200, 200), (200, 400), (255, 0, 0), thickness=5)
cv2.circle(photo, (400, 400), 350, (255, 255, 255),thickness=3)
cv2.putText(photo, 'Urban', (260, 170),
           cv2.FONT_HERSHEY_TRIPLEX, 3, (255, 0, 0))
cv2.putText(photo, 'University', (250, 660),
           cv2.FONT_HERSHEY_TRIPLEX, 2, (255, 0, 0))
cv2.ellipse(photo, (400, 400), (100, 100), 0, 0, 180, (0, 255, 0), 3)
cv2.ellipse(photo, (400, 400), (200, 200), 0, 0, 180, (0, 255, 0), 3)
cv2.rectangle(photo, (750, 750), (50, 50), (255, 255, 255), thickness=5)
cv2.imshow('Photo', photo)
cv2.waitKey(0)











# [
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0],
# ]