
''' def printme():
    print("hello world")
    
printme() '''

'''
def func(name):
    print("Hi",name)
func("Saurav")
'''
'''
def sum(a,b):
    return(a+b);

a=int(input("Enter a:"))
b=int(input("Enter b:"))
print("Sum=",sum(a,b)) '''




'''
def change_list(list1):
    list1.append(20)
    list1.append(30)
    print("list inside function=",list1)
    
list1=[10,30,40,50]

change_list(list1)
print("list outside function=",list1) 

'''

'''
def change_string(str):
    str=str+"Hows you"
    print("printing the string inside function:",str)

string1="Hi I am there"
change_string(string1)
print("printing the string outside function:",string1)
'''

'''Swap two numbers

def swap(x,y):
    s=x
    x=y
    y=s
    print(x,"",y)

swap(3,4)
'''

'''swap 2 nos taking input from console

def swap(x,y): #x and y works as a reference and they refer a and b 
    s=x
    x=y
    y=s
    print(x,"",y)

a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))

print("Before Swapping")
print(a,"",b,"\n") #simply print the original value of a and b

print("After Swapping")
swap(a,b)


'''

'''def list_change(l):
    l=[3]
    print(l)
    
x=[1,2,3,5,6]    
list_change(x)
print(x)'''

'''
def list_change(l):
    l[0]=20
    print(l)
    
x=[1,2,3,5,6]    
list_change(x)
print(x) #jo bhi changes l karega vo x bhi krega isme

'''


''' def list_change(l):
    l[0]=[i+2 for i in l if i%2==0]
    print(l)
    
x=[1,2,3,5,6,7,12,14]    
list_change(x)
print(x) '''


''' sum of list
def list_change(l):
    sum=0
    for i in l:
        sum=sum+i
    print(sum)
    
x=[1,2,3,5,6]    
list_change(x)'''


'''
def func(name):
    message='Hi'+' '+name
    return message
name=input("Enter the name: ")
print(func(name))
'''

'''
def calculate(a,b):
    return a+b
print(calculate(10,5))
'''

'''
def printme(a,b=6,c=10):
    return a+b+c
print(printme(7,2,1))
'''
'''
def printme(name,age=22):
    print("My name is",name,'and age is',age)
printme('Meenu')
'''

'''
def printme(*names):
    print("Type of passed argument is ", type(names))
    print("Printing the passed arguments...")
    for name in names:
        print(name)
        
printme('Meenu','Ash','Radha')
printme(10,20,30)  '''



''' def func(name,message):
    print("Printing the message with ",name,'and',message)
    
func(name='Meenu',message='hello')
func('Meenu','hello')             #all three func are same
func(message='hello',name='Meenu') '''

'''
def simple_interest(p,t,r):
    return (p*t*r)/100
print("Simple Interest: ",simple_interest(t=10,r=10,p=1900))
'''
'''
def factorial(x):
    if x==1:
        return 1
    else:
        return(x*factorial(x-1))
num=5
print("The factorial of",num,'is',factorial(num))
'''

'''

def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
    
n=int(input("Enter the number: "))
for i in range(n):
    print(fib(i))
    
'''


'''

def total(n):
    if n<0:
        return 0
    else:
        return n+total(n-1)
    
n=int(input("Enter the number: "))
print("Sum of 10 natural number:",total(n))
'''

'''
def num(a,b):
    c=a**b
    return(c)

a=int(input("Number 1: "))
b=int(input("Number 2: "))
print(num(a,b))
'''

'''
def num(a,b):
    c=pow(a,b)
    return c

a=int(input("Number 1: "))
b=int(input("Number 2: "))
print(num(a,b))

'''

'''
def num(a,b):
    if b==0:
        return 1
    else:
        i=0
        while(i<=b):
            k=a*a
            i=i+1
            return k
    
a=int(input("Number: "))
b=int(input("Power Value: "))
print(num(a,b))
'''

'''
def search(list,n):
    for i in range(len(list)):
        if list[i]==n:
            return i+1
        
    return ("Not Found")
    
    
list=[1,2,3,4,5,2,3,6]
n=int(input("Searched Element: "))
print(search(list,n))
'''

''' Power program
def n(a,b):
    if b==1:
        return a
    if b!=1:
        return (a*n(a,b-1))
    
a=int(input("First number: "))
b=int(input("Second number: "))
print(n(a,b))

'''
'''
def p(n,e):
    if e==0:
        return 1
    else:
        return n*p(n,e-1)

n=int(input(""))
e=int(input(""))
print(p(n,e))
'''





'''
#sum of n even numbers using recursion
def ser(n):
    if n>0:
        return 2*n+ser(n-1)
    else:
        return 0

n=int(input(" "))
print(ser(n))
'''


'''
#sum of n odd numbers using recursion
def ser(n):
    if n>0:
        return (2*n-1)+ser(n-1)
    else:
        return 0

n=int(input(" "))
print(ser(n))
'''



'''
def calculate(*args):
    sum=0
    for arg in args:
        sum=sum+arg
    print("The sum is ",sum)
    
sum=0
calculate(10,20,30)
print("Value of sum outside the function: ",sum)
'''


'''
#Evaluation of any function using eval()
print("1+8")
print(eval("1+8"))
'''


'''
#use of zip()
a=(1,2,3)
b=("a","b","c")
c=(4,5,7)

x=(zip(a,b,c))
for i in x:
    print(i)
'''




def swap(x,y): #x and y works as a reference and they refer a and b 
    s=x
    x=y
    y=s
    print(x,"",y)

a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))

print("\nBefore Swapping")
print(a,"",b,"\n") #simply print the original value of a and b

print("After Swapping")
swap(a,b)





