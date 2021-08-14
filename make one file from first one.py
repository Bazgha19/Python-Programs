
""" a=open("Test1.txt","r+")

# a.write("iitm")
# a.write("dbms")
# a.write("vb.net")
print(a.tell())

s=a.read()

print(s.upper())
print(s.count('i'))
print(s.replace('i','z'))
a.close() """

""" ek file ko dusre file me write karna ho to 
a=open("Test1.txt","r")

b=open("Test2.txt","w+")

s=a.read()
"""

""" Agar hume pehli file ke data ko upper case me likhna ho new file me then these two lines are added to it
s=a.read()
s=s.upper() """

""" agar hume pehli file ke data ko replace karke likhna ho new file me then these two line are added to it 
s=a.read()
s=s.replace('i','a') """


""" agar hume pehli file ke data ko replace karke likhna ho aur bas starting ke do i hi replace karne ho to

s=a.read()
s=s.replace('i','a',2) """
'''
b.write(s)

a.seek(0)
b.seek(0)

print(a.read())
print(b.read())


a.close()
b.close()

'''




s=open("World.txt","w+")

s.write("\n Saurav \n")
s.write("\n Meenakshi \n")
s.write("\n Ashok \n")

s.close()

s=open("World.txt","r")
a=s.read()
print(a)





























