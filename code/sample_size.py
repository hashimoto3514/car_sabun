import cv2
import numpy as np

def get_shape_information(image):

    # 連結成分のラベリングと統計情報の取得
    retval, labels, stats, centroids = cv2.connectedComponentsWithStats(image)

    # 各物体の情報を格納するリスト
    shapes = []

    # 背景（ラベル0）は無視して、物体の情報を取得
    for label in range(1, retval):
        left, top, width, height, area = stats[label]
        centroid_x, centroid_y = centroids[label]

        # 物体の形状情報を辞書としてリストに追加
        shape_info = {
            'Label': label,
            'Left': left,
            'Top': top,
            'Width': width,
            'Height': height,
            'Area': area,
            'Centroid': (centroid_x, centroid_y)
        }
        shapes.append(shape_info)

    return shapes

def binary_threshold(image_path, threshold_value):
    # 画像をグレースケールで読み込む
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # 二値化処理
    _, binary_image = cv2.threshold(image, threshold_value, 255, cv2.THRESH_BINARY)

    return binary_image

image_path = 'C:\opencv_python\\road_sabun\\road_image\size_sample.jpg'
threshold_value = 128  # 2値化の閾値を指定（例：128）
binary_result = binary_threshold(image_path, threshold_value)
#cv2.imwrite('C:\opencv_python\\road_sabun\\road_image\size_sample.jpg',binary_result)

shape_information = get_shape_information(binary_result)

# 形状情報を表示
for shape in shape_information:
    print(shape)
