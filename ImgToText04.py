# from PIL import Image
import matplotlib.pyplot as plot
import pytesseract
import numpy as np
import cv2
import time

# 手動指定 tesseract.exe 路徑
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def preprocess_image(image_path):
    """前處理影像：灰階、二值化、自適應閾值處理、高斯模糊"""
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    binary = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    blurred = cv2.GaussianBlur(binary, (5, 5), 0)
    return img, gray, binary, blurred

def find_plate(image, processed_img):
    """尋找車牌輪廓"""
    contours, _ = cv2.findContours(processed_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)  # 按面積大小排序

    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        aspect_ratio = w / h  # 計算長寬比
        if 2 < aspect_ratio < 6 and w > 50 and h > 20:  # 車牌通常是長方形
            plate_img = image[y:y+h, x:x+w]


            plot.imshow(plate_img)
            plot.axis("off")  # 隱藏座標軸
            plot.show()
            return plate_img  # 找到車牌並回傳

    return None  # 若未找到車牌

def recognize_plate(plate_img):
    """使用 OCR 辨識車牌"""
    if plate_img is None:
        return None

    # 轉換為灰階 & 調整大小
    plate_gray = cv2.cvtColor(plate_img, cv2.COLOR_BGR2GRAY)
    plate_resized = cv2.resize(plate_gray, (plate_gray.shape[1] * 2, plate_gray.shape[0] * 2), interpolation=cv2.INTER_CUBIC)

    # OCR 參數
    ocr_config = r'--oem 3 --psm 7 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    text = pytesseract.image_to_string(plate_resized, lang="eng", config=ocr_config)

    # 清理識別結果
    plate_number = "".join(filter(str.isalnum, text)).upper()
    return plate_number if len(plate_number) > 3 else None  # 過濾錯誤結果




def plate_recognition_loop(image_path, max_attempts=5):
    """迴圈執行 OCR 直到成功找到車牌號碼"""
    attempt = 0
    plate_number = None

    while attempt < max_attempts and not plate_number:
        print(f"🔍 嘗試辨識車牌 (第 {attempt + 1} 次)...")
        img, gray, binary, blurred = preprocess_image(image_path)

        # print( img, gray, binary, blurred)

        plate_img = find_plate(img, binary)
        plate_number = recognize_plate(plate_img)



        plot.imshow(img)
        plot.axis("off")  # 隱藏座標軸
        plot.show()

        attempt += 1
        time.sleep(0.5)  # 避免過快重試

    if plate_number:
        print(f"✅ 車牌號碼辨識成功: {plate_number}")
    else:
        print("❌ 無法辨識車牌，請提供更清晰的圖片。")

    return plate_number





# 測試圖片路徑
image_path = "test01.jpg"
plate_number = plate_recognition_loop(image_path)