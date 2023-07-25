import cv2

# マウスクリックイベントのコールバック関数
def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print("Clicked at (x, y):", x, y)

# 画像読み込み
image = cv2.imread("C:\opencv_python\\road_sabun\\road_image\output2\out_453.jpg")

# ウィンドウの作成とマウスイベントの設定
cv2.namedWindow("Image")
cv2.setMouseCallback("Image", mouse_callback)

# 画像表示
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()