import openCV_test as opencv
img = opencv.img_download("image.jpg")

def main():
    # 用檔名開啟主目錄的圖片
    # img = opencv.specify_main_explorer()
    # opencv.show_img(img)

    # 用目錄開啟圖片
    # img = opencv.specify_explorer_pic()
    # opencv.show_img(img)

    # 用使用者指定的目錄開啟圖片
    # new_name = opencv.new_file_name()
    # img = opencv.img_download(new_name)
    # opencv.show_img(img)

    opencv.show_img(img)



if __name__ == "__main__":
    main()