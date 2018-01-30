import requests
from bs4 import BeautifulSoup


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

		#氣溫(白天 晚上)
		#if d.find_all('td'):
			#s = d.find_all('td','num')
			#for ss in s:
				#articles.append({'Weather' : ss.text.strip()})
				#count = count +1
	#articles.append({'num' : count})
	
		#下雨
		#if d.find_all('td','num'):
		#	k = d.find_all('td','num')
		#	for kk in k:
		#		if kk.find('img'):
		#			rain = kk.find('img')['title']
		#			#articles.append({'Rain' : rain})
		#			count = count +1
	#	articles.append({'num' : count})
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
	for i in info:
		print(i)
