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

# ==========圖片二值化
'''
模式					說明
cv2.THRESH_BINARY		超過閾值變 255，否則變 0
cv2.THRESH_BINARY_INV	反向，超過閾值變 0，否則變 255
cv2.THRESH_TRUNC		超過閾值的像素變成閾值，否則不變
cv2.THRESH_TOZERO		超過閾值的不變，低於閾值的變 0
cv2.THRESH_TOZERO_INV	反向，低於閾值的不變，超過閾值的變 0
'''
ret, img3 = cv2.threshold(img2, 200, 255, cv2.THRESH_BINARY)
plot.imshow(img2, cmap="gray")
plot.axis("off")  # 隱藏座標軸
plot.show()
print('pic--2--img3')


# 但GPT推薦只用 morphologyEx 就好了
kernel = np.ones((1, 1), np.uint8)
img3 = cv2.morphologyEx(img2, cv2.MORPH_OPEN, kernel)

plot.imshow(img3, cmap="gray")
plot.axis("off")  # 隱藏座標軸
plot.show()
print('pic--2--img3')


# 另存一張變數圖  TODO
# img3 = binary

#  ==========抓線條
img3 = cv2.adaptiveThreshold(img3, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                               cv2.THRESH_BINARY, 25, 2)

plot.imshow(img3, cmap="gray")
plot.axis("off")  # 隱藏座標軸
plot.show()
print('pic--2--img3.line')

#  ========== 模糊去雜訊 模糊去雜訊 GaussianBlur(image, (size, size), sigmaX, sigmaY) 高斯模糊
img3 = cv2.medianBlur(img3, 5)
img3 = cv2.GaussianBlur(img3, (1, 1), 0)
plot.imshow(img3, cmap="gray")
plot.axis("off")  # 隱藏座標軸
plot.show()
print('pic--2--img3.blur')






# ==========計算邊框
contour, hierarchy = cv2.findContours(img3, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# 找出最外圈模式(cv2.RETR_EXTERNAL)，方法是與上下左右pixel作對比(cv2.CHAIN_APPROX_SIMPLE)
# 詳細還有其他的模式可運用
copy_img2 = img.copy()
for cnt in contour:
	# print(cv2.contourArea(cnt))
	if cv2.contourArea(cnt) > 500:
		x, y, w, h = cv2.boundingRect(cnt)
		cv2.rectangle(copy_img2, (x, y), (x + w, y + h), (0, 255, 0), 2) #畫在原圖上
plot.imshow(copy_img2)
plot.axis("off")  # 隱藏座標軸
plot.show()
print('pic--2--copy_img2')



# ======== 找出最大邊框並切割
cnt = max(contour, key=len)
x, y, w, h = cv2.boundingRect(cnt)
print(x, y, w, h, contour)
crop_img2 = copy_img2[y + 100 : y + h -300, x +650 : x + w - 500]
plot.imshow(crop_img2, cmap="gray")
plot.axis("off")  # 隱藏座標軸
plot.show()
print('pic--2--copy_img')


#  ==========抓線條
# crop_img2 = cv2.adaptiveThreshold(crop_img2, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
#                                cv2.THRESH_BINARY, 25, 8)

# plot.imshow(crop_img2, cmap="gray")
# plot.axis("off")  # 隱藏座標軸
# plot.show()
# print('pic--2--img3.line')

# #  ========== 模糊去雜訊 模糊去雜訊 GaussianBlur(image, (size, size), sigmaX, sigmaY) 高斯模糊
# # crop_img2 = cv2.medianBlur(crop_img2, 1)
# crop_img2 = cv2.GaussianBlur(crop_img2, (1, 1), 0)
# plot.imshow(crop_img2, cmap="gray")
# plot.axis("off")  # 隱藏座標軸
# plot.show()
# print('pic--2--img3.blur')






#  ========= 改變圖片大小
# crop_x, crop_y = crop_img2.shape
# scale = 0.1 #放大 10 倍
# print(crop_x, crop_y)

# new_width = int(crop_y * scale)
# new_height = int(crop_x * scale)

# # 確保寬高為偶數，避免插值異常
# new_width = (new_width // 2) * 2
# new_height = (new_height // 2) * 2

# new_img = cv2.resize(crop_img2,( new_width, new_height), interpolation=cv2.INTER_AREA)
# plot.imshow(new_img, cmap="gray")
# plot.axis("off")  # 隱藏座標軸
# plot.show()
# print('pic--2--new_img')




# OCR 參數 (適合單行文字)
custom_config = r'--oem 3 --psm 7 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

# OCR 辨識
text = pytesseract.image_to_string(crop_img2, lang="eng", config=custom_config)

# 輸出結果
print("識別出的車牌號碼：", text)




# -c tessedit_char_blacklist 把指定字元Ban掉，不辨識
config = r'--oem 3 --psm 7 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghjklmnopqrstuvwxyz0123456789'
boxes_data  = pytesseract.image_to_boxes(crop_img2, lang = 'eng',output_type=pytesseract.Output.STRING, config=config)

threshold_value = 150
def getPuTextSize(img):
        sz = min(img.shape[:2]) / 500  # 影像短邊 / 500
        lw = max(round(sz), 1)
        font_sz = max(sz / 3, 1)
        return lw, font_sz


def OCR_Area_Fuction(image:np.ndarray, gray_image:np.ndarray, boxes_data:str) -> str :
    height, width, _ = image.shape
    ocr_str = ''
    OCR_Area_list =[] #建立OCR_Area_list 等用來儲存OCR Area用
    for box in boxes_data.splitlines():
        b = box.split()
        #取出字元，位置x,y，長高
        char, x, y, w, h = b[0], int(b[1]), int(b[2]), int(b[3]), int(b[4])
        roi = gray_image[height - h:height - y, x:w]
        # 進行二值化
        _, binary_roi = cv2.threshold(roi, threshold_value, 255, cv2.THRESH_BINARY)
        # 統計黑色像素
        black_pixel_count = roi.size - cv2.countNonZero(binary_roi)
        OCR_Area_dit = { char : black_pixel_count }
        lw , font = getPuTextSize(roi)
        # 繪製矩形框
        cv2.rectangle(image, (x, height - y), (w, height - h), (0, 255, 0), 2)
        cv2.putText(image, char, (x, height- int(y)), cv2.FONT_HERSHEY_SIMPLEX, font, (255, 0, 0), lw, cv2.LINE_AA)
        ocr_str += char
        OCR_Area_list.append(OCR_Area_dit)
    return ocr_str, OCR_Area_list

ocr_str, OCR_Area_list = OCR_Area_Fuction(img, crop_img2, boxes_data)




# data = pytesseract.image_to_data(gray, lang="eng", config=config, output_type=pytesseract.Output.DICT)
# print(data['text'])
# for i, word in enumerate(data['text']):
#     if int(data['conf'][i]) > 0:  # 只顯示信心分數大於 0 的文字
#         print(f"Detected word: {word}, Confidence: {data['conf'][i]}")




print(f'OCR_char : {ocr_str}')
print(f'OCR_Area_list : {OCR_Area_list}')