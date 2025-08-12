# 以 tk 取代 tkinter
import tkinter as tk
'''
或是用下面方法:  此方式之後可省略套件名稱
from tkinter import *
win = Tk()
win.mainloop()
'''


# 建立視窗
win = tk.Tk()
win.title('測試用而已啦')
win.geometry('500x300')
label = tk.Label(	win,
					text='我是LABEL',
					bg='blue',
					fg='white',
					font=('微軟正黑體', 16),
					padx=10,
					pady=10)
# 配置 label 到 win
label.pack(side='top')

def newWord():
	if label['text'] != 'Michael超帥的啦!!':
		label['text'] = 'Michael超帥的啦!!'
		label['bg'] = 'red'
		label['font'] = ('微軟正黑體', 24)
	else:
		label['text'] = '我是LABEL'
		label['bg'] = 'blue'
		label['font'] = ('微軟正黑體', 16)

btn = tk.Button(	win,
			 		text='改變Label內容',
					command = lambda:newWord(),
					padx=10,
					pady=10).pack()


# 執行視窗直到關閉
win.mainloop()

'''  基礎元件：
標籤		Label
按鈕		Button
文字方塊	Entry
文字區域 	Text
捲軸 		Scrollbar
核取按鈕 	Checkbutton
選項按鈕 	Radiobutton
圖形 		Photoimage
功能表 		Menu
'''