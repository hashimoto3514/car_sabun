import numpy as np
import cv2
def check_passage_availability(field_data, object_width):
    # フィールドデータのサイズ
    field_height, field_width = field_data.shape

    # 全列で連続した80個の0が存在するかをチェック
    for i in range(field_width):
        consecutive_zeros = 0
        max = 0
        for j in range(field_height):
            if field_data[j, i] == 0:
                consecutive_zeros += 1
                if max < consecutive_zeros:
                    max = consecutive_zeros
            else:
                consecutive_zeros = 0

        if max < object_width:
            return False

    return True

'''
# CSVファイルからフィールドデータを読み込む（例として仮のデータを使用）
file_path = 'C:\opencv_python\\road_sabun\\road_image\output2\\array776.csv'
field_data = np.loadtxt(file_path, delimiter=',')

# 画像を読み込む
image = cv2.imread('C:\opencv_python\\road_sabun\\road_image\output2\mask\zyokyo_mask776.jpg', cv2.IMREAD_GRAYSCALE)

# 物体の幅（80）を指定して通り抜けの可否を判定
object_width = 80
result = check_passage_availability(field_data, object_width)

if result:
    print("通り抜け可能です。")
    text = "Success!"
    cv2.putText(image,text,(500,50),cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 1)
    # 書き込まれた画像を表示
    cv2.imshow('Image with Text', image)
    cv2.waitKey(0)
    cv2.imwrite(f'C:\opencv_python\\road_sabun\\road_image\output2\mask\\result776.jpg',image)
    cv2.destroyAllWindows()
    



else:
    print("通り抜け不可能です。")
    text = "Failure!"
    cv2.putText(image,text,(500,50),cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 1)
    # 書き込まれた画像を表示
    cv2.imshow('Image with Text', image)
    cv2.waitKey(0)
    cv2.imwrite(f'C:\opencv_python\\road_sabun\\road_image\output2\mask\\result776.jpg',image)
    cv2.destroyAllWindows()

'''