file = open('stores_old.csv', 'r', encoding='big5')
for line in file.readlines():
    text=(line.split(','))

    print(text[0], text[4], text[5], text[6],sep=",", end='\n',file=open('stores_old_1.csv','a',encoding='big5'))
file.close()

