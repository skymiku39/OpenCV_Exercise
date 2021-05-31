import openCV_test as opencv

img = opencv.img_read("image.jpg")
gray_img = opencv.gray_img(img)


def main():
    # #存儲
    # 用檔名開啟主目錄的圖片
    # result_img = opencv.specify_main_explorer()
    # 用目錄開啟圖片
    # result_img = opencv.specify_explorer_pic()
    # 用使用者指定的目錄開啟圖片
    # new_name = opencv.key_in_file_name()
    # result_img = opencv.img_read(new_name)
    # 讀取圖片
    # opencv.img_read("image.jpg")
    # 儲存圖片
    # opencv.img_save(rotate_img, "A")

    # #圖像基本加工處理
    # 圖片轉灰階
    # result_img = opencv.gray_img(img)
    # 裁切圖片
    # result_img = opencv.cut_img(img, (100, 200), (300, 500))
    # 負片效果
    # result_img = opencv.negative_img(img)
    # 旋轉圖片
    # angle = opencv.key_in_angle()
    # result_img = opencv.rotate_img_model(img, angle)

    # #濾波方式整理
    # 均值濾波
    # result_img = opencv.averaging_blur_img(img)
    # 高斯模糊
    # result_img = opencv.gaussian_blur_img(img)
    # 中值濾波，取捲積的範圍下的中間值，除椒鹽雜訊特有效
    # result_img = opencv.median_blur_img(img)
    # 方框濾波，與均值濾波類似，可調整歸一化處理(normalize=0)
    # result_img = opencv.box_filter_img(img)
    # 雙邊濾波器，去躁同時比較可以保持邊緣訊息，但速度慢
    # result_img = opencv.bilateral_filter_img(img)

    # #邊緣檢測
    # canny
    tmp_img = opencv.gaussian_blur_img(gray_img)
    result_img = opencv.canny_img(tmp_img)

    # 單獨顯示
    # opencv.show_img(result_img)

    # 比較顯示
    opencv.show_two_img(img, result_img)

    # 比較顯示2
    # opencv.cv2.imshow("Input", img)
    # opencv.cv2.imshow("Result", result_img)
    # opencv.cv2.waitKey(0)


if __name__ == "__main__":
    main()
