#-*-coding:UTF-8 -*-
#  EX09_04.py
#  
#   高鐵捷運站查詢範例
#  
import urllib.request
import urllib.parse
from html.parser import HTMLParser

data = urllib.parse.urlencode({'StartStation':'977abb69-413a-4ccf-a109-0272c24fd490','EndStation':'f2519629-5973-4d08-913b-479cce78a356','SearchDate':'2016/05/19','SearchTime':'21:30','SearchWay':'DepartureInMandarin','RestTime':'','EarlyOrLater':''})
data = data.encode('utf-8')
request=urllib.request.Request('http://www.thsrc.com.tw/tw/TimeTable/SearchResult',data=data,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'})
response = urllib.request.urlopen(request, data)
html = response.read().decode('utf_8')
print(html,file=open('file.html','w',encoding='utf_8'))



