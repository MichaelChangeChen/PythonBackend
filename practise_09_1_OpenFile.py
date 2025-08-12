f = open('practise_09_OpenFile.text', 'r', encoding="utf-8")
'''
r => 讀取模式預設 。
w => 寫入模式，會先清空檔案內容。
x => 只在檔案不存在時才建立新檔，並開啟為寫入模式，若檔案已存在會引發 FileExistsError 錯誤。
a => 附加模式，若檔案已存在，寫入的內容會附加至檔案尾端。
b => 二進位模式。
'''
for text in f:
	print(text)

f.close()


# 另外一種開啟檔案方式，結束不必另外關閉檔案
with open('practise_09_OpenFile.text', 'r', encoding="utf-8") as f:
	for text in f:
		print(text)

# 基本檔案、路徑功能都在這 裡面 import os
# 如果需要使用到萬用字元 *和? 就需要 這個 import glob
# 或直接： import os , glob

# os 模組
'''
getcwd() => 				取得目前程式的工作資料夾路徑
chdir() => 		path		改變程式的工作資料夾路徑
mkdir() => 		folder		建立資料夾
rmdir() => 		folder		刪除空資料夾
listdir() => 	folder		列出資料夾裡的內容
open() => 		file, mode	開啟檔案
write() => 		string		寫入內容到檔案
rename() => 	old, new	重新命名檔案
remove() => 	file		刪除檔案
stat() => 		file		取得檔案的屬性
close() => 		file		關閉檔案
path => 					取得檔案的各種屬性
system => 					執行系統命令( 等同使用 cmd 或終端機輸入指令)

'''
import os
# exists() 如果檔案存在則傳回真，否則傳回假。
if os.path.exists('practise_09_OpenFile.text'):
	with open('practise_09_OpenFile.text', 'r', encoding="utf-8") as f:
		for text in f:
			print('os--' + text)
else:
	print('沒有這個檔案')