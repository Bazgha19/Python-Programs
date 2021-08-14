""" Reversal of number 
a=int(input("Enter number: "))
c=b=0;
while(a>0):
    b=a%10
    print(b, end='')
    a=int(a/10) """
    
""" Factorial of a number
num=int(input("Enter number:"))
if(num>=0):
        fact=1
        for i in range(1,num+1):
            fact=fact*i
print("Factorial of number: ",fact)  
"""


""" GCD of two numbers 
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))     
if(a>b):
    s=b
else:
    s=a
    for i in range(1,s+1):
        if(a%i ==0 and b%i==0):
            gcd=i
            i=i+1
print("GCD of number is",gcd) """

""" Newton abson method
a=int(input("Enter the number to calculate square root: "))
b=int(input("Enter initial guess: "))
n=int(input("Enter the number of iterations: "))
for i in range(n):
    b=(b+(a/b))/2
    print(abs(b))
print("The square root of the %d is: %f"%(a,abs(b)))
"""




"""Exponent of a number
a=int(input("Enter number: "))
b=int(input("Enter exponent number: "))
s=1
for i in range(1,b+1):
    s=a*s
    print(s) """
    
""" Decimal Equivalent
a=0
for i in range(2,11):     
    a=1/i
    print(a) """
    
'''Sum of digit of a number
n=int(input("Enter a number:"))
a=0
while(n>0):
    dig=n%10
    a=a+dig
    n=n//10
print("The total sum of digits is:",a)'''

'''Average of best two marks out of three
a=int(input("Enter marks 1= "))
b=int(input("Enter marks 2= "))
c=int(input("Enter marks 3= "))
avg1 =(a+b)/2
avg2 = (b+c)/2
avg3 = (c+a)/2
c=(max(avg1, avg2, avg3))
print("\nBest average of two numbers=",c) '''
#a=int(input("Enter no: "))
 
""" Q11 pattern making

# x=1
for i in range(1,6):
    for j in range(i,6):
        print(j,end=" ")
        
    print() 
    """
    
    
    
''' Exponent/power of a number

a=int(input("Enter Number a:"))
b=int(input("Enter Number b: "))
c=a**b
print(c)'''



'''check the no: even or odd 
a=int(input("Enter number: "))
if a%2==0:
    print("Even")
else:
    print("Odd") 
'''


''' biggest number among 3 

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))

if (a>c) and (a>b):
    print("First number is greater")
elif (b>c)and (b>a):
        print("Second number is greater")
else:
    print("Third number is greater")    
    '''
    
    
# STRING PROGRAMS OF LAB    


''' reversal of a string
s="Hello World"
b=(s[::-1])  
print("Original String: ",s)
print("Reversed String: ",b)'''

'''length of string
s='Hello World'
b=len(s)
print("String: ",s)    
print("Length of string:",b)'''

''' first and last 2 character of strings 
s="Hello World"
print("String: ",s)
print("First two character:",s[:2])
print("Last two character:",s[-2:])  '''


''' upper and lower 
s="Hello World"
print("Original String: ",s)
print("Upper Case:",s.upper())
print("Lower Case:",s.lower()) 
'''
'''
def count(s):
    upper,lower,digit=0,0,0
    for i in range(len(s)):
        if s[i].isupper():
            upper+=1
        elif s[i].islower():
            lower+=1
        else:
            digit+=1
    print("Upper Case Letters:",upper)
    print("Lower Case Letters:",lower)
    print("Total Digit:",digit)

s='Hello1819World'
print("Original String:",s)
print(count(s))
'''            


'''matrix multiplication

x=[[12,7,3],[4,5,6],[7,8,9]]

print("\nFirst Matrix:",x)

# 3x4 Matrix
y=[[5,8,1,2],[6,7,3,0],[4,5,9,1]]

print("Second Matrix:",y)

# Result is 3x4
result=[[0,0,0,0],[0,0,0,0],[0,0,0,0]]


# iterate through rows of x
for i in range(len(x)):
    
    # iterate through columns of y
    for j in range(len(y[0])):
        
        # iterate through rows of y
        for k in range(len(y)):
            result[i][j] +=x[i][k]*y[k][j]
            
print("\nMultiplied Matrix:")
for r in result:
    
    print(r)
    '''


