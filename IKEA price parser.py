#python 3
import requests
from bs4 import BeautifulSoup
import re
import sys
import datetime
site = 'https://www.ikea.com'

def prog_bar(perc):
	sys.stdout.write('\r')
	sys.stdout.write("[%-50s] %d%%" % ('#'*int(perc/2), perc))
	sys.stdout.flush()

def get_cat_links():
	links = []
	html = requests.get('https://www.ikea.com/ru/ru/catalog/productsaz').text
	soup = BeautifulSoup(html, 'lxml').find_all('a', {'class':'productsAzAlphabet'})
	
	pattern = re.compile('href="(.*)">')
	for item in soup:
		links.append(pattern.findall(str(item))[0])
	links.insert(0, links[0].replace('/1/', '/0/'))
	return links

def get_full_links(link):
	html = requests.get(site+link).text
	soup = BeautifulSoup(html, 'lxml').find_all('li', {'class':'productsAzLink'})
	pattern = re.compile('href="(.*)">')
	full_links = []
	for item in soup:
		full_links.append(site+pattern.findall(str(item))[0])
	return full_links

full = []
links = get_cat_links()
print('Found %s pages in catalogue.' % len(links))
i = 0
for el in links:
	full = full + get_full_links(el)
	i= i + 100/len(links)
	prog_bar(i)
print('\nFound %s names in catalogue' % len(full))
ss = []
i=0
for el in full:
	html = requests.get(el).text.replace("\r", "").replace("\t", "").replace("\n", "").replace("\xa0","").replace("\xc4","").replace("\xd6","").replace("\xc5","")
	soup = BeautifulSoup(html, 'lxml').find_all('div', {'class':'productDetails'})
	for item in soup:
		if item.find('span', {'class':'productTitle floatLeft'}) == None:
			continue
		name = item.find('span', {'class':'productTitle floatLeft'}).contents[0]
		if item.find('span', {'class':'productDesp'}) == None:
			continue
		if item.find('span', {'class':'productDesp'}).contents == []:
			desc = ''
		else:
			desc = item.find('span', {'class':'productDesp'}).contents[0]
		price = item.find('span', {'class':'price regularPrice'}).contents[0].replace('.–','')
		ss.append([name,desc,price])
	i= i + 100/len(full)
	prog_bar(i)
print('\nProcessed %s goods ' % len(ss))
fname = 'IKEA_price_'+datetime.datetime.today().strftime("%Y%m%d")+'.csv'
with open(fname,'w') as f:
	for el in ss:
		f.write('%s\n' % ';'.join(el))
print('and saved to %s' % fname)
input('Press enter to exit')