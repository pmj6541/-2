import cv2

src = cv2.imread('02.png', cv2.IMREAD_GRAYSCALE)
_, src_bin = cv2.threshold(src, 0, 60, cv2.THRESH_BINARY | cv2.THRESH_TRIANGLE)
cnt, labels, stats, centroids = cv2.connectedComponentsWithStats(src_bin)
dst = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)
dice = [0]
ans = []


for i in range(1,cnt):
    (x,y,w,h,area) = stats[i]
    dice_src = ~src[y:y+h,x:x+w]
    _, tmp = cv2.threshold(dice_src, 0, 60, cv2.THRESH_BINARY | cv2.THRESH_TRIANGLE)
    dice.append(tmp)
    cnt_dice, _, stats_dice, _ = cv2.connectedComponentsWithStats(dice[i])

    ans_num = 0
    for j in range(2,cnt_dice):
        (dice_x,dice_y,dice_w,dice_h,dice_area) = stats_dice[j]
        if dice_area < 200:
            continue
        ans_num += 1
        pt1 = (dice_x+x, dice_y+y)
        pt2 = (dice_x+x + dice_w, dice_y+y + dice_h)
        cv2.rectangle(dst,pt1,pt2,(0,255,255))
    ans.append(ans_num)
    if area < 20:
        continue
ans.sort()
print('dice : ',ans)

