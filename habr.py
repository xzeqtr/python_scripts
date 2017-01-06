"""
3 страницы новостей с темой, временем добавления, заголовками и ссылками на пост 
"""
import urllib.request
import re

filename = "parse.csv"
# opening the file with w+ mode truncates the file
f = open(filename, "w+")
f.close()

from lxml import html
import requests
titles = []
themes = []
posttimes = []
ids = []
url = 'https://habrahabr.ru/'
for i in range(1,4):
	page = requests.get(url + 'page' + str(i))
	tree = html.fromstring(page.content)

	titles = titles + tree.cssselect('a.post__title_link')
	themes = themes + tree.cssselect('a.post__flow')
	posttimes = posttimes + tree.cssselect('span.post__time_published')
	ids = ids + tree.xpath('//div[@class="post post_teaser shortcuts_item"]')
#tree.xpath('//div[@class="post post_teaser shortcuts_item"]')[0].get('id')
# for title in titles:
#    print(title.text_content())

import csv
with open(filename, 'a', newline='') as fp: #используем a вместо w для добавления в конец файла
    a = csv.writer(fp, delimiter=';')
    for i in range(len(titles)):
    	a.writerow([themes[i].text_content(),
    		posttimes[i].text_content().lstrip().rstrip(),
    		titles[i].text_content(), 
    		url + ids[i].attrib['id'].replace('_', '/')])

text_file = "habr.html"
# opening the file with w+ mode truncates the file
f = open(text_file, "w+")
f.close()

text_file = open("habr.html", "w")
#text_file.write("Purchase Amount: %s" % TotalAmount)
text_file.write('<table border="1">')
text_file.write('<tr>')
for i in range(len(titles)):
	text_file.write('<td>' + themes[i].text_content() + '</td>')
	text_file.write('<td>' + posttimes[i].text_content().lstrip().rstrip() + '</td>')
	text_file.write('<td>' + titles[i].text_content() + '</td>')
	text_file.write('<td>' + ids[i].attrib['id'].replace('_', '/') + '</td>')
	text_file.write('</tr>')
text_file.write('</table>')
text_file.close()
