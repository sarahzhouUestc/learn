import tkinter
# !/usr/bin/python
# -*- coding: UTF-8 -*-

root = tkinter.Tk()
root.title('应用程序窗口')  # 窗口标题
root.resizable(False, False)  # 固定窗口大小
windowWidth = 800  # 获得当前窗口宽
windowHeight = 500  # 获得当前窗口高
screenWidth, screenHeight = root.maxsize()  # 获得屏幕宽和高
geometryParam = '%dx%d+%d+%d' % (
windowWidth, windowHeight, (screenWidth - windowWidth) / 2, (screenHeight - windowHeight) / 2)
root.geometry(geometryParam)  # 设置窗口大小及偏移坐标
root.wm_attributes('-topmost', 1)  # 窗口置顶

# label文本
label_text = tkinter.Label(root, text='文本');
label_text.pack();

# label图片
img_gif = tkinter.PhotoImage(file='body.png')
label_img = tkinter.Label(root, image=img_gif)
label_img.pack()

# 不带图button
button = tkinter.Button(root, text='不带图按钮')
button.pack()

# 带图button，image
button_img_gif = tkinter.PhotoImage(file='xiaofang.png')
button_img = tkinter.Button(root, image=button_img_gif, text='带图按钮')
button_img.pack()

# 带图button，bitmap
button_bitmap = tkinter.Button(root, bitmap='error', text='带图按钮')
button_bitmap.pack()

root.mainloop()