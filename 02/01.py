import cv2
import numpy as np

src = cv2.imread('01.png', cv2.IMREAD_GRAYSCALE)
_, src_bin = cv2.threshold(src, 0, 80, cv2.THRESH_BINARY | cv2.THRESH_TRIANGLE)
cnt, labels, stats, centroids = cv2.connectedComponentsWithStats(src_bin)
dst = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)
dice = [0]

(x,y,w,h,area) = stats[1]
dice_src = ~src[y:y+h,x:x+w]
_, tmp = cv2.threshold(dice_src, 0, 80, cv2.THRESH_BINARY | cv2.THRESH_TRIANGLE)
dice.append(tmp)
cnt_dice, _, stats_dice, _ = cv2.connectedComponentsWithStats(dice[1])
ans = 0
for j in range(2,cnt_dice):
    (dice_x,dice_y,dice_w,dice_h,dice_area) = stats_dice[j]
    if dice_w < 30 or dice_h < 30:
        continue
    ans += 1
    pt1 = (dice_x+x, dice_y+y)
    pt2 = (dice_x+x + dice_w, dice_y+y + dice_h)
    cv2.rectangle(dst,pt1,pt2,(0,255,255))
print("dice : ",ans)

cv2.imshow('dst',dst)

cv2.waitKey()
cv2.destroyAllWindows()
