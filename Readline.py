
""" a=open("Test1.txt","w+")

a.write("I like programming")

a.seek(4)

print(a.read())

a.close() """


""" # kitni length hai ye bata dega
a=open("Test1.txt","w+")

a.write("I like programming")


print(a.read())

print(a.tell())

a.close() """





""" #line read karne ke liye hum readline use karte hai agar bht sare lines read karna hai to for loop use karenge that was done below
a=open("Test1.txt","w+")

a.write("I like programming\nI like python\nI live in delhi")

a.seek(0)

print(a.readline())
print(a.readline())

a.close() """



""" # readlines nhi lagayenge varna vo \n ko bhi read karega
a=open("Test1.txt","w+")

a.write("I like programming\nI like python\nI live in delhi")

a.seek(0)

print(a.readline())
print(a.readlines())

a.close() """



""" # jitni line ko read karvana hai uske liye for loop lagayenge
a=open("Test1.txt","w+")

a.write("I like programming\nI like python\nI live in delhi")

a.seek(0)

for i in range(4):
    print(a.readline())


a.close() """

'''
a= open("Test1.txt", "r+") 
s= a.read(10) 
print ("Read String is : ", s)
# Check current position 
position = a.tell() 
print( "Current file position : ", position)
 # Reposition pointer at the beginning once again 
position =a.seek(0, 0)
s= a.read(10) 
print ("Again read String is : ", s)
# Close opend file 
a.close()

'''
'''
s= "Hi I am Saurav Bemotra"
s=s.split()

# split string s
for i in s:
    print(i)

# Length of sub string i.e., Hi, I, am, Saurav, Bemotra    
a=[len(j) for j in s]
print(a)
k=(max(a))
print(k)
x=[j for j in s if len(j)==k]
print(x)
    
    

m_1=max(len(w) for w in s)
print(m_1)
a=[]
a=[word for word in s if len(word)==m_1]

'''


'''
s=open("World.txt","r")
s=s.split()

b=[len(j) for j in s]
m=(max(b))
for j in s:
    if len(j)==m:
        x=j
print(x)
'''

'''
s=open("World.txt","r")
b=s.read()
b=b.split()
m=max(len(j) for j in b)
print(m)
a=[]
a=[word for word in b if len(word)==m]
print(a)

s.close()
'''


s=open("World.txt","r")
a=s.read()
a=a.split()
b=[len(j) for j in a]
m=(max(b))
for j in a:
    if len(j)==m:
        x=j
print("Longest string in a file: ",x)























