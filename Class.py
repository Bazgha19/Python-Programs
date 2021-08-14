''' #create class
class animal:
    colour='White'
    weight=80
    def display(self):
        print(self.colour,self.weight)
        
    def speak(a): #a is just we write in place of self it is a reference
        print("Animal is speaking")
    
    
#create object        
Dog=animal()
Dog.display()
Dog.speak()


#create object 2
Cow=animal()
Cow.colour='Black'
Cow.weight=120
Cow.display()


#create object 3 
Butterfly=animal() 
Butterfly.colour='Pink'
Butterfly.weight=15
Butterfly.display()  '''

'''
class student:
    roll_num=101
    name="Joseph"
    
    def display(self):
        print(self.roll_num,self.name)
        
s=student()
s.display() '''




'''
class student:
    def__init__(self):  '''
    
    
'''
class demo:
    count=0
    def __init__(self):
        demo.count=demo.count+1
        
        
s1=demo()
s2=demo()
s3=demo()
print("TOtal number of objects are:",demo.count)'''

'''
class demo:
    
    def __init__(self):
        print("this is my first constructor")
        
    def __init__(self):
        print("this is my second constructor")
        
        
s1=demo()
'''

'''
class demo:
    
    def __init__(self,*arg):
        s=0
        for i in arg:
            s=s+i
        print("Sum is ",s)
        
        
s1=demo(1,2,3)

s2=demo(2,3,4,5)

s3=demo(2,3,4,5,6,7)
'''
'''
class Student: 
    def __init__(self,name):
        print("This is Parametrized constructor")
        self.name=name
    def show(self):
        print("Hello",self.name)
student=Student("John")
student.show()

'''

'''
class employee:
    def tellname(self):    
        print("Hello World")
        
class boss(employee):
    def whoismyboss(self):
        print("I am your boss")
        
        
class manager(boss):
    def __init__(self, name):
        self.name=name
    def salary(self, name):
        print(self.name,"I have good salary")

m1=manager()
m1.tellname()
#m1.whoismyboss()
m1.salary()
e1=employee()
e1.tellnamename()
#e1.whoismyboss()

'''


'''
class person:                                     #SuperClass
    def __init__(self,name,id):
        self.name=name
        self.id=id

class employee(person):                           #DriveClass 
    def __init__(self,name,id,dept,designation):
        self.dept=dept
        self.designation=designation
        person.__init__(self,name,id)  #superclass ke andar constructor banaya hai tabhi ye likhenge

    def display(self):
        print("Employee name:",self.name,"id is:",self.id,"And department:",self.dept,"having designation:",self.designation)




e1=employee("Ankush",20,"IT","Accountant")
e1.display()

e2=employee("Sachin",29,"HR","Intern")
e2.display()
'''

'''
class person:                                     #SuperClass
    def __init__(self,name,id):
        self.name=name
        self.id=id

class employee(person):                           #DriveClass 
    def __init__(self,name,id,dept,designation):
        self.dept=dept
        self.designation=designation
        person.__init__(self,name,id)  #superclass ke andar constructor banaya hai tabhi ye likhenge

    def display(self):
        print("Employee name:",self.name,"id is:",self.id,"And department:",self.dept,"having designation:",self.designation)

class clerk(employee):
    def __init__(self,name,id,dept,designation):
        employee.__init__(self,name,id,dept,designation)


e1=clerk("Ankush",20,"IT","Accountant")
e1.display()

e2=clerk("Sachin",29,"HR","Intern")
e2.display()



'''




''' 
class employee:
    def tellname(self):    
        print("Hello World")
        
class boss(employee):
    def whoismyboss(self):
        print("I am your boss")
        
        
class manager(boss):
    def __init__(self,name):
        self.name=name
    def salary(self, name):
        print(self.name,"I have good salary")

m1=manager()
m1.tellname()
#m1.whoismyboss()
m1.salary()
e1=employee()
e1.tellnamename()
#e1.whoismyboss()
'''




'''
class Animal():
    def move(self):  #Abstract Function
        pass

class Human(Animal):
    def move(self):
        print("I can walk and run")
        
class Snake(Animal):
    def move(self):
        print("I can crawl")
        
class Dog(Animal):
    def move(self):
        print("I can bark")

R=Human()
R.move()
K=Snake()
K.move()
R=Dog()
R.move()
'''

'''
class Shape:
    def area(self):
        pass
    
class Rectangle(Shape):
    def __init__(self,x,y):
        self.l=x
        self.b=y
    def area(self):
        return self.l*self.b

class Square(Shape):
    def __init__(self,x):
        self.l=x
        def area(self):
            return self.l*self.l

r=Rectangle(10,20)    
s=Square(10)
print("Area:",r.area())
print("Area:",s.area())
'''


