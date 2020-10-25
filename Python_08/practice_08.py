#teacher demo
import random
file=open('randome.txt','w')
odd_nums=range(1,1001,2)
for i in random.sample(odd_nums,100):
    file.write(str(i)+'\n')
file.close()


#self practice~
file=open('text2.txt','w')
import random
nums=range(1,1000,2)
randomnums=random.sample(nums,100)
for i in range(0,99):
    file.write(str(randomnums[i])+'\n')
file.close()
