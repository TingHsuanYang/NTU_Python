#X戰警：天啟 X-MEN: APOCALYPSE
while True:
        
    url=(input('please input the number:'))
    import urllib.request
    from html.parser import HTMLParser
    response=urllib.request.urlopen('https://tw.movies.yahoo.com/movieinfo_main.html/id='+url)
    html=response.read().decode('utf_8')
    response.close()

    #需要抓取的資訊如下:
    #電影名稱 (中英)
    #上映日期
    #類 型
    #片 長
    #導 演
    #演 員
    #發行公司
    #官方網站
    #劇情介紹

    class myparser(HTMLParser):

        def __init__(self):
            HTMLParser.__init__(self)
            self.isNumber=0
            self.movietitle_c = []
            self.movietitle_e = []
            self.date = []
            self.type = []
            self.length = []
            self.director = []
            self.actor = []
            self.company = []
            self.website = []
            self.plot = []

        
        def handle_data(self, data):
            if self.isNumber ==1:
                if self.tag=='h4':
                    self.movietitle_c.append(data)
                if self.tag=='h5':
                    self.movietitle_e.append(data)
                if (220<=self.getpos()[0]<=220) and self.attr == [('class', 'dta')]:
                    self.date.append(data)
                if (221<=self.getpos()[0]<=221) and self.tag == 'a':
                    self.type.append(data)
                if (222<=self.getpos()[0]<=222) and self.attr == [('class', 'dta')]:
                    self.length.append(data)
                if (223<=self.getpos()[0]<=223) and self.tag == 'a':
                    self.director.append(data)
                if (224<=self.getpos()[0]<=224) and (self.tag=='a' or self.attr == [('class', 'dta')]):
                    self.actor.append(data)
                if (225<=self.getpos()[0]<=225) and self.attr == [('class', 'dta')]:
                    self.company.append(data)
                if (226<=self.getpos()[0]<=226) and (self.tag=='a' or self.attr == [('class', 'dta')]):
                    self.website.append(data)
                if self.attr == [('class', 'text full')]:
                    self.plot.append(data)
                    
            self.isNumber=0
                        

        def handle_starttag(self, tag, attrs):
            if (218<=self.getpos()[0]<=226) and (tag=='h4'or tag == 'h5' or tag == 'span' or tag == 'a' ) :
                self.isNumber=1
                self.tag=tag
                self.attr=attrs
            if (226<self.getpos()[0]) and (tag=='div' and attrs == [('class','text full')]) :
                self.isNumber=1
                self.tag=tag
                self.attr=attrs


        def handle_endtag(self,tag):
            if (226<self.getpos()[0]) and tag=='br' :
                self.isNumber=1
                self.tag=tag
               
            
    Parser = myparser() 
    Parser.feed(html)
    filename=url+'.txt'


    print('電影名稱:',Parser.movietitle_c[0],Parser.movietitle_e[0],'\n上映日期:',Parser.date[0],'\n類 型:',','.join(Parser.type),'\n片 長:',Parser.length[0],'\n導 演:',','.join(Parser.director),'\n演 員:',','.join(Parser.actor),'\n發行公司:',Parser.company[0],'\n官方網站:',Parser.website[0],'\n劇情介紹:\n',','.join(Parser.plot),file=open(filename,'w',encoding='utf_8'))