''' Selection Sort

A = [64, 25, 12, 22, 11, 6, 34, 52, 94,28]

for i in range(len(A)):
    min_idx = i
    for j in range(i+1, len(A)):
        if A[min_idx] > A[j]:
            min_idx = j
            
# Swap the found minimum element with
# the first element
    A[i], A[min_idx] = A[min_idx], A[i]
    
# Driver code to test above
print ("Sorted array")
for i in range(len(A)):
    print("%d" %A[i])

'''

''' position of a character in string

s=(input(" "))

b=(input("\t"))

print("\nInitial string:",s,"\nCharacter to find:",b)

c=None
for i in range(0,len(s)):
    if s[i]==b:
        c=i+1
        break
if c==None:
    print("No such character available in the string")
else:
    print("Character {} is present at {}".format(b,str(c)))

'''
''' first and last 2 elements

# Type your string
s=input("")

# First two elements of given string
a=s[:2]

# Last two elements of given string
b=s[-2:]

print("First two elements of the given string:",a)

print("Last two elements of the given string:",b)
'''
'''
# Original String
s=input("Original String: ")

# Add an element
b=input("String after adding element ")

# After adding element in original string
c=(s+b)

# Remove an element from string
d=c.replace("b","l")

print("\n",c)
print("\n",d)
'''
'''First and last 2 elements from list

s=[1,2,3,4,5,6,7,8]
print("Original List:",s)

# First two elements of given string
x=s[:2]

# Last two elements of given string
y=s[-2:]

print("\nFirst two elements of the given list:",x)
print("Last two elements of the given list:",y)
'''
'''
# Original List
s=[1,2,3,4,5,6,7,8]
print("Original List:",s)

# Inset an element in List
s.insert(5,9)
print("After inserting an element:",s)

# Delete an element in List
s.remove(9)
print("After deleting an element:",s)

'''
''' Find duplicate elements
def Repeat(x): 
    s= len(x) 
    repeated = [] 
    for i in range(s): 
        k = i + 1
        for j in range(k,s): 
            if x[i] == x[j] and x[i] not in repeated: 
                repeated.append(x[i]) 
    return repeated 
  
# Driver Code 
l = [1,2,3,4,5,5,5,6,7,3,4,3,3,4,8] 
print("\nOriginal List:",l)
print ("\nDuplicate Elements from List:",Repeat(l)) 
'''
'''
l=[1,2,3,4,2,3,2,2,5,6,7]
print("\nOriginal List:",l)
u=[]
if (len(l)<2):
    print("invalid list")
else:
    for i in l:  
        if i not in u:  
            u.append(i)
            
print("\nSorted List:",u)
u.sort(reverse=True); 
  
print("\nSecond Largest Element in the List:",u[1])
'''

'''
s={}
print("\nEmpty Dictionary:",s)
s['name']="Saurav"
s['age']=30
s[12]="Meenakshi"
print("\nDictionary:",s)

print("\nAccess value of name from Dictionary:",s['name'])

b=s.keys()
print("\n",b)

b=s.values()
print("\n",b)
'''





'''
n=int(input("Enter the number:"))
if n>1:
    for i in range(2,n//2):
        if(n%i==0):
            print("No is not prime")
            break;
            
    else:
            print("No is prime")
            '''
           
'''Binary Search
                
def binary_search(arr,x):
    low=0
    high=len(arr)-1
    mid=0
    
    while low<=high:
        mid=(high+low)//2
        
        if arr[mid]<x:
            low=mid+1
            
        elif arr[mid]>x:
            high=mid-1
            
        else:
            return mid
        
    return -1

arr=[2,3,19,18]

print("\nArray:",arr)

x=int(input("\nEnter the element:"))

result=binary_search(arr,x)

if result !=1:
    print("\nElement is present at index",str(result))
    
else:
    print("Element is not present in array")
'''

