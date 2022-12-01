import cv2
import numpy as np

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
    showImg(src)
    _, src_bin = cv2.threshold(src, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    
    src_bin = cv2.morphologyEx(src_bin, cv2.MORPH_OPEN, None)
    src_bin = cv2.morphologyEx(src_bin, cv2.MORPH_CLOSE, None)
    
    return src_bin

def saturated(value):
    if value > 255:
        value = 255
    elif value < 0:
        value = 0
    return value

def labelingImg(src) :
    cnt, _, stats, _ = cv2.connectedComponentsWithStats(src)
    dice_list = []
    for i in range(1,cnt):
        (x, y, w, h, area) = stats[i]

        if area < 20 :
            continue
        tmp = src[y:y+h,x:x+w]
        dice_list.append(tmp)
    return dice_list

def labelingDice(src) : 
    cnt, _, stats, _ = cv2.connectedComponentsWithStats(src)
    dice_list = []
    for i in range(1,cnt):
        (x, y, w, h, area) = stats[i]

        if abs(w-h)>20 or area > 800:
            continue
        if area < 100:
            continue
        tmp = src[y:y+h,x:x+w]
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