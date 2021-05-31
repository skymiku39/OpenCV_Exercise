import openCV_test as opencv

img = opencv.img_read("image.jpg")


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

    # 邊緣檢測
    # 高斯模糊
    g_img = opencv.gaussian_blur_img(img)
    opencv.show_img(g_img)


if __name__ == "__main__":
    main()
