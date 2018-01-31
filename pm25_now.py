import requests
from bs4 import BeautifulSoup


def get_articles(dom):
	soup = BeautifulSoup(dom, 'xml')
	articles = []
	#print(soup)
	
	divs = soup.find_all('Data')
	#print(divs)
	for d in divs:
		big_place = d.find('county').text
		small_place = d.find('Site').text
		pm25 = d.find('PM25').text
		time = d.find('DataCreationDate').text
		articles.append({'Big_place' : big_place,
					'Small_place' : small_place,
						'Pm25' : pm25,
						'Time' : time,})
		#articles.append(big_place)
	return articles

def get_web_page(url):
	resp = requests.get(url)
	
	#success open website
	if resp.status_code != 200:#server的回覆馬 404error 200ok
		print('Invalis url:', resp.url)
		return None
	#falied to open website
	else:
		return resp.text
	
	
if __name__ == '__main__':
	page = get_web_page('http://opendata.epa.gov.tw/ws/Data/ATM00625/?$format=xml')
	info = get_articles(page)
	for i in info:
		print (i)