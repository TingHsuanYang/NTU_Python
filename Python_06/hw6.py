infile=open('stores_new.csv','w')
for line in open('stores_old.csv','r'):
	sp=line.strip().split(',')
	infile.write('%s,%s,%s,%s\n'%(sp[0],sp[3],sp[5],sp[6]))