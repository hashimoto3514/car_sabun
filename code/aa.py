import cv2
import numpy as np

def create_top_view(images):
    # スティッチャーの作成
    stitcher = cv2.Stitcher.create()

    # パノラマ画像の生成
    status, panorama = stitcher.stitch(images)

    if status != cv2.Stitcher_OK:
        print("パノラマ画像の生成に失敗しました:", status)
        return None

    # パノラマ画像の高さと幅を取得
    height, width = panorama.shape[:2]

    # 変換前の4点と変換後の4点を指定
    src_points = np.float32([[0, 0], [width, 0], [width, height], [0, height]])
    dst_points = np.float32([[0, 0], [width, 0], [width, 2*height], [0, 2*height]])

    # 変換行列の計算
    M = cv2.getPerspectiveTransform(src_points, dst_points)

    # 射影変換の実行
    top_view = cv2.warpPerspective(panorama, M, (width, 2*height))

    return top_view

# 画像の読み込み
image1 = cv2.imread("C:\opencv_python\image\hidari.jpg")
image2 = cv2.imread("C:\opencv_python\image\\naka.jpg")
image3 = cv2.imread("C:\opencv_python\image\migi.jpg")

# 画像リストの作成
images = [image1, image2, image3]

# 上方からの写真の生成
top_view = create_top_view(images)

if top_view is not None:
    # 上方からの写真の表示
    cv2.imshow("Top View", top_view)
    cv2.waitKey(0)
    cv2.destroyAllWindows()