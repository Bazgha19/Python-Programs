
'''
s1='Delhiisfamouscity15346'

s= 'Delhi is famous city'
print(s)


print(s.upper())
print(s.lower())

print(s.isdigit()) #true only when all are numeric value
print(s.isalpha()) #true only when all are alphabets without any space
print(s1.isalnum())


print(s[:4]) #First 4 characters
print(s[-4:]) #Last 4 characters

print(s.count('i'))

print(s.replace('i','z'))
print(len(s))


print(s.isupper()) #First we have to make string s in upper case then we aplly this condition to make it true
print(s.islower())

s2=s.join("***")
print(s2)

print(s[len(s)-4:])

print(s[3::-2])
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




















