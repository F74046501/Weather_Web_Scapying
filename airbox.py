import requests
import json
from bs4 import BeautifulSoup


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