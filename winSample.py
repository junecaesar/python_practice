# !/usr/bin/env python
# -*- coding: utf-8 -*-
#

import tkinter as tk

my_window = tk.Tk()

my_window.title("py's  window")

my_window.geometry('600x300')  # 这里的乘是小x

var = tk.StringVar()
l = tk.Label(my_window, textvariable=var, bg='green', font=('Arial', 12), width=30, height=2)

l.pack()  # Label内容content区域放置位置，自动调节尺寸
# 放置lable的方法有：1）l.pack(); 2)l.place();

on_hit = False
def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set('you hit me')
    else:
        on_hit = False
        var.set('')

b = tk.Button(my_window, text='OK', font=('Arial', 12), width=10, height=1, command=hit_me)
b.pack()

def win_exit():
    my_window.quit()

b2 = tk.Button(my_window, text='Exit', font=('Arial', 12), width=10, height=1, command=win_exit)
b2.pack()

e1 = tk.Entry(my_window, show="*****", font=('Arial', 14))   # 显示成密文形式
e2 = tk.Entry(my_window, show=None, font=('Arial', 14))  # 显示成明文形式
e1.pack()
e2.pack()

my_window.mainloop()
