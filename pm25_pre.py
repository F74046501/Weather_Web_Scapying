import requests
from bs4 import BeautifulSoup


def get_articles(dom):
	soup = BeautifulSoup(dom, 'html.parser')

	articles = []
	
	#網頁的id的規律
	x = 1
	y = 1
	while(1):
		#製造出need_id,need_id就是要跟x++ y++組合起來 變成網頁上的id
		x_str = str(x)
		y_str = str(y)
		parts = ['ctl09_tdPsi',x_str,'_',y_str,'_2']
		need_id = ''.join(parts)

		divs = soup.find('td',id = need_id)
		
		#金門澎湖馬祖的預測較少 會有null
		if(divs.find('span').string!= None):
			count = int(divs.find('span').string)
			articles.append(count)
			
		if(x==3 and y==10): 
			break
		x+=1
		if(x>3):
			x=1
			y+=1
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
	page = get_web_page('https://taqm.epa.gov.tw/taqm/tw/AqiForecast.aspx')
	info = get_articles(page)
	print (info)