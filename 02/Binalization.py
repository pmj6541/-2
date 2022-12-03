import cv2
import numpy as np
import ImageProcess


def binImg_03(src) :
    alpha = 3.0
    dst = np.empty(src.shape, dtype=src.dtype)
    for y in range(src.shape[0]):
        for x in range(src.shape[1]):
            dst[y, x] = ImageProcess.saturated(src[y, x] + (src[y, x]-200) * alpha)


    _, src_bin = cv2.threshold(dst, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    
    src_bin = cv2.morphologyEx(src_bin, cv2.MORPH_OPEN, None)
    src_bin = cv2.morphologyEx(src_bin, cv2.MORPH_CLOSE, None)
    
    return src_bin

def binImg_04(src) :
    src_blu = ImageProcess.blurring(src)
    #showImg(src_blu)

    bgr_planes = cv2.split(src_blu)
    _, src_bin_0 = cv2.threshold(bgr_planes[0], 155, 85, cv2.THRESH_BINARY )
    _, src_bin_1 = cv2.threshold(bgr_planes[1], 155, 85, cv2.THRESH_BINARY )
    _, src_bin_2 = cv2.threshold(bgr_planes[2], 155, 85, cv2.THRESH_BINARY )
    
    src_bin = src_bin_0 +  src_bin_1 + src_bin_2
    #showImg(src_bin)
    src_bin = cv2.dilate(src_bin, np.ones((3,3), np.uint8)) 
    _, src_bin = cv2.threshold(src_bin, 180, 255, cv2.THRESH_BINARY )
    #showImg(src_bin)
    
    return src_bin

def binImg_04_INV(src) :
    src_blu = ImageProcess.blurring(src)
    #showImg(src_blu)

    bgr_planes = cv2.split(src_blu)
    _, src_bin_0 = cv2.threshold(bgr_planes[0], 155, 85, cv2.THRESH_BINARY )
    _, src_bin_1 = cv2.threshold(bgr_planes[1], 155, 85, cv2.THRESH_BINARY )
    _, src_bin_2 = cv2.threshold(bgr_planes[2], 155, 85, cv2.THRESH_BINARY )
    
    src_bin = src_bin_0 +  src_bin_1 + src_bin_2
    #showImg(src_bin)
    src_bin = cv2.dilate(src_bin, np.ones((3,3), np.uint8)) 
    _, src_bin = cv2.threshold(src_bin, 254, 0, cv2.THRESH_TOZERO_INV )
    _, src_bin = cv2.threshold(src_bin, 70, 255, cv2.THRESH_BINARY )
    #showImg(src_bin)

    return src_bin

def binImg_05(src) :
    alpha = 3.0
    for y in range(src.shape[0]):
        for x in range(src.shape[1]):
            src[y, x] = ImageProcess.saturated(src[y, x] + (src[y, x]-190) * alpha)
    
    _, src_bin = cv2.threshold(src, 80, 255, cv2.THRESH_BINARY )

    src_bin = cv2.morphologyEx(src_bin, cv2.MORPH_OPEN, None)
    src_bin = cv2.morphologyEx(src_bin, cv2.MORPH_CLOSE, None)
    
    return src_bin