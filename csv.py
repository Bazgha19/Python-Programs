''' 
import csv 

b=open("csv2.txt",'w+',newline='')

q=csv.writer(b)
q.writerow(["dbms",'soham',2500])

b.seek(0)

p=csv.reader(b)

for i in p:
    print(i)
    
b.close() '''




''' import csv 

b=open("csv2.txt",'w+',newline='')

q=csv.writer(b)
q.writerow(["dbms",'soham',2500])

q.writerows([['Python',50,100,200,300],['c++',70,140,210,350],['java',90,160,220,360]])

b.seek(0)

p=csv.reader(b)

for i in p:
    print(i[0:3])
    
b.close() '''