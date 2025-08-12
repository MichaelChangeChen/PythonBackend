# Tuple 有索引
tuple01 = ( 'abc', 100, 3.14 )
print(tuple01[0])

# Tuple 是不可變物件，一旦建立，元素不能任意更改其位置和值。 可以更安全的保護資料
try:
	tuple01[0] = 'defg'
	print(tuple01[0])
except:
	print('Tuple 內容不可改變!')

# Tuple 可以轉為 List    Tuple增加程式執行速度，比 List 快
print(tuple01)
tupleToList = list(tuple01)
print(tupleToList, tuple01)

# 拆解
print(tuple01)
a, b, c = tuple01
print(f'a => {a} \nb => {b} \nc => {c}')