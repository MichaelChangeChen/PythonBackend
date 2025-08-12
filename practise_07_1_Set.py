# Set 與 Dict 類似，但 Set 沒有 key
set01 = { 'Mike', 18, '打球', 555 }
print(set01)

# 內容不可重複
set02 = { '123', 555, '123', 666 }
print(set02)

''' ===== 運算 =====
聯集 |     => 取所有，但若重複只取一次
交集 &     => 只取重複
差集 -     => 取前面的 Set 若重複則不取
互斥或 ^   => 取所有，若有重複則不取
========== '''

print(f'set01 | set02 => {set01 | set02}')
print(f'set01 & set02 => {set01 & set02}')
print(f'set01 - set02 => {set01 - set02}')
print(f'set02 - set01 => {set02 - set01}')
print(f'set01 ^ set02 => {set01 ^ set02}')

''' ===== 函式 =====
add()  => 新增
remove()  => 移除
update()  => 合併或更新 Set 物件
clear()  => 清空
========== '''

# test01
text = input('請輸入文字：')
dictBox = {}
for t in set(text):
	dictBox[t] = text.count(t)

print(dictBox)
print(f'在{text}中')

for t in dictBox.items():
	print(f'{t[0]}出現{t[1]}次')
