import cv2
import numpy as np

img = cv2.imread('C:\opencv\Project1\image\\panorama.jpg') # 提示画像

W, H = (1500, 400) # 変換先の矩形

# 変換前後の点を対応させる（左上から時計回りに指定する）
pts1 = np.float32([[298,411],[1453,431],[1502,567],[240,480]])
pts2 = np.float32([[0,0],[W,0],[W,H],[0,H]])

# 射影変換
M = cv2.getPerspectiveTransform(pts1, pts2)
dst = cv2.warpPerspective(img, M, (W, H))

cv2.imwrite("out2.jpg", dst)