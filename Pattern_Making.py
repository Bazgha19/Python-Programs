'''    
for i in range(1,6):
    for j in range(i,6):
        print("*",end=" ")
    print()
'''
'''    
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
'''   
'''    
for i in range(1,6):
    for j in range(1,7):
        print("*",end=" ")
    print()    
'''   
'''
for i in range(1,6):
    for j in range(i,6):
        print(j,end=" ")
        
    print() 
    
'''

       
        
'''        
def print_squaredi(n) : 
    for i in range(1, n+1) : 
        for j in range(1, n+1) : 
            if (i==1 or i==n or j==1 or j==n  
                or i==j or j==(n - i + 1)) : 
                print('*'*a)           
            else : 
                print(' '+'#'+' '+'#')
                            
        print() 
          
          
rows = 8
print_squaredi(rows) 

'''


a=int(input())
for i in range(1,a+1):
    if i==1 or i==a:
        for j in range(1,a+1):
            print('*')
    else:
        for j in range(1,a+1):
            if j==1 or j==a:
                print('#')
                
            else:
                print(' ')
       
                    









































  