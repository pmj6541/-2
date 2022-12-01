import cv2
import numpy as np
import math

def binImg(src) :
    alpha = 3.0
    dst = np.empty(src.shape, dtype=src.dtype)
    for y in range(src.shape[0]):
        for x in range(src.shape[1]):
            dst[y, x] = saturated(src[y, x] + (src[y, x]-200) * alpha)


    _, src_bin = cv2.threshold(dst, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    
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
    cnt, labels, stats, centroids = cv2.connectedComponentsWithStats(src)
    dice_list = []
    for i in range(1,cnt):
        (x, y, w, h, area) = stats[i]

        if area < 20:
            continue
        print(area)
        tmp = src[y:y+h,x:x+w]
        dice_list.append(tmp)
    
    #affine transformation


    return dice_list

def setLabel(img, pts, label):
    (x,y,w,h) = cv2.boundingRect(pts)
    pt1 = (x,y)
    pt2 = (x+w, y+h)
    cv2.rectangle(img, pt1, pt2, (0,0,255),1)
    cv2.putText(img,label,pt1,cv2.FONT_HERSHEY_PLAIN,1,(0,0,255))
    cv2.imshow('src',img)
    cv2.waitKey()
    cv2.destroyAllWindows()


def getDiceNumber(dice_list) :
    ans = []
    cnt = 0
    for i in range(len(dice_list)):
        cv2.imshow('src',dice_list[i])
        cv2.waitKey()
        cv2.destroyAllWindows()
        contours, hierarchy = cv2.findContours(~dice_list[i], cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        approx = cv2.approxPolyDP(contours[i], cv2.arcLength(contours[i], True)*0.02, True)

        vtc = len(approx)
        if vtc != 3 and vtc != 4:
            lenth = cv2.arcLength(contours[i], True)
            area = cv2.contourArea(contours[i])
            ratio = 4. * math.pi * area / (lenth * lenth)     
            if ratio > 0.55:
                cnt += 1
            setLabel(dice_list[i], contours[i],'CIR')
        ans.append(cnt) 
    return ans