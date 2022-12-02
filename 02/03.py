import cv2
import MJFunction

src = cv2.imread('case3/03_2.png', cv2.IMREAD_GRAYSCALE)
dice_list = []
ans = [] 

#binalization
src_bin = MJFunction.binImg_03(src)

#dice labeling
dice_list = MJFunction.labelingImg(src_bin)

#getnumber from dice
dice_ans_list = MJFunction.getDiceNumber(dice_list)

#sort & print
dice_ans_list.sort()
print("dice : ", dice_ans_list)
