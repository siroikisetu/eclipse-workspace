#coding=utf-8
# 导入 socket、sys 模块
import socket
import sys
import os
'''
# 创建 socket 对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# 获取本地主机名
host = socket.gethostname() 
print(host)
# 设置端口好
port = 9999

# 连接服务，指定主机和端口
s.connect((host, port))
'''
sk = socket.socket()
sk.connect(("10.60.63.53", 9999))  # 主动初始化与服务器端的连接
while True:
    send_data = input("输入发送内容:")
    sk.sendall(bytes(send_data, encoding="utf-8"))
    if send_data == "byebye":
        break
    accept_data = str(sk.recv(1024), encoding="utf-8")
    print("".join(("接收内容：", accept_data)))

sk.close()

os.system("pause")