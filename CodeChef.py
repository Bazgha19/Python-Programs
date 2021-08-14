'''
# Add Two Numbers
a=int(input())
for i in range(a):
    s,b=map(int, input().split(' '))
    m=s+b
    print(m)
    
'''
''' Divide
a=int(input())
for i in range(a):
    s,b=map(int, input().split(" "))
    m=s%b
    print(m)
'''


''' Sum of a digit
a=int(input())
for i in range(a):
    x=int(input())
    def sum(n):  
        if n == 0:
            return 0
        else:
            return int(n % 10) + sum(int(n / 10))   
    print(sum(x))
'''




''' Sum of first and last digit
a=int(input())
for i in range(a):
    n=(input())
    r=n[::-1]
    n=int(n)
    r=int(r)
    f=r%10
    l=n%10
    s=f+l
    print(s)
'''

''' Second largest
a=int(input())
for i in range(a):
    s,b,m=map(int,input().split(' '))
    l=[s,b,m]
    u=[]
    for i in l:
        if i not in u:
            u.append(i)
    u.sort(reverse=True)
    print(u[1])
        
        
'''        



''' watermelon in codeforces
a=int(input())
if a==2:
    print('NO')

elif a%2==0:
    print('YES')
    
else:
    print('NO')

    '''


''' Life universe and everything

for i in range(100):
    b=int(input('\n'))
    if b!=42:
        print(b)
    else:
        break

'''
        

''' Reverse of a number

a=int(input())
for i in range(a):
    n=(input())
    r=n[::-1]
    r=int(r)
    print(r)

'''

''' Small factorial
a=int(input())
for i in range(a):
    b=int(input())
    s=1
    for j in range(1,b+1):
        s=s*j
    print(s)
    
'''
''' Relational operator
a=int(input())
for i in range(a):
    s,b=map(int,input().split())
    if s>b:
        print('>')
    elif s<b:
        print('<')
    else:
        print('=')

'''

''' 
s,b=map(int,input().split())
c=0
for i in range(s):
    a=int(input())
    if a%b==0:
        c=c+1
print((c))

'''

''' Incomplete...

a=input()
if a.islower():
    print('True')
elif a[:].isupper() or a[0].isupper():
    print('True')
else:
    print('False')

'''

    

''' Farenheit to Celcius (Coding Ninjas)
f1=int(input())
f2=int(input())
s=int(input())
i=f1
while i<=f2:
    c=(i-32)*5/9
    c=int(c)
    print(i,' ',c) 
    i=i+s
'''

''' Calculator (Coding Ninjas)
s=int(input())
while s!=6:
    if s<=5 and s>=1:
        a=int(input())
        b=int(input())
    if s==1:
        print(a+b)
    if s==2:
        print(a-b)
    if s==3:
        print(a*b)
    if s==4:
        print(a//b)
    if s==5:
        print(a%b)
    elif s<1 or s>6:
        print('Invalid Operation')
    s=int(input())
    
'''







