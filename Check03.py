import cv2
import imutils
import numpy as np
import pytesseract

# 手動指定 tesseract.exe 路徑
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# 讀取圖片並調整大小
img = cv2.imread('test05.png', cv2.IMREAD_COLOR)
img = cv2.resize(img, (600, 400))

# 轉為灰階
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 使用雙邊濾波進行去噪
gray = cv2.bilateralFilter(gray, 13, 15, 15)

# 二值化處理，增強對比度
_, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# 邊緣檢測
edged = cv2.Canny(thresh, 30, 200)

# 找出輪廓
contours = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(contours)
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]

screenCnt = None

# 檢測車牌輪廓
for c in contours:
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.018 * peri, True)
    if len(approx) == 4:  # 如果找到四邊形輪廓
        screenCnt = approx
        break

# 如果找到輪廓，畫出輪廓框
if screenCnt is not None:
    cv2.drawContours(img, [screenCnt], -1, (0, 0, 255), 3)
else:
    print("No contour detected")
    screenCnt = None

# 創建遮罩並提取車牌區域
mask = np.zeros(gray.shape, np.uint8)
if screenCnt is not None:  # 改為檢查是否為 None
    cv2.drawContours(mask, [screenCnt], 0, 255, -1)
    new_image = cv2.bitwise_and(img, img, mask=mask)

    (x, y) = np.where(mask == 255)
    (topx, topy) = (np.min(x), np.min(y))
    (bottomx, bottomy) = (np.max(x), np.max(y))

    # 截取車牌區域
    Cropped = gray[topx:bottomx + 1, topy:bottomy + 1]

    # 使用 tesseract 辨識車牌號碼
    text = pytesseract.image_to_string(Cropped, config='--psm 11')
    print("Detected License Plate Number is:", text)
else:
    print("No license plate detected.")

# 顯示結果
img = cv2.resize(img, (500, 300))
if screenCnt is not None:  # 檢查是否有車牌區域
    Cropped = cv2.resize(Cropped, (400, 200))

cv2.imshow('Car Image', img)
if screenCnt is not None:
    cv2.imshow('Cropped Plate', Cropped)

cv2.waitKey(0)
cv2.destroyAllWindows()