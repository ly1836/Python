
import socket

#练习服务器套接字

def conn():

    #创建socket
    serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)


    #获取本机IP
    host = socket.gethostname()

    port = 1234

    serverSocket.bind((host,port))

    #设置最大连接数
    serverSocket.listen(5)

    print("等待连接....")
    i = 0
    while True:
        i += 1
        clicentSocket,addr = serverSocket.accept()

        print("连接地址:%s" %str(addr))

        message = str("连接成功,第%d位"%(i))

        #向客户端发送消息
        clicentSocket.send(message.encode('utf-8'))

        clicentSocket.close()

if __name__ == "__main__":
    conn()