#課堂練習
#使⽤者可以輸⼊任意整數 n
#當輸⼊的n不為整數，提⽰使⽤者輸⼊型態錯誤，並且重新讓使⽤者繼續輸⼊
#若輸⼊的值為整數，將其print⾄螢幕上
#ex.n=100

num=input('請輸入任意數字:')
if num.isnumeric() and float(num) - int(num) == 0 :
    print('n=',num)
else:
    print('n不為整數')
