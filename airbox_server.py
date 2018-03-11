import requests
import json
from bs4 import BeautifulSoup

import socket
import sys

def get_articles(dom):
	articles = []
	
	html = json.loads(dom)
	how_long = len(html['feeds'])

	count = 0
	while(1):
		if count==how_long:
			break
		lon = html['feeds'][count]['gps_lon']
		lat = html['feeds'][count]['gps_lat']
		site = html['feeds'][count]['SiteName']
		date = html['feeds'][count]['date']
		time = html['feeds'][count]['time']
		articles.append({
			'gps_lon' : lon,
			'gps_lat' : lat,
			'site' : site,
			'date' : date,
			'time' : time,
		})
		count = count +1 
	return articles

def get_web_page(url):
	resp = requests.get(url)
	resp.encoding = 'utf-8'
	
	#success open website
	if resp.status_code != 200:#server的回覆馬 404error 200ok
		print('Invalis url:', resp.url)
		return None
	#falied to open website
	else:
		return resp.text
	
	
if __name__ == '__main__':
	page = get_web_page('https://pm25.lass-net.org/data/last-all-airbox.json')
	info = get_articles(page)
	for i in info:
		print (i)
	
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