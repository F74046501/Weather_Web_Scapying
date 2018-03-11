import requests
import json
from bs4 import BeautifulSoup

import socket
import sys

def get_articles(dom):
	soup = BeautifulSoup(dom, 'html.parser')
	
	articles = []
	
	#地名
	d1 = soup.find_all('tr')
	for d in d1:
		if d.find('th'):
			place = d.find('th').text
			if place!='':
				articles.append({'Place' : place})
	
	#白天晚上 氣溫
	d2 = soup.find_all('td','num')
	for dd2 in d2:
		articles.append({'temperature' : dd2.text.strip()})

	#下雨程度
	d3 = soup.find_all('td','num')
	for dd3 in d3:
		if dd3.find('img'):
			k = dd3.find('img')['title']
			articles.append({'Rain' : k})
			
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
	page = get_web_page('http://www.cwb.gov.tw/V7/forecast/week/week.htm')
	info = get_articles(page)
	print(info)
	##for i in info:
	##	print (i)
	
	#tranfer list to json(這樣傳過去的json就會可以是完整的國字)
	js_info = json.dumps(info, ensure_ascii=False).encode('utf8')

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

		clientsocket.send(js_info)
		clientsocket.close()