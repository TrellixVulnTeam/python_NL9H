from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
html=urlopen('https://en.wikipedia.org/wiki/Kevin_Bacon')
bs0bj=BeautifulSoup(html,'lxml')
for link in bs0bj.find('div',{'id':'bodyContent'}).findAll('a',href=re.compile('^(/wiki/)((?!:).)*$')):
	if 'href' in link.attrs:
		print(link.attrs['href'])