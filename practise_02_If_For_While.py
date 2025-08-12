# if => elif => else
# 類似 JS三元運算法
x = int(input('X = 輸入一個數字?'))
y = int(input('Y = 輸入一個數字?'))
print('X > Y' if x > y else ('Y > X' if y > x else 'X = Y'))

#  for
# for 變數 in range( 起始值 <若省略則為0> , 終止值 <不可省略>, 增/減量 <若省略則為+1>)
i = int(input('輸入數字'))
for x in range(i, 0, -1):
	print(' ' * (i - x + 1) + ('* ' * x))
for x in range(i + 1):
	print(' ' * (i - x + 1) + ('* ' * x))

# break 和 continue 指令皆可用於 for 或 while