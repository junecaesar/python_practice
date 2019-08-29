#!/usr/bin/python
# -*- coding: UTF-8 -*-

import socket# 客户端 发送一个数据，再接收一个数据
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #声明socket类型，同时生成链接对象
client.connect(('localhost',6999)) #建立一个链接，连接到本地的6969端口
link_cnt=1
while True:
    # addr = client.accept()
    # print '连接地址：', addr
    msg = 'Msg from client:'+str(link_cnt)  #strip默认取出字符串的头尾空格
    client.send(msg.encode('utf-8'))  #发送一条信息 python3 只接收btye流
    data = client.recv(1024) #接收一个信息，并指定接收的大小 为1024字节
    print('recv:',data.decode()) #输出我接收的信息
    link_cnt = link_cnt + 1
    if (link_cnt > 3):
        break
client.close() #关闭这个链接
print("Clent Finished\n")