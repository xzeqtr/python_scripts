# -*- coding: utf-8 -*-
"""
3 страницы новостей с темой, временем добавления,
заголовками и ссылками на пост 
"""
import urllib.request
import re

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

""" #cvs version
filename = "parse.csv"
# opening the file with w+ mode truncates the file
f = open(filename, "w+")
f.close()
import csv
with open(filename, 'a', newline='') as fp: #используем a вместо w для добавления в конец файла
    a = csv.writer(fp, delimiter=';')
    for i in range(len(titles)):
    	a.writerow([themes[i].text_content(),
    		posttimes[i].text_content().lstrip().rstrip(),
    		titles[i].text_content(), 
    		url + ids[i].attrib['id'].replace('_', '/')])
"""

def spl(text, maxlen): #Скрипт для разбиения текста на строки
    text1 = ''  # записываем сюда новую строку
    c = 0  # счётчик символов в строке
    for i in text.split():  # проходим по каждому слову
        c += len(i)  # прибавляем длину слова
        if c > maxlen:  # если символов больше максимума
            text1 += '<br>'  # перенос строки
            c = len(i)  # счётчик равен первому слову в строке
        elif text1 != '':  # условие, чтобы не ставить пробел перед 1-м словом
            text1 += ' '  # ставим пробел после непоследнего слова в строке
            c += 1  # учитываем его в счётчике
        text1 += i  # прибавляем слово
    return text1  # возвращаем новый текст

text_file = "habr.html"
f = open(text_file, "w+") # opening the file with w+ mode truncates the file
f.close()

text_file = open("habr.html", "w")
text_file.write("""<!DOCTYPE HTML>
		<html>
		<head>
		<title>Habr short news</title>
		<meta http-equiv="Content-Type" content="text/html; charset=win-1251"/>
		<style type="text/css">
		td{color:#1476ff; background:#e0e0e0; text-decoration:none; font-size:12px; font-family: arial, serif;}
		a{color:#1476ff; background:#e0e0e0; text-decoration:none; font-size:12px; font-family: arial, serif;}
		</style>
		</head>
		""")
text_file.write('<body><table border="1"><tr>')
#text_file.write('<tr>')
for i in range(len(titles)):
	"""text_file.write('<td>' + themes[i].text_content() + '</td>')
	text_file.write('<td>' + posttimes[i].text_content().lstrip().rstrip() + '</td>')
	text_file.write('<td>' + titles[i].text_content() + '</td>')
	text_file.write('<td><a href="' + url + ids[i].attrib['id'].replace('_', '/') + '">Ссылка</a></td>')
	text_file.write('</tr>')"""
	text_file.write('<td>' + themes[i].text_content() + '<br>' + 
		posttimes[i].text_content().lstrip().rstrip() + '</td>')
	text_file.write('<td><a href="' + url + ids[i].attrib['id'].replace('_', '/') + 
		'">' + spl(titles[i].text_content(), 30) + '</a></td>')
	text_file.write('</tr>')
text_file.write('</table></body></html>')
text_file.close()
