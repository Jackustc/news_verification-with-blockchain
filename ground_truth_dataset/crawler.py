#coding:utf-8
import csv
from bs4 import BeautifulSoup
import requests

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'}

label = ['label']
text = ['content']
time = ['pub_time']

for i in range(744):
    url = 'http://www.politifact.com/truth-o-meter/statements/?page={}'.format(i)
    htm = requests.get(url,headers=headers, timeout = 80000)
    soup = BeautifulSoup(htm.text,'html.parser')
    for line in soup.findAll('div',{'class:','scoretable__item'}):
        content = BeautifulSoup(str(line),'html.parser')
        if len(content.findAll('div',{'class:','meter'}))>0:
            label_text = content.findAll('div',{'class:','meter'})[0]
            label_content = BeautifulSoup(str(label_text),'html.parser')
            label_result = label_content.find('img').get('alt')
        else: label_result = 'not exist'
        label.append(label_result.strip())
        if len(content.findAll('p',{'class:','statement__text'}))>0:
            news_text = content.findAll('p',{'class:','statement__text'})[0]
            news_content = BeautifulSoup(str(news_text),'html.parser')
            news_result = news_content.find('a').string
        else: news_result = 'not exist'
        text.append(news_result.strip())
        if len(content.findAll('p',{'class:','statement__edition'}))>0:
            time_text = content.findAll('p',{'class:','statement__edition'})[0]
            time_content = BeautifulSoup(str(time_text),'html.parser')
            time_result = time_content.find('span').string
        else: time_result = 'not exist'
        time.append(time_result.strip())
        print(label_result.strip(),news_result.strip(),time_result.strip())
with open('politifact.csv','w',encoding='utf-8',newline='') as w:
    w_t = csv.writer(w)
    for i in range(len(label)):
        row = [label[i],text[i],time[i]]
        w_t.writerow(row)
