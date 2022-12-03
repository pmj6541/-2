import cv2

def blurring(src):
    for ksize in range(3, 9, 2):
        src = cv2.blur(src,(ksize,ksize))
    return src

def sharpening(src):
    for sigma in range(1,6):
        blurred = cv2.GaussianBlur(src, (0,0), sigma)

        alpha = 1.0
        src = cv2.addWeighted(src, 1+alpha, blurred, -alpha, 0.0)
    return src

def saturated(value):
    if value > 255:
        value = 255
    elif value < 0:
        value = 0
    return value

def showImg(src):
    cv2.imshow('src',src)
    cv2.waitKey()
    cv2.destroyAllWindows()