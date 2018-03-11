import json
import socket
import sys

if __name__ == '__main__':
	info = []
	info.append({'Rain':'haha'})
	
	#tranfer list to json
	js_info = json.dumps(info)
	
	# 创建 socket 对象
	serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

	# 获取本地主机名
	host = '192.168.137.246'

	port = 9999

	# 绑定端口
	serversocket.bind((host, port))

	# 设置最大连接数，超过后排队
	serversocket.listen(5)
	serversocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

	while True:
		# 建立客户端连接
		clientsocket,addr = serversocket.accept()

		print("连接地址: %s" % str(addr))

		clientsocket.send(js_info.encode('utf-8'))
		clientsocket.close()