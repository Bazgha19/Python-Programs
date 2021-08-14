# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 13:36:02 2020

@author: asus
"""

#e={1:'a','S':'b',3:'c'}
#print(e["S"])



''' a={}
print(a)
a['name']="Saurav"
a['age']=30
a[12]="Meenu"
print(a)

print(a['age'])

a["Work"]=['Ashok','Ladli','Ladla']

print(a["Work"]) '''



'''
a={}
a['name']="Saurav"
a['age']=30
a[12]="Meenu"

a["Work"]=['Google','Infy','Del']

#print(a["Work"])


#del a['age']
print(a)

'''


'''iterating the dictionary

print("Print Keys")
for j in a:
    print(j) #print keys


print("Print Values")
for i in a:
    print(a[i]) #print values because i ke pas keys hai to ab vo values ko print karega

'''
'''

print("\nDict items")
for i in a.items():
    print(i)
    

print("\nVALUES")
for i in a.values():
    print(i)


print("\nKEYS")    
for i in a.keys():
    print(i) '''

    
'''
d1={'a':{'a1':12,'a2':24,'a3':29},'p':[2,3,5,7,"saurav"],'c':"Meenu"}
print(d1)
print(sep=" ")
print(d1['a'])
print(d1['a']['a1'])


d2={'s':[10,20,30],'b':{'a':18,'m':[12,19]}}
print(sep=" ")
print(d2)
print(sep=' ')

d1.update(d2)        #update d1
print(d1)
print(len(d1))       #len of dictionary

print(d1.pop('s'))   #delete a specific key
print(d1.popitem())  #delete last key element i.e, b not m because m is the value of b so last key is b 
print(d1)


d2.clear()
print(d2)
'''

'''
count=0
for i in d1.items():
    count=count+1
print(count) #len of dictionary without using len function
'''

'''
D5={'a':1,'b':4,'c':6,'f':12}
print(len(D5))
print(D5)
for i in D5.values():
    print((i))

'''

'''
n=int(input().split())
x=map(input(dict_items().split())
y=map(input(dict_keys().split())
for i in x.items():
    if i in y.keys():
        print(y.values())

'''

'''
Merge two dictionaries

x={'s':1,'b':9}
y={'a':1,'m':8}

z={**x,**y}
print(z)

'''

''' Squares of first 10 numbers using dictionary 

squares={x:x*x for x in range(1,11)}
print(squares)

'''


squares={x:x*x for x in range(5)}
for i in squares:
    print(squares[i])




