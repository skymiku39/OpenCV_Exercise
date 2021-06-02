import cv2
import matplotlib.pyplot as plt  # 數值數學擴展包 NumPy的可視化操作界面
import math
import numpy as np


def img_read(path):
    img = cv2.imread(path)  # 圖片檔名，需要與.py的目錄在同一層
    return img


def img_save(img, file_name):
    if file_name == "":
        file_name = "output.jpg"
    else:
        file_name = file_name + ".jpg"
    cv2.imwrite(file_name, img)  # 圖片檔名，與.py的目錄在同一層
    return


def specify_main_explorer():  # 用檔名開啟主目錄的圖片
    file_name = "image.jpg"  # 指定圖片檔名，需要與.py的目錄在同一層
    img = img_read(file_name)
    return img


def specify_explorer_pic():  # 指定圖片路徑
    file_name = "./pic/imageMiku.jpg"  # 指定目錄
    img = img_read(file_name)  # 圖片位置
    return img


def cut_img(img, l_top, r_tbm):
    img = img[l_top[1]:r_tbm[1], l_top[0]: r_tbm[0]]
    return img


def gray_img(img):  # RGB轉Gray
    # 權重比例：Gray = R * 0.299 + G * 0.587 + B * 0.114
    # 人眼在 紅綠藍權重約為 3:6:1 時較為舒適，得出公式
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return img


def key_in_file_name():  # 使用輸入的變數作為影像路徑
    name = input("請輸入檔名，預設image.jpg")
    print("輸入字串 " + name)
    if name == "":  # 如果沒有輸入字元，會用image.jpg取代
        name = "image.jpg"
    return name


def key_in_angle():  # 使用輸入的變數作為影像路徑
    angle = input("請輸入旋轉角度，預設15度 -順時針/+逆時針")
    print("輸入字串 " + angle)
    if angle == "":  # 如果沒有輸入字元，會用15取代
        angle = 15
    angle = int(angle)  # 字串轉數字
    return angle


def show_img(img):
    # 用 matplotlib 顯示圖片
    image_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # cv2 轉成 matplotlib 格式
    plt.imshow(image_rgb)
    plt.show()
    cv2.waitKey(0)  # 等待按鍵
    cv2.destroyAllWindows()  # 關閉視窗，不加也可使用


def show_two_img(img1, img2):
    # 用 matplotlib 顯示圖片
    image_rgb1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)  # cv2 轉成 matplotlib 格式
    image_rgb2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)  # cv2 轉成 matplotlib 格式

    plt.subplot(121), plt.imshow(image_rgb1), plt.title("Image1")
    plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(image_rgb2), plt.title("Image2")
    plt.xticks([]), plt.yticks([])
    plt.show()
    cv2.waitKey(0)  # 等待按鍵
    cv2.destroyAllWindows()  # 關閉視窗，不加也可使用


