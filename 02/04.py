import cv2
import MJFunction

src = cv2.imread('case4/04_1.png', cv2.IMREAD_COLOR)
dice_list = []
ans = [] 

#binalization
src_bin = MJFunction.binImg_04(src)
src_bin_INV = MJFunction.binImg_04_INV(src)

#dice labeling
dice_list = MJFunction.labelingImg(src_bin)
dice_list_INV = MJFunction.labelingImg(src_bin_INV)

#getnumber from dice
dice_ans_list = MJFunction.getDiceNumber(dice_list)
dice_ans_list_INV = MJFunction.getDiceNumber(dice_list_INV)

#sort & print
dice_ans_list = dice_ans_list + dice_ans_list_INV
dice_ans_list.sort()
print("dice : ", dice_ans_list)
MJFunction.showImg(src)
