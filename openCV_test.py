import cv2
import matplotlib.pyplot as plt  # 數值數學擴展包 NumPy的可視化操作界面


def img_download(path):
    img = cv2.imread(path)  # 圖片檔名，需要與.py的目錄在同一層
    return img


def specify_main_explorer():  # 用檔名開啟主目錄的圖片
    file_name = "image.jpg"  # 指定圖片檔名，需要與.py的目錄在同一層
    img = img_download(file_name)
    return img


def specify_explorer_pic():  # 指定圖片路徑
    file_name = "./pic/imageMiku.jpg"  # 指定目錄
    img = img_download(file_name)  # 圖片位置
    return img


def new_file_name():  # 使用輸入的變數作為影像路徑
    name = input("請輸入檔名，預設image.jpg")
    print("輸入字串 " + name)
    if name == "":  # 如果沒有輸入字元，會用image.jpg取代
        name = "image.jpg"

    return name


def show_img(img):
    # 用 matplotlib 顯示圖片
    image_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # cv2 轉成 matplotlib 格式
    plt.imshow(image_rgb)
    plt.show()
    cv2.waitKey(0)  # 等待按鍵
    cv2.destroyAllWindows()  # 關閉視窗，不加也可使用


def key_in_angle():  # 使用輸入的變數作為影像路徑
    angle = input("請輸入旋轉角度，預設15度 -順時針/+逆時針")
    file_name = "image.jpg"
    img = img_download(file_name)  # 圖片位置
    print("輸入字串 " + angle)
    if angle == "":  # 如果沒有輸入字元，會用15取代
        angle = 15
    angle = int(angle)  # 字串轉數字
    (h, w, d) = img.shape
    center = (w // 2, h // 2)

    # 第一個參數旋轉中心，第二個參數旋轉角度(-順時針/+逆時針)，第三個參數縮放比例
    M = cv2.getRotationMatrix2D(center, angle, 1.0)

    # 第三個參數變化後的圖片大小
    rotate_img = cv2.warpAffine(img, M, (w, h))
    show_img(rotate_img)

def rotate_img(img):
    (h, w, d) = img.shape
    center = (w // 2, h // 2)

    # 第一個參數旋轉中心，第二個參數旋轉角度(-順時針/+逆時針)，第三個參數縮放比例
    M = cv2.getRotationMatrix2D(center, angle, 1.0)

    # 第三個參數變化後的圖片大小
    rotate_img = cv2.warpAffine(img, M, (w, h))
    show_img(rotate_img)
