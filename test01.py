# -*- coding: UTF-8 -*-
from tkinter import *
import tensorflow as tf


def center_window(root, width, height):
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    root.geometry(size)

class GUI:
    """给每个组件都命名是为了以后迭代方便"""
    def __init__(self, root):
        # 创建双向链表
        data = ''
        data.encode("gbk")
        root.title(data)
        # 设置窗口大小
        center_window(root, 600, 400)
        root.maxsize(1200, 800)
        root.minsize(300, 240)
        icon = PhotoImage(file='xiaofang.png')
        root.tk.call('wm', 'iconphoto', root._w, icon)
        # root.iconbitmap('@./xiaofang.xbm')


root = Tk()
test = GUI(root)
root.mainloop()