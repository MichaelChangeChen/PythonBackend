# from PIL import Image
import matplotlib.pyplot as plot
import pytesseract
import numpy as np
import cv2

''' ====辨識原則====
1. 黑底白字,字型清晰
2. 字體最小12號字，也不可過大
3. 去除文字底線
4. 圖片解析度高於 300 DPI
5. 去除圖片光影
6. 最好二值化,去噪
===================='''

# 手動指定 tesseract.exe 路徑
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

''' pytesseract 其中重要的function:
1. image_to_string 回傳純文字串
2. image_to_data 傳回字串,bbox,level...等等訊息

image_to_data 參數:
image_to_data(image, lang=None, config='', nice=0, output_type=Output.STRING, timeout=0, pandas_config=None)
1. image 傳入圖片可以是 Pillow, opencv, numpy 圖片
2. lang 語言默認為英文(eng)，另有簡體中文(chi_sim)，繁體中文(chi_tra)...  等等
3. config 設定辨識模式,辨識白名單,辨識方式等等
4. 回傳數據類型，默認為string，output_type=pytesseract.Output.DICT 可以回傳dict格式
'''

# ===========讀取圖片
img = cv2.imread("test01.jpg")

# 轉換為灰階
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 自適應二值化
binary = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

# 去除小噪點 (形態學開運算)
kernel = np.ones((2, 2), np.uint8)
clean = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)

plot.imshow(clean, cmap="gray")
plot.axis("off")
plot.show()

#  ========== 模糊去雜訊 模糊去雜訊 GaussianBlur(image, (size, size), sigmaX, sigmaY) 高斯模糊
img3 = cv2.medianBlur(clean, 5)
img3 = cv2.GaussianBlur(img3, (1, 1), 0)
plot.imshow(img3, cmap="gray")
plot.axis("off")  # 隱藏座標軸
plot.show()
print('img3.blur')





# 找輪廓 (車牌定位)
contours, _ = cv2.findContours(clean, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
roi = None
if contours:
    # 找到最大面積的輪廓（假設為車牌）
    x, y, w, h = cv2.boundingRect(max(contours, key=cv2.contourArea))

    # **適應小車牌圖片的放大**
    if w < 100 or h < 40:  # 車牌太小的情況
        scale_factor = 2.5  # 放大倍率
        w, h = int(w * scale_factor), int(h * scale_factor)
        print('small')


    print('found')
    # 裁剪並調整大小 (放大車牌區域)
    roi = cv2.resize(clean[y:y+h, x:x+w], (w, h), interpolation=cv2.INTER_CUBIC)
else:
    print('not found')
    roi = clean  # 若找不到輪廓，使用原始二值化影像

# 顯示處理後的車牌區域
plot.imshow(roi, cmap="gray")
plot.axis("off")
plot.show()

# OCR 參數 (適合單行文字)
custom_config = r'--oem 3 --psm 7 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

# OCR 辨識
text = pytesseract.image_to_string(roi, lang="eng", config=custom_config)

# 輸出結果
print("識別出的車牌號碼：", text.strip())