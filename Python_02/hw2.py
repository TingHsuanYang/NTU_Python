import random
a=int(input('please input a number')) #輸入第一個數字
b=random.randint(1,a)

#for迴圈版本
for j in range(1,a+1): #給予y 1~使用者輸入的list
	for i in range(1,a+1) :
		print(j,'*',i,'=',i*j)

#while迴圈版本
i = 1
j = 1
while i <= a:
    while j <= a:
        print(i,'*',j,'=',i*j)
        j+=1
    i+=1
    j=1