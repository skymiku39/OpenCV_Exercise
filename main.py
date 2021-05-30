import openCV_test as opencv


def main():
    # opencv.show_main_explorer()
    # opencv.show_pic_explorer_pic()
    #
    # key_in_file_name = input("請輸入檔名，預設image.jpg")
    # opencv.key_in_variable(key_in_file_name)
    #

    key_in_angle = input("請輸入旋轉角度，預設15度 -順時針/+逆時針")
    opencv.key_in_angle(key_in_angle)


if __name__ == "__main__":
    main()
