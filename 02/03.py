import cv2
import Binalization, Labeling, DiceNumber, ImageProcess

src = cv2.imread('case3/03_1.png', cv2.IMREAD_COLOR)
src_gray = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)

#binalization
src_bin = Binalization.binImg_03(src_gray)


#dice labeling
dice_list = Labeling.labelingImg_03_04(src_bin)


#getnumber from dice
dice_ans_list = DiceNumber.getDiceNumber_03_04(dice_list)


#sort & print
dice_ans_list.sort()
print("dice : ", dice_ans_list)
ImageProcess.showImg(src)
