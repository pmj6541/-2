import cv2
import numpy as np

src = cv2.imread('03.png', cv2.IMREAD_GRAYSCALE)
dice = [0]
ans = []
def saturated(value):
    if value > 255:
        value = 255
    elif value < 0:
        value = 0
    return value
#이진화 필요
alpha = 5.0
avg = np.mean(src)
dst = np.empty(src.shape, dtype=src.dtype)
for y in range(src.shape[0]):
    for x in range(src.shape[1]):
        dst[y, x] = saturated(src[y, x] + (src[y, x]-260) * alpha)

cv2.imshow('src',dst)
cv2.waitKey()
_, src_bin = cv2.threshold(dst, 0, 255, cv2.THRESH_TOZERO | cv2.THRESH_OTSU)
_, src_bin = cv2.threshold(src_bin, 0, 255, cv2.THRESH_OTSU)
cv2.imshow('bin',src_bin)
cv2.waitKey()
cv2.destroyAllWindows()
cnt, labels, stats, centroids = cv2.connectedComponentsWithStats(src_bin)
dst = cv2.cvtColor(src_bin, cv2.COLOR_GRAY2BGR)




for i in range(1,cnt):
    (x,y,w,h,area) = stats[i]
    dice_src = src[y:y+h,x:x+w]
    cv2.imshow('dice',dice_src)
    cv2.waitKey()
    _, tmp = cv2.threshold(dice_src, 0, 60, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    dice.append(tmp)
    cnt_dice, _, stats_dice, _ = cv2.connectedComponentsWithStats(dice[i])

    ans_num = 0
    for j in range(2,cnt_dice):
        (dice_x,dice_y,dice_w,dice_h,dice_area) = stats_dice[j]
        print(stats_dice[j])
        if dice_w < 20 or dice_h < 20:
            continue
        ans_num += 1
        pt1 = (dice_x+x, dice_y+y)
        pt2 = (dice_x+x + dice_w, dice_y+y + dice_h)
        cv2.rectangle(dst,pt1,pt2,(0,255,255))
    ans.append(ans_num)
    if area < 20:
        continue
ans.sort()
cv2.imshow('src',dst)
cv2.waitKey()
cv2.destroyAllWindows()
print('dice : ',ans)

