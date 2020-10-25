#分別用for，while迴圈各寫⼀個nXn的乘法表 程式可以讀取使用者輸入的值 n, n>1
#Q1
print('Q1 for迴圈乘法表')
num=int(input('n='))

for i in range(1,num+1):
    for j in range(1,num+1):
        print(str(i)+"X"+str(j)+"="+str(i*j))




#Q2
print('Q2 while迴圈乘法表')
num=int(input('n='))
i = 1
while i<=num:
    
    j = 1
    while j<=num:
   
        print(str(i)+"X"+str(j)+"="+str(i*j))
        j+=1
    
    i += 1
