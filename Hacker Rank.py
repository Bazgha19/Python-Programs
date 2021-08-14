

""" n=22

if n%2==0:
    if n in range(2,5)or n>20:
        print("Not Weird")
    else:
        print("Weird")
else:
    print("Weird")   """
    
""" The first line contains the sum of the two numbers.
The second line contains the difference of the two numbers (first - second).
The third line contains the product of the two numbers. """

""" a=int(input(""))
b=int(input(""))

print(a+b)
print(a-b)
print(a*b) """




'''
a=6564424525
b=323252462

c=(a//b)
print(c)
print(a/b)



n=10
for i in range(n):
    print(i*i)
    '''
'''Numpy array 
import numpy as np
a=([11,12,13],[21,22,23],[31,32,33])
A=np.array(a)
print(A)
print(type(a))
print(A.size)
print(A.ndim)'''








'''
s=set()
n=int(input())
for i in range(n):
    n=int(input())
    s.add(n)

s1=set()
m=int(input())
for j in range(m):
    m=int(input())
    s1.add(m)


S=s.union(s1)
print(len(S)) '''

'''l=[]
n=int(input())
for i in range(n):
    n=int(input())
    l.append(n)

l1=[]
m=int(input())
for j in range(m):
    m=int(input())
    l1.append(m)


L=l+(l1)
A=(str(set(L)))
print(A)'''

''' 
e={1:'a','S':'b',3:'c'}
print(e["S"]) '''




''' n = int(input())
a = set(map(int,input().split()))
m = int(input())
b = set(map(int,input().split()))
print(a.union(b))
print(len(a.union(b))) '''




''' Symmetric difference of two sets
a=int(input())
b=set(map(int,input().split()))
c=int(input())
d=set(map(int,input().split()))
print((d^b).union(b^d))   '''






'''def Count(s): 
    
    upper, lower, number= 0, 0, 0,
    for i in range(len(s)): 
        if s[i].isupper(): 
            upper += 1
        elif s[i].islower(): 
            lower += 1
        else: 
            number += 1
    print('Upper case letters:', upper) 
    print('Lower case letters:', lower) 
    print('Number:', number) 
    
    
s='Hello12345world'
print(Count(s))'''



def Count(s): 
    upper, lower, digit = 0, 0, 0
    for i in range(len(s)): 
        if s[i].isupper(): 
            upper += 1
        elif s[i].islower(): 
            lower += 1
        else: 
            digit += 1
    print('Upper case letters:', upper) 
    print('Lower case letters:', lower) 
    print('Total Digit:', digit) 
    #print('Special characters:', special) 

s = "Hello12345World"
Count(s) 






