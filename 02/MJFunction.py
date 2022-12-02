import cv2
import numpy as np

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


def binImg_03(src) :
    alpha = 3.0
    dst = np.empty(src.shape, dtype=src.dtype)
    for y in range(src.shape[0]):
        for x in range(src.shape[1]):
            dst[y, x] = saturated(src[y, x] + (src[y, x]-200) * alpha)


    _, src_bin = cv2.threshold(dst, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    
    src_bin = cv2.morphologyEx(src_bin, cv2.MORPH_OPEN, None)
    src_bin = cv2.morphologyEx(src_bin, cv2.MORPH_CLOSE, None)
    
    return src_bin

def binImg_04(src) :
    src_blu = blurring(src)
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
    src_blu = blurring(src)
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


def labelingImg(src) :
    cnt, _, stats, _ = cv2.connectedComponentsWithStats(src)
    dice_list = []
    for i in range(1,cnt):
        (x, y, w, h, area) = stats[i]

        if abs(w-h)>15 or area < 2500:
            continue
        if area < 100:
            continue
        tmp = src[y:y+h,x:x+w]
        showImg(tmp)
        dice_list.append(tmp)
    return dice_list

def labelingDice(src) : 
    cnt, _, stats, _ = cv2.connectedComponentsWithStats(src)
    dice_list = []
    for i in range(1,cnt):
        (x, y, w, h, area) = stats[i]

        if abs(w-h)>15 or area > 700:
            continue
        if area < 200:
            continue
        tmp = src[y:y+h,x:x+w]
        cnt_test, _, _, _ = cv2.connectedComponentsWithStats(tmp)
        if cnt_test == 2:
            dice_list.append(tmp)
    return dice_list

def getDiceNumber(dice_list) :
    ans = []
    tmp_dice = []
    for i in range(len(dice_list)):
        tmp_dice = labelingDice(~dice_list[i])
        if len(tmp_dice)<7 and len(tmp_dice)>0:
            ans.append(len(tmp_dice)) 
    return ans

def showImg(src):
    cv2.imshow('src',src)
    cv2.waitKey()
    cv2.destroyAllWindows()