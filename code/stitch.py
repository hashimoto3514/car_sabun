import cv2

def create_panorama(images):
    # スティッチャーの作成
    stitcher = cv2.Stitcher.create()

    # パノラマ画像の生成
    status, panorama = stitcher.stitch(images)

    if status == cv2.Stitcher_OK:
        return panorama
    else:
        print("パノラマ画像の生成に失敗しました:", status)
        return None

# 画像の読み込み
image1 = cv2.imread("C:\opencv\Project1\image\\3.jpg")
image2 = cv2.imread("C:\opencv\Project1\image\\4.jpg")
image3 = cv2.imread("C:\opencv\Project1\image\\5.jpg")
image4 = cv2.imread("C:\opencv\Project1\image\\6.jpg")
image5 = cv2.imread("C:\opencv\Project1\image\\1.jpg")

# パノラマ画像の生成
images = [image1, image2, image3, image4, image5]
panorama = create_panorama(images)

if panorama is not None:
    # パノラマ画像の表示
    cv2.imshow("Panorama", panorama)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite("C:\opencv\Project1\image\\panorama.jpg", panorama)

