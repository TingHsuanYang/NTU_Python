class student:
	def __init__(self,name,gen):
		self.name=name
		self.gen=gen
		self.grades=[]
	def add(self,grade):
		self.grades.append(grade)
	def avg(self):
		sum=0.0
		for i in range(0,len(self.grades)):
			sum=self.grades[i]+sum
		return sum/len(self.grades)
	def fcount(self):
		count=0
		for i in range(0,len(self.grades)):
			if self.grades[i]<60:
				count+=1
		return count

def top(*students): #用不定個數寫
	students = sorted(list(students), key=lambda student: student.avg(), reverse=True)
	return students[0]

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

print ("%s同學: 性別:%s avg=%.2f, 不及格:%d " %(s1.name,s1.gen,s1.avg(),s1.fcount()))
print ("%s同學: 性別:%s avg=%.2f, 不及格:%d " %(s2.name,s2.gen,s2.avg(),s2.fcount()))
print ("%s同學: 性別:%s avg=%.2f, 不及格:%d " %(s3.name,s3.gen,s3.avg(),s3.fcount()))
print ("%s同學: 性別:%s avg=%.2f, 不及格:%d " %(s4.name,s4.gen,s4.avg(),s4.fcount()))
print ("%s同學: 性別:%s avg=%.2f, 不及格:%d " %(s5.name,s5.gen,s5.avg(),s5.fcount()))
top=top(s1,s2,s3,s4,s5)
print ("平均最高分的同學=%s , 最高分的分數%.2f "%(top.name,top.avg()))
