import cv2
import numpy as np

def remove_small_objects(binary_image, min_area):
    # 連結成分のラベリングと統計情報の取得
    retval, labels, stats, centroids = cv2.connectedComponentsWithStats(binary_image)

    # 面積が閾値より大きい連結成分のマスクを作成
    mask = np.zeros_like(binary_image, dtype=np.uint8)
    for label in range(1, retval):
        area = stats[label, cv2.CC_STAT_AREA]
        if area >= min_area:
            mask[labels == label] = 255

    # マスクを使って小さな物体を削除
    result = cv2.bitwise_and(binary_image, binary_image, mask=mask)

    return result

'''
# 例として、二値化された画像を読み込む
binary_image = cv2.imread('C:\opencv_python\\road_sabun\\road_image\output2\mask\mask.jpg', cv2.IMREAD_GRAYSCALE)

# 小さな物体を削除する（閾値を調整してください）
min_area_threshold = 4000  # 小さな物体の面積の閾値
result_image = remove_small_objects(binary_image, min_area_threshold)

# 結果を表示
cv2.imshow('Original Binary Image', binary_image)
cv2.imshow('Filtered Binary Image', result_image)
cv2.imwrite(f'C:\opencv_python\\road_sabun\\road_image\output2\mask\zyokyo_mask.jpg',result_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

def binary_to_array(image_path):
    # 二値化画像をグレースケールで読み込む
    binary_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # 二値化画像をNumPyの配列に変換
    binary_array = np.array(binary_image)

    return binary_array

'''
# 例として、二値化された画像を配列として読み込む
binary_image_path = 'C:\opencv_python\\road_sabun\\road_image\output2\mask\zyokyo_mask1280.jpg'
binary_array = binary_to_array(binary_image_path)

# 配列をカンマ区切りの形式に変換
comma_delimited_data = binary_array.astype(int)

# カンマ区切りの配列をCSV形式で保存
np.savetxt('C:\opencv_python\\road_sabun\\road_image\output2\\array1280.csv', comma_delimited_data, delimiter=',', fmt='%d')

# 二値化画像の配列を表示
#print(binary_array)
'''


def binary_threshold_array(array, threshold):
    # 閾値を基準に配列を2値化する
    binary_array = np.where(array >= threshold, 999, 0)

    return binary_array

'''
file_path = 'C:\opencv_python\\road_sabun\\road_image\output2\\array1280.csv'
data_array = np.loadtxt(file_path, delimiter=',')

threshold_value = 10

binary_result = binary_threshold_array(data_array, threshold_value)
# 配列をカンマ区切りの形式に変換
comma_delimited_data = binary_result.astype(int)

# カンマ区切りの配列をCSV形式で保存
np.savetxt('C:\opencv_python\\road_sabun\\road_image\output2\\array1280.csv', comma_delimited_data, delimiter=',', fmt='%d')
'''
