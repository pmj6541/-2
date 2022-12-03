import cv2

def blurring(src):
    for ksize in range(3, 9, 2):
        src = cv2.blur(src,(ksize,ksize))
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