''' prime number
i = 1
x = int(input("Enter the number:"))
for k in range(1, x+1):
    c = 0
    for j in range(1, i+1):
        a = i % j
        if a == 0:
            c = c + 1

    if c == 2:
        print(i)
    else:
        k = k - 1

    i = i + 1
'''
''' first N Prime number 
def print_primes_till_N(N):
 
    # Declare the variables
    i, j, flag = 0, 0, 0;
 
    # Print display message
    print("\nPrime numbers between 1 and",N,":")
 
    # Traverse each number from 1 to N
    # with the help of for loop
    for i in range(1, N + 1, 1):
 
        # Skip 0 and 1 as they are
        # niether prime nor composite
        if (i == 1 or i == 0):
            continue;
 
        # flag variable to tell
        # if i is prime or not
        flag = 1;
 
        for j in range(2, ((i // 2) + 1), 1):
            if (i % j == 0):
                flag = 0;
                break;
 
        # flag = 1 means i is prime
        # and flag = 0 means i is not prime
        if (flag == 1):
            print("\n",i);
 
# Driver code
N =int(input(""))
print_primes_till_N(N)
'''
''' Employee class
class employee:
    def display(self):
        print("\n",self.name,self.emp_id)           
    
#create object        
e1=employee()
e1.name='Renu'
e1.emp_id=130
e1.display()

#create object 2
e2=employee()
e2.name='Geeta'
e2.emp_id=120
e2.display()

#create object 3 
e3=employee()
e3.name='Anju'
e3.emp_id=126
e3.display()

#creater object 4
e4=employee()
e4.name='Neena'
e4.emp_id=102
e4.display()

#create object 5
e5=employee()
e5.name='Sonia'
e5.emp_id=119
e5.display()
    '''

''' 
class person:                                     #SuperClass
    def __init__(self,name,id):
        self.name=name
        self.id=id

class employee(person):                           #DriveClass 
    def __init__(self,name,id,dept,designation):
        self.dept=dept
        self.designation=designation
        person.__init__(self,name,id)

    def display(self):
        print("\nEmployee name:",self.name,",","Id is:",self.id,"\nDepartment:",self.dept,",","Designation:",self.designation)




e1=employee("Sonia",20,"IT","Accountant")
e1.display()

e2=employee("Bhawna",29,"HR","Intern")
e2.display()
'''
''' Inheritance 
  
class A:
    def n(self):
        print("In class A")
        
class B(A):
    def n(self):
        print("In class B")
        
class C(A):
    def n(self):
        print("In class C")
        
class D(B,C):
    pass

obj=D()
obj.n()

A.n(obj)
C.n(obj) 
    
 '''
'''
import abc

class Shape:
    def area(self):
        pass
    
class Rectangle(Shape):
    def __init__(self,x,y):
        self.l=x
        self.b=y
    def area(self):
        return self.l*self.b

class Square(Shape):
    def __init__(self,x):
        self.l=x
    def area(self):
             print(self.l*self.l)

r=Rectangle(10,20)    
s=Square(10)
print("Area of rectangle:",r.area())
print("Area of Square:",s.area())   
'''



''' Area of rectangle and square using Abstract class 
import abc
class shape:
    def area(self):
        pass
    
class Rectangle(shape):
    def __init__(self,x,y):
        self.l=x
        self.b=y
        
    def area(self):
        return self.l*self.b
    
class Square(shape):
    def __init__(self,x):
        self.a=x
    def area(self):
            return self.a*self.a
    
r=Rectangle(10,20)
s=Square(10)
print("Area of Rectangle:",r.area())
print("Area of Square:",s.area()) 
'''

''' + and - overloading

class demo:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __add__(self,e):
        r=self.a+e.a
        s=self.b+e.b
        print("\n",r,s)
        
    def __sub__(self,e):
        r=self.a-e.a
        s=self.b-e.b
        print("\n",r,s)
        
x=demo(6,4)
y=demo(3,2)
x+y
x-y
   
''' 
    