'''
class Point:
    def __init__(self,x):
        self.x=x
        
    def __add__(self,o):
        x=self.x+o.x
        return Point(x)

p1=Point(5)
p2=Point(6)
c=p1+p2
print(c,x)
'''
''' Employee Class 
class employee:
    def display(self):
        print("\n",self.name,self.emp_id)           
    
#create object        
e1=employee()
e1.name='Renu'
e1.emp_id=130
e1.display()

#create object 2
e2=employee()
e2.name='Geeta'
e2.emp_id=120
e2.display()

#create object 3 
e3=employee()
e3.name='Anju'
e3.emp_id=126
e3.display()

#creater object 4
e4=employee()
e4.name='Neena'
e4.emp_id=102
e4.display()

#create object 5
e5=employee()
e5.name='Sonia'
e5.emp_id=119
e5.display()
'''
''' Inheritance/Method Overridding
class A:
    def n(self):
        print("In class A")
        
class B(A):
    def n(self):
        print("In class B")
        
class C(A):
    def n(self):
        print("In class C")
        
class D(B,C):
    pass

obj=D()
obj.n()

A.n(obj)
C.n(obj)
'''


''' Super Class 
class a:
    def __init__(self,name,id):
        self.name=name
        self.id=id
       
    def getid(self):
        print("\n",self.name,"\n\n",self.id)
       
class b(a):
    def __init__(self,name,id,age):
        super().__init__(name,id)
        self.age=age
   
    def getid(self):
        super().getid()
        print("\n",self.age)
       

b1=b('Saurav',19,22)
b1.getid()
'''

''' Polymorphism

class Bird:
    def intro(self):
        print("There are many types of birds.")
       
    def flight(self):
        print("Most of the birds can fly but some cannot.")
   
class sparrow(Bird):
    def flight(self):
        #super().flight()
        print("Sparrow can fly.")
       
class ostrich(Bird):
    def flight(self):
        print("Ostrich cannot fly.")
       
obj_spr=sparrow()
obj_ost=ostrich()

obj_spr.intro()
obj_spr.flight()
obj_ost.intro()
obj_ost.flight()

'''




'''
class demo:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __mul__(self,e):
        r=self.a*e.a
        s=self.b*e.b
        print(r,s)
        
    def __sub__(self,e):
        r=self.a-e.a
        s=self.b-e.b
        print(r,s)
        
x=demo(2,4)
y=demo(3,2)
x-y
x*y
'''




''' Abstract Class 

import abc
    
class Animal():
    def move(self):
        pass
    
class Human(Animal):
    def move(self):
        print("I can walk and run")
        
class Snake(Animal):
    def move(self):
        print("I can crawl")
        
class Dog(Animal):
    def move(self):
        print("I can bark")
        
R=Human()
R.move()
K=Snake()
K.move()
R=Dog()
R.move()
        '''
        
        
        
        
        
        
'''        
class employee:
    emp_name=input("Employee name:")
    emp_age=int(input("Employee age:"))
    emp_salary=int(input("Employee salary:"))
    emp_address=input("Employee address:")
    def show(self):
        print(self.emp_name,self.emp_age,self.emp_salary,self.emp_address)
        
    
    
#create object        
e1=employee()
e1.show()


#create object 2
e2=employee()
emp_name='M'
emp_age=18
emp_salary=2000
emp_address='Punjab'
e2.show()      

'''  
        
'''        
class employee:
    emp_name='S'
    emp_age=10
    emp_salary=1000000
    emp_address='Delhi'
    def show(self):
        print(self.emp_name,self.emp_age,self.emp_salary,self.emp_address)
        
    
    
#create object        
e1=employee()
e1.show()


#create object 2
e2=employee()
employee.emp_name='M'
employee.emp_age=18
employee.emp_salary=2000
employee.emp_address='Punjab'
e2.show()              
        
'''        
        
  
        
  
'''        
class employee:
    emp_name=input("Employee Name:")
    emp_age=int(input("Employee Age:"))
    emp_salary=int(input("Employee Salary:"))
    emp_address=input("Employee Address:")
    def show(self):
        print("\nEmployee Name:",self.emp_name,"Employee Age:",self.emp_age,"Employee Salary:",self.emp_salary,"Employee Address:",self.emp_address)
        
    
    
#create object  
print("\nFor Employee 1\n")      
e1=employee()
e1.show()        

    
#create object 2

e2=employee()
employee.emp_name=input("Employee Name:")
employee.emp_age=int(input("Employee Age:"))
employee.emp_salary=int(input("Employee Salary:"))
employee.emp_address=input("Employee Address:")
print("\n\nFor Employee 2\n")
e2.show()         
        
  '''      
        
        
        
        
        
        
        
        
        
        
  
        
  