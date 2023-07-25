import cv2
import numpy as np

def remove_shadow(frame, background, threshold=40):
    # グレースケールに変換
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_background = cv2.cvtColor(background, cv2.COLOR_BGR2GRAY)

    # 背景差分
    diff = cv2.absdiff(gray_frame, gray_background)

    # 閾値処理
    _, thresholded = cv2.threshold(diff, threshold, 255, cv2.THRESH_BINARY)

    # マスクの作成
    mask = cv2.inRange(thresholded, 1, 255)  # 二値化した画像から影の部分を抽出

    # 影の除去
    result = frame.copy()
    result[mask == 255] = [255, 255, 255]  # 影の部分を白色に置き換え

    return result

# 例として、背景差分を行う前後の2つのフレームを読み込む
frame1 = cv2.imread('C:\opencv_python\\road_sabun\\road_image\output\haikei.jpg')
frame2 = cv2.imread('C:\opencv_python\\road_sabun\\road_image\output\out_653.jpg')

# 影の除去を実行
result = remove_shadow(frame1, frame2)

# 結果を表示
cv2.imshow('Result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()