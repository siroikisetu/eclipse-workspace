#coding=utf-8
# 导入 socket、sys 模块
import socket
import sys

# 创建 socket 对象
sk = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM) 

# 获取本地主机名
host = socket.gethostname()
print(host)
port = 9999

# 绑定端口号
#sk.bind((host, port))
sk.bind(("127.0.0.1",port))
# 设置最大连接数，超过后排队
sk.listen(5)

while True:
    # 建立客户端连接
    print("服务器已启动")
    conn, addr = sk.accept()
    while True:
        accept_data = str(conn.recv(1024),
                          encoding="utf-8")
        print("".join(["接收内容：", accept_data, "     客户端口：", str(addr[1])]))
        if accept_data == "byebye":  # 如果接收到“byebye”则跳出循环结束和第一个客户端的通讯，开始与下一个客户端进行通讯
            break
        msg='欢迎访问菜鸟教程！'+ "\r\n"
        conn.sendall(msg.encode('utf-8')) 
    conn.close()