'''  < and > overloading   
class demo:
    def __init__(self,a):
        self.a=a
    def __gt__(self,e):
        r=self.a>e.a
        print("\n",r)
        
    def __lt__(self,e):
        r=self.a<e.a
        print("\n",r)
        
x=demo(6)
y=demo(3)
x>y
x<y
'''    
'''    
a=open("Test1.txt","w+")

a.write("I like programming\nI like python\nI live in delhi")

a.seek(0)

for i in range(3):
    print(a.readline())


a.close()   
'''
''' Write a python to copy the content from one file to another file in capital letters
a=open("Test1.txt","r")

b=open("Test2.txt","w+")

s=a.read()    
    
s=s.upper()

b.write(s)

a.seek(0)
b.seek(0)

print("\n Content of File 1\n",a.read())
print("\n Content Copied to File 2 in Capital letters\n",b.read())


a.close()
b.close()
'''

''' Write a python to copy the content from one file to another file.

a=open("Test1.txt","r")

b=open("Test2.txt","w+")

s=a.read() 
b.write(s)

a.seek(0)
b.seek(0)

print("\nContent of File1\n",a.read())
print("\nContent Copied to File2\n",b.read())


a.close()
b.close()    

'''  
''' 2-D Matrix  
    
r, c = (3, 3) 
arr=[] 
for i in range(c): 
    c= [] 
    for j in range(r): 
        c.append(int(input())) 
    arr.append(c) 
print("Required 2-D Matrix:",arr) 
'''

''' Insertion Sort 

def insertionSort(arr): 
  
    # Traverse through 1 to len(arr) 
    for i in range(1, len(arr)): 
  
        key = arr[i] 
   
        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key 
  
  
# Driver code to test above 
arr = [19, 2, 18, 5, 4] 
insertionSort(arr) 
print ("Sorted array is:") 
for i in range(len(arr)): 
    print ("%d" %arr[i]) 

'''

''' Merge Sort
def merge(arr, l, m, r): 
    n1 = m - l + 1
    n2 = r- m 
  
    # create temp arrays 
    L = [0] * (n1) 
    R = [0] * (n2) 
  
    # Copy data to temp arrays L[] and R[] 
    for i in range(0 , n1): 
        L[i] = arr[l + i] 
  
    for j in range(0 , n2): 
        R[j] = arr[m + 1 + j] 
  
    # Merge the temp arrays back into arr[l..r] 
    i = 0     # Initial index of first subarray 
    j = 0     # Initial index of second subarray 
    k = l     # Initial index of merged subarray 
  
    while i < n1 and j < n2 : 
        if L[i] <= R[j]: 
            arr[k] = L[i] 
            i += 1
        else: 
            arr[k] = R[j] 
            j += 1
        k += 1
  
    # Copy the remaining elements of L[], if there 
    # are any 
    while i < n1: 
        arr[k] = L[i] 
        i += 1
        k += 1
  
    # Copy the remaining elements of R[], if there 
    # are any 
    while j < n2: 
        arr[k] = R[j] 
        j += 1
        k += 1
  
# l is for left index and r is right index of the 
# sub-array of arr to be sorted 
def mergeSort(arr,l,r): 
    if l < r: 
  
        # Same as (l+r)//2, but avoids overflow for 
        # large l and h 
        m = (l+(r-1))//2
  
        # Sort first and second halves 
        mergeSort(arr, l, m) 
        mergeSort(arr, m+1, r) 
        merge(arr, l, m, r) 
  
  
# Driver code to test above 
arr = [12, 19, 18, 5, 4, 0] 
n = len(arr) 
print ("Given array is") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
mergeSort(arr,0,n-1) 
print ("\n\nSorted array is") 
for i in range(n): 
    print ("%d" %arr[i])

'''

''' Random Number    
import random

print(random.randint(1,6))
    '''

    

    