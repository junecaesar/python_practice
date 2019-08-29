#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：server.py

import socket  # 导入 socket 模块
#!/usr/bin/python
# -*- coding: UTF-8 -*-

import socket
# 建立一个服务端
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('localhost',6999)) #绑定要监听的端口
server.listen(5) #开始监听 表示可以使用五个链接排队
print("Wainting ... \n")
link_cnt=1
while True:# conn就是客户端链接过来而在服务端为其生成的一个链接实例
    conn,addr = server.accept() #等待链接,多个链接的时候就会出现问题,其实返回了两个值
    print(conn,addr)
    while True:
        try:
            data = conn.recv(1024)  #接收数据
            print(link_cnt,'msg recived:',data.decode()) #打印接收到的数据
            conn.send(data.upper()) #然后再发送数据
            if (link_cnt == 3):
                break
            link_cnt = link_cnt + 1
        except ConnectionResetError as e:
            print('关闭了正在占线的链接！')
            break
    if(link_cnt==3):
        break
conn.close()
print("Server Finished\n")