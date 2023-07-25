import cv2
import numpy as np

def find_keypoints_and_descriptors(image):
    # SIFT特徴量の初期化
    sift = cv2.SIFT_create()

    # 特徴点と特徴記述子の抽出
    keypoints, descriptors = sift.detectAndCompute(image, None)

    return keypoints, descriptors

def match_keypoints(descriptors1, descriptors2):
    # FLANNベースの特徴点マッチャーの初期化
    flann = cv2.FlannBasedMatcher_create()

    # 特徴点のマッチング
    matches = flann.knnMatch(descriptors1, descriptors2, k=2)

    # ベストマッチの選択
    good_matches = []
    for m, n in matches:
        if m.distance < 2 * n.distance:
            good_matches.append(m)

    return good_matches

def create_panorama(images):
    # 特徴点と特徴記述子のリスト
    keypoints_list = []
    descriptors_list = []

    # 特徴点と特徴記述子の抽出
    for image in images:
        keypoints, descriptors = find_keypoints_and_descriptors(image)
        keypoints_list.append(keypoints)
        descriptors_list.append(descriptors)

    # パノラマ画像の初期化
    panorama = images[0]

    for i in range(len(images) - 1):
        # 画像間の特徴点のマッチング
        matches = match_keypoints(descriptors_list[i], descriptors_list[i+1])

        # 特徴点の対応座標の取得
        src_pts = np.float32([keypoints_list[i][m.queryIdx].pt for m in matches]).reshape(-1, 1, 2)
        dst_pts = np.float32([keypoints_list[i+1][m.trainIdx].pt for m in matches]).reshape(-1, 1, 2)

        # ホモグラフィー行列の推定
        M, _ = cv2.findHomography(dst_pts, src_pts, cv2.RANSAC, 5.0)

        # パノラマ画像への変換
        warped_image = cv2.warpPerspective(images[i+1], M, (panorama.shape[1]+images[i+1].shape[1], panorama.shape[0]))
        warped_image[:, 0:panorama.shape[1]] = panorama

        # パノラマ画像の更新
        panorama = warped_image

    return panorama

# 画像の読み込み
image1 = cv2.imread("C:\opencv\Project1\image\\3.jpg")
image2 = cv2.imread("C:\opencv\Project1\image\\4.jpg")
image3 = cv2.imread("C:\opencv\Project1\image\\5.jpg")
image4 = cv2.imread("C:\opencv\Project1\image\\6.jpg")
image5 = cv2.imread("C:\opencv\Project1\image\\1.jpg")

# パノラマ画像の生成
images = [image1, image2, image3, image4, image5]

# パノラマ画像の生成
panorama = create_panorama(images)

# パノラマ画像の表示
cv2.imshow("Panorama", panorama)
cv2.waitKey(0)
cv2.destroyAllWindows()