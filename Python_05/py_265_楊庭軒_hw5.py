#-*-coding:UTF-8 -*-
# 類別作業練習 EX05_hw.py
#
# 測試資料 http://140.112.31.82/wordpress/?p=216

class student:

    def __init__(self, n, g):
        self.name = n
        self.gender = g
        self.grades = []

    def add(self,g):
        self.grades.append(g)
        

    def avg(self):

        print(self.name,':',sum(self.grades)/len(self.grades))
        
    def fcount(self):
        faillist=[]
        for i in self.grades:
            if i < 60:
                faillist.append(i)
        print(self.name,'has failed', len(faillist),'subjects,and the grades are',faillist)

def top (*names):
    studentdict={}
    for n in names:
        avg=sum(n.grades)/len(n.grades)
        studentdict[n.name]=avg
    sort = [(value, key) for key, value in studentdict.items()]

    print("the student with highest average grade is",max(sort)[1]+', and the student get',max(sort)[0],'!!!')


        
s1 = student("Tom","M")
s2 = student("Jane","F")
s3 = student("John","M")
s4 = student("Ann","F")
s5 = student("Peter","M")
s1.add(80)
s1.add(90)
s1.add(55)
s1.add(77)
s1.add(40)
s2.add(58)
s2.add(87)
s3.add(100)
s3.add(80)
s4.add(40)
s4.add(55)
s5.add(60)
s5.add(60)
s1.avg()
s2.avg()
s3.avg()
s4.avg()
s5.avg()
s1.fcount()
s2.fcount()
s3.fcount()
s4.fcount()
s5.fcount()
top(s1,s2,s3,s4,s5)
print('****這堂課我缺課,所以不確定這個作業是不是要這樣做XD****')

