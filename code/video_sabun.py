import cv2
import numpy as np
import time

def binary_threshold(image, threshold_value):

    # 二値化処理
    _, binary_image = cv2.threshold(image, threshold_value, 255, cv2.THRESH_BINARY)

    return binary_image

# 差分を数値化
def getDiff(img1, img2):
    # グレースケール変換
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    # 差分取得
    mask = cv2.absdiff(img1, img2)
    # ２値化
    th = 10
    mask = binary_threshold(mask,th)

    kernel = np.ones((3, 3), np.uint8)
    mask = cv2.dilate(mask, kernel)      #膨張処理
    mask = cv2.erode(mask, kernel)  #収縮処理

    return cv2.countNonZero(mask),mask # 白の要素数

'''
#動画ファイルの読み込み
cap = cv2.VideoCapture("C:\opencv_python\\road_sabun\\road_image\car_2_trim.mp4")

span = 50  # 静止間隔
threshold = 1000 # 変化の敷居値

# 最初のフレームを背景画像に設定
ret, previous = cap.read()
ret2,haikei = cap.read()
cv2.imwrite(f'C:\opencv_python\\road_sabun\\road_image\output2\haikei.jpg',haikei)
counter=0
frame_num = 0

time.sleep(2)

while(cap.isOpened()):
    # フレームの取得
    ret, frame = cap.read()
    
    if ret == False:
        break

    # 差分計算    
    diff,mask = getDiff(previous, frame)

    if(diff < threshold):
        counter+=1
    else:
        counter=0

    #print("diff:{} counter:{}".format(diff,counter))

    # 一定以下の変化量が、一定時間続いたら描画する
    if(span < counter):
        counter = 0
        # 監視画面を更新
        cv2.imshow("previous", frame)
        
        diff2,mask2 = getDiff(haikei,frame)
        if diff2 > 15000:
            cv2.imwrite(f'C:\opencv_python\\road_sabun\\road_image\output2\out_{frame_num}.jpg',frame)


    
    # フレームを表示
    cv2.imshow("Flame", frame)

    # 今回のフレームを１つ前として保存する
    previous = frame

    frame_num += 1 

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

'''
img_1 = cv2.imread('C:\opencv_python\\road_sabun\\road_image\output2\haikei.jpg')
img_2 = cv2.imread('C:\opencv_python\\road_sabun\\road_image\output2\out_1280.jpg')

diff ,mask = getDiff(img_1,img_2)
cv2.imwrite(f'C:\opencv_python\\road_sabun\\road_image\output2\mask\mask1280.jpg',mask)
cv2.imshow("mask",mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
