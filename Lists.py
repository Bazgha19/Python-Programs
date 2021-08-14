#elements of list are mutable

""" empty list 
L =[]
print (L) """

""" define element in list"

L=[1,2,"a",4,"b",6.23]

print(L) """

""" search an element
L=[1,2,"a",4]

print(L[3]) """


""" slicing used in list

L=[1,2,"a",4,"b",4.78]

print(L[2:])
print(L[2:5])
print(L[1:5:2]) """

""" List in a list 

L=[1,2,"a",4,"b",6.42,[2,3,4]]

print(L) """ 

"""input from the user

a=int(input("Enter the value:"))
L=[a,1,2,"a",4,"b",4.78,[2,3,4]]

print(L) """

""" L=[1,2,"a",4,"b",4.78,[2,3,4]]

print(L[6][2:]) """


""" using negative index

L=[1,2,3,4,5]

print(L[-3:])
print(L[:-1]) """

""" L1=[3,5,6,8]
L2=[2,7,12,16]
print(L1)
print(L1*3)
print(4 in L1)
L=["Saurav","Ladli","Ladla"]
for j in L:
    print(j)
    
for i in range(6):
    print(i)

L3=[i for i in range(6)]
print(L3)

L4=[i+2 for i in range(6)]
print(L4)

L5=[i*2 for i in range(51)]
print(L5)

L[0]="Bazgha"
print(L)


L6=[1,2,3,[4,5,6],7,8]
L6[3][2]=3
print(L6)

L7=[3,5,6,8]
L7.append(["Rose",4,6])
print(L7)

L8=[3,5,6,8]
L8.append("Rose")
print(L8)
L8.insert(2,"OK")
print(L8)
L8.remove(8)
print(L8)


#first occurence removed if you have multiple variable
L9=[1,2,3,4,5,5,5,5,6,7]
L9.remove(5)
print(L9) """ 
 

""" LIST built in funtcions

l=[3,6,9,3,6,3,6,8,3]
l1=[]
l2=[]
l1=l
print(l1)

l2=l1.copy()
print(l2)

#print(l2.clear())

l.sort()
print(l)

l.sort(reverse=True)    # decending order
print(l)

print(l.count(6))


print(max(l))

print(min(l))


print("Sum of elements are: %d "%sum(l))


a=sum(l)
b=len(l)

avg=(a/b)

print("Average of the elements are: %d" %avg)



print(l)

for i in range(5):
    print(l.pop())
    
print(l)

print(l.index(6))


l2.extend(l)
print(l2)  """




''' remove duplicates from list '''

l=[1,2,3,4,2,3,2,2,5,6,7]
U_l=[]
for i in l:
    if i not in U_l:
        U_l.append(i)
print(U_l)
    




''' find second largest element '''
l=[1,2,3,4,2,3,2,2,5,6,7]
u=[]
if (len(l)<2):
    print("invalid list")
else:
    for i in l:    # agar list l me element hai to if ki condition check karna hai
        if i not in u: #agar element list u me nhi hai 
            u.append(i) #to append karenge u me varna nhi aur sare append hone ke bad new list is ready
u.sort(reverse=True);   #u list jo banegi use sort kar denge aur sorted list ko reverse kar denge
print(u[1])  #second element is the second largest element
    


''' find the common element in two list'''

l1=[1,3,5,7,9]
l2=[1,2,4,6,7,8]
for i in l1:
    if i in l2:
        print(i,end='')

'''find the element of the list which are not present in another list'''

l3=[1,3,5,7,9]
l4=[1,2,4,6,7,8]
for i in l3:
    if i not in l4:
        print(end=', ')
        print(i,end='')
        
        
        
        
        
        
L19=[1,2,3,4,5]
#L19.insert(3,4)
print(sum(L19))