def show_images(images, titles, row, column):
    for i in range(len(images)):
        plt.subplot(row, column, i + 1), plt.imshow(images[i], "gray")
        plt.title(titles[i])
        plt.xticks([]), plt.yticks([])
    plt.show()
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def rotate_img(img, angle):
    (h, w, d) = img.shape
    print(h, w, d)
    center = (w // 2, h // 2)  # 找中心點

    # 參數旋轉中心(座標),第二個參數旋轉角度(-順時針/+逆時針),第三個參數縮放比例
    M = cv2.getRotationMatrix2D(center, angle, 1.0)

    # 第三個參數為變化後的圖片大小
    img = cv2.warpAffine(img, M, (w, h))
    return img, M


def shift_img(img, shift, canvas_size):  # 平移圖片
    # 平移矩阵M：[[1,0,x],[0,1,y]]
    M = np.float32([[1, 0, shift[0]], [0, 1, shift[1]]])
    img = cv2.warpAffine(img, M, canvas_size)
    return img


def rotate_img_model(img, angle):  # 旋轉圖片+調整圖片位置
    # 取得圖片座標
    (h, w, d) = img.shape
    center = (w // 2, h // 2)
    # 視中心點為原點，取得圖形相對座標
    p1 = (0 - center[0], 0 - center[1])
    p2 = (w - center[0], 0 - center[1])
    p3 = (0 - center[0], h - center[1])
    p4 = (w - center[0], h - center[1])

    # 簡化數學式
    tmp_angle = (angle * math.pi) / 180
    tmp_sin = math.sin(tmp_angle)
    tmp_cos = math.cos(tmp_angle)

    r_p1 = (int(p1[0] * tmp_cos + p1[1] * math.sin(tmp_angle) + center[0]),
            int(p1[0] * tmp_sin + p1[1] * math.cos(tmp_angle) + center[1]))
    r_p2 = (int(p2[0] * tmp_cos + p2[1] * math.sin(tmp_angle) + center[0]),
            int(p2[0] * tmp_sin + p2[1] * math.cos(tmp_angle) + center[1]))
    r_p3 = (int(p3[0] * tmp_cos + p3[1] * math.sin(tmp_angle) + center[0]),
            int(p3[0] * tmp_sin + p3[1] * math.cos(tmp_angle) + center[1]))
    r_p4 = (int(p4[0] * tmp_cos + p4[1] * math.sin(tmp_angle) + center[0]),
            int(p4[0] * tmp_sin + p4[1] * math.cos(tmp_angle) + center[1]))

    # 計算需要平移的座標
    r_min = min(r_p1[0], r_p2[0], r_p3[0], r_p4[0]), min(r_p1[1], r_p2[1], r_p3[1], r_p4[1])
    # 平移多少位置
    r_shift = (0 - r_min[0], 0 - r_min[1])
    # 計算需要修正畫布的座標
    r_max = max(r_p1[0], r_p2[0], r_p3[0], r_p4[0]), max(r_p1[1], r_p2[1], r_p3[1], r_p4[1])
    # 畫布尺寸修正
    r_canvas_size = (r_max[0] - r_min[0], r_max[1] - r_min[1])
    # 計算變換矩陣 (??)
    M = rotate_img(img, angle)[1]
    M[0, 2] = M[0, 2] + r_shift[0]
    M[1, 2] = M[1, 2] + r_shift[1]
    img = cv2.warpAffine(img, M, r_canvas_size)
    # REF http://hk.uwenku.com/question/p-sfnzzoue-mz.html
    return img


def gaussian_blur_img(img):  # 高斯模糊，減少雜訊；細節，以利分辨圖形特徵
    img = cv2.GaussianBlur(img, (5, 5), 0)
    # REF 指令說明 https://docs.opencv.org/master/d4/d86/group__imgproc__filter.html#gaabe8c836e97159a9193fb0b11ac52cf1
    # REF 找邊緣的方法 https://iter01.com/550063.html
    return img


def canny_img(img):
    img = cv2.Canny(img, 30, 180)
    return img


def averaging_blur_img(img):
    img = cv2.blur(img, (5, 5))
    return img


def negative_img(img):
    img = 255 - img
    return img


def bilateral_filter_img(img):
    img = cv2.bilateralFilter(img, 9, 75, 75)
    return img


def median_blur_img(img):
    img = cv2.medianBlur(img, 5)
    return img


def box_filter_img(img):
    img = cv2.boxFilter(img, -1, (5, 5), normalize=1)
    # REF 所有濾波參考資料 https://iter01.com/509811.html
    return img


def black_white_img(img):
    # ret?識別TF?
    # >127 =255, <127 =0 將小於閾值的灰度值設為0，其他值設為最大灰度值。
    ret, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    # >127 =0, <127 =255 將大於閾值的灰度值設為0，其他值設為最大灰度值。
    ret, thresh2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)

    # >127 =127 將大於閾值的灰度值設為閾值，小於閾值的值保持不變。
    ret, thresh3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)

    # <127 =0 將小於閾值的灰度值設為0，大於閾值的值保持不變。
    ret, thresh4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
    # >127 =0 將大於閾值的灰度值設為0，小於閾值的值保持不變。
    ret, thresh5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

    titles = ["img", "BINARY", "BINARY_INV", "TRUNC", "TOZERO", "TOZERO_INV"]
    images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
    return images, titles
