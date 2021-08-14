# April Long Challenge

''' VALID PAIRS

a,b,c=map(int,input().split(' '))

if a==b or b==c or c==a:
    print('YES')
    
else:
    print('NO')
    
'''


''' WORLD RECORD 

t = int(input())
for i in range(t):
    k1,k2,k3,v = map(float,input().split(' '))
    time = 100/(k1*k2*k3*v)
    final_result = round(time,2)
    if final_result<9.58:
        print('YES')
        
    else:
            print('NO')
    
'''   


''' CHEF And DICE
t=int(input())
for i in range(t):
    n=int(input())
    if n==1:
        print(20) 
    elif n==2:
        print(36)
    elif n==3:
        print(51)
    elif n==4:
        print(60)
    else:
        r=n%4
        ans=((n-r)//4)*44
        if r==0:
            ans=ans+16
            print(ans)
        elif r==1:
            ans=ans+32
            print(ans)
        elif r==2:
            ans=ans+44
            print(ans)
        elif r==3:
            ans=ans+55
            print(ans)            
'''


''' STRONG LANGUAGE  '''
          
t =  int(input())
t in range(1,11)
c=0
for z in range(t):
    n,k = map(int,input().split(' '))
    x=list(map(str,input()))[:n]
    s=''.join(x)
    
    s=s.lower()
    
    for i in range(len(s)):
        if s[i]=='*':
            c=c+1
        else: 
            if c>=k:
                break
            else:
                c=0
    if c>=k:
        print('YES')
    else:
        print("NO")
            





            
                
            
         
            
    
        
        
