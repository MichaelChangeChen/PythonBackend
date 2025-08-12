# Dict 有 key 及 value
dict01 = { 'age': '18', 'name': 'Mike' }
print(f'{dict01['name']}今年{dict01['age']}歲')

# 內容可改變
dict01['age'] = 21
print(f'{dict01['name']}後年就{dict01['age']}歲了')

# 新增
dict01['hobby'] = '打籃球'
print(f'{dict01['name']}喜歡{dict01['hobby']}')

# 刪除
del dict01['hobby']
try:
	print(dict01['hobby'])
except:
	print('找不到(dict01[hobby])')


'''
==== 常用函式 ====
clear() => 清空 dict 物件
copy() => 複製 dict 物件
get() => 以 key 來搜尋資料
pop() => 移除元素
update() => 合併或更新 dict 物件
dict01.keys() => dict_keys(['age', 'name', 'hobby'])
dict01.clear() => dict_values([21, 'Mike', '打籃球'])
'''
print(dict01.values())

# test01
a = 'ABCDEFGHIJKLOMOPQRSTUVWXYZ'
b = 'DEFGHIJKLOMOPQRSTUVWXYZABC'
# 將 a 和 b 打包建立成字典
print(zip(a,b))
print(dict(zip(a,b)))
code = dict(zip(a,b))
# upper() 轉為大寫
text = input('請輸入字串:').upper()
textout = ''
print(text)
for i in text:
	textout += code[i]
print(textout)