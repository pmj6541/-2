import cv2

def labelingImg_03_04(src) :
    cnt, _, stats, _ = cv2.connectedComponentsWithStats(src)
    dice_list = []
    for i in range(1,cnt):
        (x, y, w, h, area) = stats[i]

        if abs(w-h)>15 or area < 2500:
            continue
        if area < 100:
            continue
        tmp = src[y:y+h,x:x+w]
        dice_list.append(tmp)
    return dice_list

def labelingImg_05(src) :
    cnt, _, stats, _ = cv2.connectedComponentsWithStats(src)
    dice_list = []
    for i in range(1,cnt):
        (x, y, w, h, area) = stats[i]

        if area < 10000:
            continue
        if area < 100:
            continue
        tmp = src[y:y+h,x:x+w]
        dice_list.append(tmp)
    return dice_list