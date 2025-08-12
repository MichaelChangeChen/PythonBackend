''' test02 身份證字號檢查
檢查步驟：
1. 檢查長度，須為十個字元。
2. 檢查格式，第一碼須為字母，後九碼須為數字。
3. 檢查性別，第一個數字須為 1( 男性 或 2( 女性 。
4. 計算檢查碼是否正確。


方法					作用						適用場景
isalpha()				檢查字串是否只包含字母		驗證字串內容是否為純字母
type(obj) is str		確保變數類型是 str			確保變數是字串（不推薦）
isinstance(obj, str)	確保變數是 str 或其子類型	更通用的類型檢查（推薦）
'''
setId = input('請輸入您的身分證字號：')

if not isinstance(setId[0], str):
	print('身分字號錯誤，開頭須為英文字母!')
elif not len(setId) == 10:
	print('身分字號錯誤，數需等於10碼!')
elif not setId[1] == '1' or setId[1] == '2':
	print('身分字號錯誤，第一個數字須為1或2!')
elif not setId[1:].isdigit():
	print('身分字號錯誤，後九位數須為數字!')
else:
	setId = setId[0].upper() + setId[1:]
	X = { 	'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17,
	  		'I': 34, 'J': 18, 'K': 19, 'L': 20, 'M': 21, 'N': 22, 'O': 35, 'P': 23,
			'Q': 24, 'R': 25, 'S': 26, 'T': 27, 'U': 28, 'V': 29, 'W': 32, 'X': 30,
			'Y': 31, 'Z': 33 }
	num = X[setId[0]] // 10 + (X[setId[0]] % 10) * 9

	for i in range(2, 10):
		num += int(setId[-i]) * (i - 1)
	ans = 10 - num % 10

	if ans == int(setId[-1]):
		print(f'{setId} 是正確的身分證字號')
	else:
		print(f'{setId} 不是正確的身分證字號')