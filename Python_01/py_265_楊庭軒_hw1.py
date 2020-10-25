#Q1
#students who pass math
math_pass={'Tom','Mary','Jimmy','Sunny','Amy'}
#students who pass english
eng_pass={'John','Mary','Tony','Bob','Pony','Tom','Alice'}
#math pass but english fail
print("students who pass math but fail english are" ,math_pass-eng_pass)
#english pass but math fail
print("students who pass english but fail math are" ,eng_pass-math_pass)
#both math and english pass
print("students who pass both math and english are" ,eng_pass&math_pass)
#all the students in the class
print("all the students in the class are" ,eng_pass|math_pass)


#Q2
#Tom's homework grades & John's
hw={'Tom':[80,100,90,95],'John':[100,93,75,80]}
print("average score of Tom's homework is" ,sum(hw.get('Tom'))/len(hw.get('Tom')))
print("average score of John's homework is" ,sum(hw.get('John'))/len(hw.get('John')))
