import cv2
import Binalization, Labeling, DiceNumber, ImageProcess

src = cv2.imread('case4/04_1.png', cv2.IMREAD_COLOR)


#binalization
src_bin = Binalization.binImg_04(src)
src_bin_INV = Binalization.binImg_04_INV(src)

#dice labeling
dice_list = Labeling.labelingImg_03_04(src_bin)
dice_list_INV = Labeling.labelingImg_03_04(src_bin_INV)

#getnumber from dice
dice_ans_list = DiceNumber.getDiceNumber_03_04(dice_list)
dice_ans_list_INV = DiceNumber.getDiceNumber_03_04(dice_list_INV)

#sort & print
dice_ans_list = dice_ans_list + dice_ans_list_INV
dice_ans_list.sort()
print("dice : ", dice_ans_list)
ImageProcess.showImg(src)
