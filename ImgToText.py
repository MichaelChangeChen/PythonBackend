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

# =========== alpha => 對比， beta => 亮度
alpha = 0.5
beta = 0
adjusted = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)
# opencv 內並沒有字帶調整對比降噪的函數，因此使用纖性來提升對比,降低升高亮度
plot.imshow(cv2.cvtColor(adjusted, cv2.COLOR_BGR2RGB))  # OpenCV 預設是 BGR 需轉成 RGB
plot.axis("off")  # 隱藏座標軸
plot.show()
print('pic--1--adjusted')

# ==========轉成灰階 255白 - 0黑
img2 = cv2.cvtColor(adjusted, cv2.COLOR_RGB2GRAY)
plot.imshow(img2, cmap="gray")
plot.axis("off")  # 隱藏座標軸
plot.show()
print('pic--2--img2')

# ==========膨脹與腐蝕 去除黑白點
''' ===先膨脹再腐蝕的效果===
這種組合叫做「開運算」(Opening Operation)：
先膨脹，擴大目標物，連接斷裂區域。
再腐蝕，去除多餘雜訊，平滑邊界。
效果：有效去除雜訊、平滑邊界、修復小型間隙。
'''
kernel = np.ones((5, 5), np.uint8)
binary = cv2.dilate(img2, kernel, iterations=4) #膨脹
''' 膨脹:
擴大白色區域，減少黑色區域。
填補小孔洞，消除細小雜訊。
強化物件邊界，適用於需要連接斷開的區域。

cv2.dilate(src, kernel, iterations)
src => 輸入圖像
kernel => 結構元素（用於決定操作範圍）
iterations => 膨脹的次數，次數越多效果越明顯
'''
plot.imshow(binary, cmap="gray")
plot.axis("off")  # 隱藏座標軸
plot.show()
print('pic--2--binary')


binary = cv2.erode(binary, kernel, iterations=2) #腐蝕
''' 腐蝕:
縮小白色區域，擴大黑色區域。
去除細小噪點，消除孤立像素。
分割物件，適用於連接過於緊密的區域。
cv2.erode(src, kernel, iterations)
src => 輸入圖像
kernel => 結構元素（用於決定操作範圍）
iterations => 腐蝕的次數，次數越多效果越明顯
'''
plot.imshow(binary, cmap="gray")
plot.axis("off")  # 隱藏座標軸
plot.show()
print('pic--2--binary')


#  ==========抓線條
binary = cv2.adaptiveThreshold(binary, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                               cv2.THRESH_BINARY, 25, 2)

plot.imshow(binary, cmap="gray")
plot.axis("off")  # 隱藏座標軸
plot.show()
print('pic--2--binary')



#  ========== 模糊去雜訊
binary = cv2.GaussianBlur(binary, (5, 5), 1, 1)
plot.imshow(binary, cmap="gray")
plot.axis("off")  # 隱藏座標軸
plot.show()
print('pic--2--binary')
# 模糊去雜訊 GaussianBlur(image, (size, size), sigmaX, sigmaY) 高斯模糊
# src：輸入圖像（通常是灰階圖）
# ksize：高斯核的大小（寬, 高），必須是奇數，如 (3,3), (5,5), (7,7)
# sigmaX：X方向的標準差（數值越大模糊程度越高）
# sigmaY（可選）：Y方向的標準差，若設為 0，則會自動與 sigmaX 相同
# borderType（可選）：邊界處理方式，默認為 cv2.BORDER_DEFAULT

# ==========計算邊框
contour, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# 找出最外圈模式(cv2.RETR_EXTERNAL)，方法是與上下左右pixel作對比(cv2.CHAIN_APPROX_SIMPLE)
# 詳細還有其他的模式可運用
copy_img = img.copy()
for cnt in contour:
	# print(cv2.contourArea(cnt))
	if cv2.contourArea(cnt) > 500:
		x, y, w, h = cv2.boundingRect(cnt)
		cv2.rectangle(copy_img, (x, y), (x + w, y + h), (0, 255, 0), 2) #畫在原圖上
plot.imshow(copy_img)
plot.axis("off")  # 隱藏座標軸
plot.show()
print('pic--2--copy_img')

# ======== 找出最大邊框並切割
cnt = max(contour, key=len)
x, y, w, h = cv2.boundingRect(cnt)
crop_img = copy_img[y + 100 : y + h - 100, x + 200 : x + w - 250]
plot.imshow(crop_img, cmap="gray")
plot.axis("off")  # 隱藏座標軸
plot.show()
print('pic--2--copy_img')

#  ========= 改變圖片大小
crop_x, crop_y = crop_img.shape
print(crop_x, crop_y)
new_img = cv2.resize(crop_img, (int(crop_y / 10), int(crop_x / 10)))
plot.imshow(new_img, cmap="gray")
plot.axis("off")  # 隱藏座標軸
plot.show()
print('pic--2--new_img')


