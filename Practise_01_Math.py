w, x, y, z = map(int, input('請輸入四個數值，以空白分隔：').split())

# 計算二次方
w = w**2
x = x**2
y = pow(y, 2)
z = pow(z, 2)

print(f'w = {w}, x = {x}, y = {y}, z = {z}')

# use Math
import math
x = int(input('x = 給個數字吧：'))
print(f'{x}的log = {math.log(x)}')
print(f'{x}的開根號 = {math.sqrt(x)}')
print(f'{x} sin = {math.sin(x * math.pi)}')