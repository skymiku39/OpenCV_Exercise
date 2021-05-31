import openCV_test as opencv

img = opencv.img_read("image.jpg")
gray_img = opencv.gray_img(img)


def main():
    # 用檔名開啟主目錄的圖片
    # img = opencv.specify_main_explorer()
    # opencv.show_img(img)

    # 用目錄開啟圖片
    # img = opencv.specify_explorer_pic()
    # opencv.show_img(img)

    # 圖片轉灰階
    # gray_img = opencv.gray_img(img)
    # opencv.show_img(gray_img)

    # 裁切圖片
    # c_img = opencv.cut_img(img, (100, 200), (300, 500))
    # opencv.show_img(c_img)

    # 儲存圖片
    # opencv.img_save(rotate_img, "A")

    # 用使用者指定的目錄開啟圖片
    # new_name = opencv.key_in_file_name()
    # img = opencv.img_read(new_name)
    # opencv.show_img(img)

    # 旋轉圖片
    # angle = opencv.key_in_angle()
    # rotate_img = opencv.rotate_img_model(img, angle)
    # opencv.show_img(rotate_img)

    # 高斯模糊
    # opencv.show_img(gray_img)

    # 邊緣檢測(canny)
    # c_img = opencv.canny_img(gray_img)
    # opencv.show_img(c_img)

    # 均值濾波
    # blur_img = opencv.averaging_blur_img(gray_img)
    # opencv.show_img(blur_img)
    # opencv.show_two_img(img, blur_img)

    # 負片效果
    # negative_img = opencv.negative_img(img)
    # opencv.show_two_img(img, negative_img)

    # 雙邊濾波器，去躁同時比較可以保持邊緣訊息，但速度慢
    result_img = opencv.bilateral_filter_img(img)
    opencv.show_two_img(img, result_img)


if __name__ == "__main__":
    main()
