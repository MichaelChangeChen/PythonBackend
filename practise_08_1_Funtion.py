def printName(name):
	print(f'Hello {name}!')

setName = input('輸入名字:')
printName(setName)



# test 01
def setNameList(num):
	return [ input(f'設定{i + 1}位姓名:').capitalize() for i in range(num) ]

	# ===== 以下式尚未簡化的程式碼 =====
	# for p in range(num):
	# 	name = input(f'設定{p + 1}位姓名:')
	# 	nameList.append(name[0].upper() + name[1:])

def checkName(list):
	print('Michael 又帥又聰明，太優秀了!!!') if 'Michael' in list else print(list)

	# ===== 以下式尚未簡化的程式碼 =====
	# for name in list:
	# 	if name == 'Michael':
	# 		return print('Michael 又帥又聰明，太優秀了!!!')
	# print(list)

num = int(input('設定人數:'))
nameList = setNameList(num)
checkName(nameList)
#  ===============================================

# test 02
def textingFunc():
	x = 0
	while x != 'stop':
		t = input('打一個字，若打X就退出:').capitalize()
		if len(t) > 1:
			print('一個字而已聽不懂嗎? 若打X就退出')
			continue
		elif t == 'X':
			x = 'stop'
		else:
			x += 1
			print('* ' * x)
	print('已解鎖了我恭喜你')

textingFunc()
