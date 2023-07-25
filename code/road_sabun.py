import cv2
import numpy as np

img_1 = cv2.imread('C:\opencv_python\\road_coad\haikei.png')
img_2 = cv2.imread('C:\opencv_python\\road_coad\car2.png')
car_gray = cv2.cvtColor(img_2, cv2.COLOR_BGR2GRAY)
haikei_gray = cv2.cvtColor(img_1, cv2.COLOR_BGR2GRAY)
mask = cv2.absdiff(haikei_gray, car_gray)

kernel = np.ones((7, 7), np.uint8)
th = 10

mask[mask < th] = 0#二値化処理
mask[mask >= th] = 255#二値化処理

d_mask = cv2.dilate(mask, kernel)      #膨張処理
e_mask = cv2.erode(d_mask, kernel)  #収縮処理

tyou = 2000/614
menseki = tyou*tyou

retval, labels, stats, centroids = cv2.connectedComponentsWithStats(e_mask)
#print(stats)

yoko_1 = stats[1,2] * tyou / 100
yoko_1 = np.round(yoko_1,decimals=2)
tate_1 = stats[1,3] * tyou  / 100
tate_1 = np.round(tate_1,decimals=2)
yoko_2 = stats[2,2] * tyou / 100
yoko_2 = np.round(yoko_2,decimals=2)
tate_2 = stats[2,3] * tyou / 100
tate_2 = np.round(tate_2,decimals=2)

menseki_1 = menseki * stats[1,4] / 10000
menseki_1 = np.round(menseki_1,decimals=2)
menseki_2 = menseki * stats[2,4]/ 10000
menseki_2 = np.round(menseki_2,decimals=2)

cv2.putText(e_mask,f"yoko = {yoko_1} tate = {tate_1},menseki = {menseki_1}",(stats[1,0]-20,stats[1,1]-30),cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 1)
cv2.putText(e_mask,f"yoko = {yoko_2} tate = {tate_2},menseki = {menseki_2}",(stats[2,0]-400,stats[2,1]-30),cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 1)
cv2.imshow("mask",e_mask)
cv2.imshow("moto",img_2)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('C:\opencv_python\\bbb.jpg',e_mask)