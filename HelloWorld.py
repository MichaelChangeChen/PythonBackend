'''wewq
eqwewqe
eqweqwe 註解啦'''

#都用大寫
a = True
b = False

#變數轉換
a = str(a)
print(type(a), type(b))

'''
python的list 有點像是 js的Array
python的dictionary 有點像是 js的Object
list => []		有序，具備索引，內容與長度可變，通過索引進行查找。
tuple => ()		有序，將多樣的物件集合到一起，不能修改，通過索引進行查找。
dict => {}		是一組'key'和'value'的組合，通過'key'進行查找，沒有順序， 'key'不能重複。
set => () or {}	無序，元素只出現一次，自動去除重複。
'''

'''
運算子
+	加 => a + b
-	減 => a - b
*	乘 => a * b
/	除 => a / b
//	整除(向下取整數) => a // b
%	取餘數 => a % b
**	指數 => a ** b
'''

'''
關係運算子
==	相等 a == b
!=	不相等 a != b
>	大於 a > b
>=	大於等於 a >= b
<	小於 a < b
<=	小於等於 a <= b
'''

'''
位元運算子
& and => a & b
| or => a | b
^ xor => a ^ b
~ not => ~ a
<< 位元左移 => a << 2
>> 位元右移 => a >> 2
'''

#成員運算子
a = 'aaa'
setList = [ 'aaa', 'bbb', 'ccc' ]
print(a in setList)
print(a not in setList)

#跳脫字元
print('\\')
print('\'')
print('\"')
print('abc\ndef')
print('\a')
print('abc\tdef')
print('abc	\b	def')
print('abc	\f	def')

#基本輸出指令
name = 'Michael Change'
age = 18
print(f'我是{ name }，今年{ age }歲')
print('我是%s，今年%d歲' % (name, age))
'''
%d =>	整數
%f =>	浮點數
%x =>	16進為整數
%X =>	大寫16進為整數
%o =>	8進為整數
%s =>	字串
%e =>	科學記號e
%E =>	科學記號大寫E
'''

#輸入函數 input()
tel = input('你的電話幾號?')
print(f'他的電話是: { tel }')
print(type(tel))
tel = int(input('你的電話幾號?')) #轉化成int
print(type(tel))

# for test 001
x = int(input('2x - 4 = 8, 請問x為多少?'))
while x != 6:
	print('答錯囉')
	x = int(input('在一次?'))

print('我恭喜你')

# for test 002
import random
guess_num = random.randint(0, 100)
print('我們來玩【猜數字】')
set_num = int(input('猜一個數字(0 ~ 100):'))
max_num = 100
min_num = 0
guess_time = 0

def check(set_num, max_num, min_num):
	while set_num == max_num or set_num == min_num:
		print('不能選重複數字唷!')
		set_num = int(input(f'再猜一個數字({min_num} ~ {max_num}):'))
	while set_num > max_num or set_num < min_num:
		print(f'不能小於{min_num}或大於{max_num}唷!')
		set_num = int(input(f'再猜一個數字({min_num} ~ {max_num}):'))
	return set_num

while guess_num != set_num:
	set_num = check(set_num, max_num, min_num)
	if guess_num < set_num:
		if max_num > set_num:
			max_num = set_num
		print(f'再小一點喔!')
		guess_time += 1
		set_num = int(input(f'再猜一個數字({min_num} ~ {set_num}):'))
		set_num = check(set_num, max_num, min_num)

	if guess_num > set_num:
		min_num = set_num
		print(f'再大一點喔!')
		guess_time += 1
		set_num = int(input(f'再猜一個數字({set_num} ~ {max_num}):'))
		set_num = check(set_num, max_num, min_num)

print(f'猜{guess_time}次就中了，我恭喜你')

# ============================

