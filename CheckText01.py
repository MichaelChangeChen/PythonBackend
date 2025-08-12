from PIL import Image
import pytesseract
import numpy as np
import cv2

# 手動指定 tesseract.exe 路徑
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
# img = Image.open('test.png')

# 讀取圖片
image = cv2.imread("test06.png")

# 轉為灰階
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

gray = cv2.GaussianBlur(gray, (3, 3), 0)

# gray = cv2.equalizeHist(gray)

gray = 255 - gray


# 使用中值濾波去噪
gray = cv2.medianBlur(gray, 3)
# Otsu 二值化法
_, binary_image = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)


# 增強對比度
alpha = 1.5 # 對比度增益
beta = 50    # 亮度增益
enhanced_image = cv2.convertScaleAbs(gray, alpha=alpha, beta=beta)



cv2.imshow('OCR_Result', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()






# -c tessedit_char_blacklist 把指定字元Ban掉，不辨識
config = r'--oem 3 --psm 4 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghjklmnopqrstuvwxyz0123456789'
boxes_data  = pytesseract.image_to_boxes(gray, lang = 'eng',output_type=pytesseract.Output.STRING, config=config)

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

ocr_str, OCR_Area_list = OCR_Area_Fuction(image,gray,boxes_data)




# data = pytesseract.image_to_data(gray, lang="eng", config=config, output_type=pytesseract.Output.DICT)
# print(data['text'])
# for i, word in enumerate(data['text']):
#     if int(data['conf'][i]) > 0:  # 只顯示信心分數大於 0 的文字
#         print(f"Detected word: {word}, Confidence: {data['conf'][i]}")




print(f'OCR_char : {ocr_str}')
print(f'OCR_Area_list : {OCR_Area_list}')





cv2.imshow('OCR_Result', image)
cv2.waitKey(0)
cv2.destroyAllWindows()



# 進行二值化處理（提高對比度）
# gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

# 將 OpenCV 的圖片格式轉換為 PIL 格式
# pil_image = Image.fromarray(gray)

# 文字識別
# text = pytesseract.image_to_string(pil_image, lang="eng")  # 指定語言（英文）
# print("識別結果：",text)

# 顯示圖片（選擇性）
# cv2.imshow("Processed Image", gray)
# cv2.waitKey(0)
# cv2.destroyAllWindows()




# lang='chi_tra' or   lang='chi_tra+eng'
# image_to_string => 回傳純字串
# image_to_data => 傳回字串,bbox,level...等等多種訊息

# f = open('file_io.text', 'w')
# f.write(text)
# f.close()