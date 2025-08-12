# 二維清單
A = [[0] * 4 for _ in range(3)]
print(f'A List => {A}')
B = [[1] * 4 for _ in range(3)]
print(f'B List => {B}')

# 二維清單 計算 ==================
A = [[0] * 3 for _ in range(2)]
B = [[0] * 3 for _ in range(2)]
C = [[0] * 3 for _ in range(2)]

for x_ind, x in enumerate(A):
	for i_ind, i in enumerate(x):
		A[x_ind][i_ind] = int(input('設定A，請輸入數字：'))
for x_ind, x in enumerate(B):
	for i_ind, i in enumerate(x):
		B[x_ind][i_ind] = int(input('設定B，請輸入數字：'))

# enumerate() 在for loop中 可抓取index
for x_ind, x in enumerate(C):
	for i_ind, i in enumerate(x):
		C[x_ind][i_ind] = A[x_ind][i_ind] + B[x_ind][i_ind]

print(f'A => {A} \n B => {B} \n C => {C}')