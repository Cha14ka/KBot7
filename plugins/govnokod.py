import random, requests, re
from bs4 import BeautifulSoup as bs
from plugins.utils import *

class main:
	level = 1
	keywords = ['говнокод','govnokod','гв']
	def execute(self, msg):
		try:
			index = requests.get('http://govnokod.ru/'+msg['user_text'].lower()).text
		except:
			apisay('Такого языка не существует :(',msg['toho'])
			return 0
		index = bs(index,'html.parser')
		index = index.find_all('ul','pagination numbered')[0].find_all('a')
		max = int(index[0].text)+1
		min = int(index[-1].text)
		randnum = str(random.randint(min,max))
		index = requests.get('http://govnokod.ru/'+msg['user_text'].lower()+'?page='+randnum).text
		index = bs(index,'html.parser')
		code = re.sub('(\\n\d*\\n)','',random.choice(index.find_all('li','hentry')).find('div').text).replace('  ', '&#8195;')
		description = index.find_all('li','hentry')[0].find('p','description').text

		apisay(code+'-'*30+description,msg['toho'])