
a=open("Test1.txt","w+")

a.write("iitm")
a.write("dbms")
a.write("vb.net")
print(a.tell())
a.seek(0)

print(a.read())

a.close() 


a=open("Test1.txt","a+")

a.write("iitm")
a.write("dbms")
a.write("vb.net")
print(a.tell())
a.seek(0)

print(a.read())

a.close()

# First ten prime numbers
for i in range(0,30):
  if i>1:
    for j in range(2,i):
        if(i % j==0):
            break
    else:
        print(i)