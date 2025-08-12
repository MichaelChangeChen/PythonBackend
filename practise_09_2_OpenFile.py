import os, glob

# 建立目錄
path = 'textFolder'
new_path = 'textFolder_2'
if os.path.exists(path):
	print(path + '已存在')
	os.rename(path, new_path)
	print('已重新命名' + new_path)
elif os.path.exists(new_path):
	os.rmdir(new_path)
	print(new_path + '已刪除')
else:
	os.mkdir(path)
	print(path + '已建立')


print('============================')
pyPath = 'C:/Users/W00/Desktop/learnPython/'
for file in os.listdir(pyPath):
	print(file)

print('============================')
fname = '*.text'
# 使用萬用字元 * 就用 glob
print(pyPath + fname)
for file in glob.glob(pyPath + fname):
	print(file)