import cv2
import matplotlib.pyplot as plt
im=cv2.imread("Pic.PNG")
dst=cv2.GaussianBlur(im,(5,5),cv2.BORDER_DEFAULT)
plt.imshow(dst)
plt.show()