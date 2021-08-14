
''' Exception hsndling
a=[2,3,4,"Saurav",5]
try:
    print("Welcome!!!")
    print(a[10])
    print("Hello Exception Handling")
    
except:
    print(a[3])
    print("Exception Caught")
    
else:
    print("Ohhh! there is no exception")
    
finally:
    print("I am in finally block...")
    

'''    
    
    
    
    
    
    
    
    
    


# Exception handling

#exception syntax error nhi hoti logical error hoti hai 
#logical error
#exception are the conditon that will stop the flow of the program

'''
print("google")
x=6
y=7
print(x/y)
print("Hello")

a=9
b=0
print(a/b)
'''

'''
a=[1,2,3,4,5]
print(a[9])
'''

''' More then one except block '''
a=[2,3,4,"Saurav",5]

try:
    print("Welcome!!!")
    print(a[10])
    print("Hello Exception Handling")
    c=3
    d=0
    print(c/d)
    
except IndexError:
    print("Exception Caught of type index error")
    
except ZeroDivisionError:
    print("Exception caught of type division by zero error")
 

 
 
 
a=[1,2,3,2,2,4,3,2]
print(a.count(2))
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 