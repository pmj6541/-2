import cv2
import numpy as np
import ImageProcess

def labelingDice_03_04(src) : 
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

def getDiceNumber_03_04(dice_list) :
    ans = []
    tmp_dice = []
    for i in range(len(dice_list)):
        tmp_dice = labelingDice_03_04(~dice_list[i])
        if len(tmp_dice)<7 and len(tmp_dice)>0:
            ans.append(len(tmp_dice)) 
    return ans

def labelingDice_05(src) : 
    cnt, _, stats, _ = cv2.connectedComponentsWithStats(src)
    dice_list = []
    for i in range(1,cnt):
        (x, y, w, h, area) = stats[i]

        if abs(w-h)>15 or area > 2000:
            continue
        if area < 350:
            continue
        tmp = src[y:y+h,x:x+w]
        cnt_test, _, _, _ = cv2.connectedComponentsWithStats(tmp)
        if cnt_test == 2:
            dice_list.append(tmp) 
    return dice_list

def getDiceNumber_05(dice_list) :
    ans = []
    tmp_dice = []
    for i in range(len(dice_list)):
        tmp_dice = labelingDice_05(~dice_list[i])
        if len(tmp_dice)<7 and len(tmp_dice)>0:
            ans.append(len(tmp_dice)) 
    return ans