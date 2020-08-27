import socket
import time
HOST = '192.168.60.66'    # Cấu hình address server
PORT = 8000             # Cấu hình Port sử dụng
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Cấu hình socket
s.connect((HOST, PORT))
def  main():
    while True:
        data = s.recv(1024) # Đọc dữ liệu server trả về
        dataload = repr(data)
        dataprint = dataload[2] + dataload[3]
        print('Server Respone: ', repr(data) + str(dataprint))
        toaster = ToastNotifier()
        toaster.show_toast(str(dataprint), duration=10)
if "__main__" == __name__:
    main()
