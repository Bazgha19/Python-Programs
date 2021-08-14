

a=2
b=3

print(a.__add__(b))
print(a.__sub__(b))

print(a.__mul__(b))
print(a.__pow__(b))

print(a.__truediv__(b))
print(a.__floordiv__(b))

print(a.__lshift__(b))
print(a.__rshift__(b))

print(a.__mod__(b))

print(a.__and__(b))
print(a.__or__(b))
print(a.__xor__(b))
print(a.__invert__())

print(a.__lt__(b))
print(a.__le__(b))
print(a.__gt__(b))
print(a.__ge__(b))
print(a.__eq__(b))
print(a.__ne__(b))

'''
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










