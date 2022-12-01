import cv2
import MJFunction

src = cv2.imread('03_2.png', cv2.IMREAD_GRAYSCALE)
dice_list = []
ans = [] 

#이진화 필요
src_bin = MJFunction.binImg_03(src)

#labeling
dice_list = MJFunction.labelingImg(src_bin)

#getDiceNumberList
dice_ans_list = MJFunction.getDiceNumber(dice_list)
dice_ans_list.sort()
print("dice : ", dice_ans_list)
