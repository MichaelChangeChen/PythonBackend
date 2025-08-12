# try 測試  expect 抓錯 => 像是 JS 的 .then()  .catch()

A = [ 1, 2, 3, 4, 5, 6, 7, 8 ]

check_num = int(input('想檢查哪個數字出現過?'))

try:
	for x in A:
		print(f'{check_num}出現在索引: {A.index(check_num)}的位置!!')
		break
except:
	print('沒有出現過!!')

print(f'{A}中\n{check_num}總共出現過{A.count(check_num)}次!!')