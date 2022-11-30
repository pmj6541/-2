import cv2

src = cv2.imread('02.png', cv2.IMREAD_GRAYSCALE)

src = src[30:280,0:250]

cv2.imwrite('01.png',src)