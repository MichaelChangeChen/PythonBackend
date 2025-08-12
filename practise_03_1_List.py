a = [ 1, 3, 5, 7, 9, 11 ]
print(a[0:3])
print(a[:3])
print(a[3:])
print(a[::2])
print(a[::-1]) #反轉

# 插入
a[0:3] = 66, 77, 88, 99
print(a)

# 將奇偶數分離：
a = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
even_num = a[1::2]
odd_num = a[0::2]
print(f'偶數 {even_num}, 奇數 {odd_num}')

'''
insert() => 插入新元素
append() => 附加新元素
count(X) => 計算X在List出現次數
pop() => 移除最後一個元素
remove() => 移除元素(指定)
reverse() => 倒轉順序
=====================
sort() => 排序
sorted() => 排序(原清單內容不受影響)
a = sorted(b)
=====================
max() => 最大
min() => 最小
sum() => 總和
=====================
len() => 長度
index(x) => 找索引
'''
b = [ 1, 9, 7, 25, 44, 2, 66, 34, 5 ]
b.sort()
print(b, len(b))

# List 運算
a = [ 1, 2, 3 ]
b = [ 4, 5, 6 ]
print(f'相加後 {a + b}')
print(f'相乘後 {a * 3}')

# ====== test01
A = []
for x in range(10):
	A.append(int(input(f'請輸入第{x + 1}個數字：')))

check_num = int(input('想檢查哪個數字出現過?'))

for x in range(len(A)):
	if A[x] == check_num:
		print(f'{check_num}出現位置在{x}')

if A.count(check_num) == 0:
	print('沒有出現過!!')
else:
	print(f'{A}中\n{check_num}總共出現過{A.count(check_num)}次!!')
#  ======================================