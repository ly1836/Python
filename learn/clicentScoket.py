import socket


def clicentSocket():
    #创建套接字
    clicentScokets  = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    #获取IP
    host = socket.gethostname()

    #获取端口
    port = 1234

    #连接指定host、port的服务器
    clicentScokets.connect((host,port))

    #接收消息
    message = clicentScokets.recv(1024)

    clicentScokets.close()

    print(message.decode('utf-8'))

if __name__ == "__main__":
    clicentSocket()