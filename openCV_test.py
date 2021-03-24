import cv2


def show_main_explorer():  # 載入並顯示圖片
    img = cv2.imread("image.jpg")  # 圖片檔名，需要與.py的目錄在同一層
    cv2.imshow("show_main_explorer", img)  # 顯示圖片
    cv2.waitKey(0)  # 等待按鍵
    cv2.destroyAllWindows()  # 關閉視窗，不加也可使用


def show_pic_explorer_pic():  # 指定目錄並顯示圖片
    file_name = "./pic/imageMiku.jpg"  # 指定目錄
    img = cv2.imread(file_name)  # 圖片位置
    cv2.imshow("show_pic_explorer_pic", img)  # 顯示圖片
    cv2.waitKey(0)  # 等待按鍵
    cv2.destroyAllWindows()  # 關閉視窗，不加也可使用

