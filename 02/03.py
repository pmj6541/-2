import cv2
import numpy as np
import random
import MJFunction

src = cv2.imread('03_2.png', cv2.IMREAD_GRAYSCALE)
dice_list = []
ans = [] 

#이진화 필요
src_bin = MJFunction.binImg(src)

#labeling
dice_list = MJFunction.labelingImg(src_bin)

#getDiceNumberList
dice_ans_list = MJFunction.getDiceNumber(dice_list)

print(dice_ans_list)


cv2.imshow('binImg',src_bin)
cv2.waitKey()
cv2.destroyAllWindows()

contours, hierarchy = cv2.findContours(src_bin, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
contours_dices, hierarchy_dices = cv2.findContours(src_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

dst = cv2.cvtColor(src_bin,cv2.COLOR_GRAY2BGR)





print(len(contours_dices))



cv2.imshow('src',dst)
cv2.waitKey()
cv2.destroyAllWindows()

