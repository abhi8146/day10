'''

# ! Method riding
# * Ploymorphism in classes
class bank:
    def ratio(self):
        print("All banks has repo rate")

class SBI(bank):
    def ratio(self):
        print("SBI rate is 9%")

class IOB(bank):
    def ratio(self):
        print("IOB rate is 7.5%")

i = IOB()
i.ratio()

s = SBI()
s.ratio()



# ? Eg:2
class USA:
    def langauge(self):
        print("English")

    def capital(self):
        print("washington DC")

class India(USA):
    def langauge(self):
        print("None")

    def capital(self):
        print("New delhi")

I = India()
I.langauge()
I.capital()



# Eg:3
 Ploymorphism using bjects

# c1, c2---> c1 = print(c1),print(c2)
# f1, f2

# * Eg:4
class c1:
    def f1(self):
        print("class 1")

class c2(c1):
    def f1(self):
        super().f1()
        print("class 2")

obj1 = c2()
obj1.f1()

# obj2 = c1()
# obj2.f1()

def display(a):
    a.f1()
display(obj1)
display(obj2)

# * Changing the functionality of builtin functions
class shooping:
    def __init__(self,l1):
        self.items = l1

    def__len__(self):
        length = len(self.items)
        return length

s.item_list([1,2,3,4,5])
print(len(s))

# ! -----> Method overloading
# ! Eg:1
class suming:
    def add(self,a,b):
        print(a+b)

    def add(self,a,b,c):
        print(a+b+c)

s = suming()
s.add(4,3)# ! ---> error
s.add(4,5,1)

'''

# ! Eg:2
class summing:
    def add(self, a=none, b=none, c=none):
        if a ! = None and b!=None and c!=None:
            print(a+b+c)
        elif a!=None and b!=None:
            print(a+b)
        else:
            print(a)

obj = summing()
obj.add(2)
obj.add(3,4)
obj.add(1,2,3)

# ! ------> Abstraction
---> The process if hiding the implimentation details is abstraction.

# ? Eg:1
from abc import ABC, abstractmethod
class shapes(ABC):
    @abstractmethod
    def sides(self):
        print("All shapes have sides except circle")

class triangle(shapes):
    def triangle_sides(self):
        print("3 sides")

    def name(self):
        print("I am triangle")

    def sides(self):
        pass

class square(shapes):
    def sqaure(self):
        print("4 sides")

tr = triangle()
tr.triangle_sides()
tr.name()

# -->Rules to define abstract class1 :

#1.) Abstract class cannot be instantiated
#2.) From abc import ABC, abstract method
#3.) Subclass the normal class with ABC
#4.) Convert the normal method inside the abstract class to abstract method
#5.) All the child classes have to be subclassed with abstract class
#6.) The abstract method should be present in the child classes


# ! Eg:2
# super()---> used to access the parent class method from child class method

from abc import ABC,abstract method
class c1(ABC):
    @abstractmethod
    def m1(self):
        print("This is abstract class")

class c2(c1):
    def m2(self):
        super().m1()
        print("Iam child 1")

    def m1(self):
        pass
class = c2()
class2.m2()

# Eg:3
from abc import ABC,abstract method
class password:
    @abstractmethod
    def pwd(self):
        pswd = "Abhi"
        return pswd

class login(password):
    def validate(self,name,password):
        if super().pwd()==password:
            print("welcome",name,'!!')
            print("login successfull")
        else:
            print("please check the password")

    def pwd(self):
        pass

login = login()
name = input("Enter the name")
pwd = input("Enter the password:")
login.validate(name,pwd)

# ! Encapsulation

# * Eg:1

class car:
    __name = "BMW"# private variable
    print(__name)

c1 = car()
print(c1.name) # error
c1.name = "Audi"
print(c1.name) # error

# --->Eg:2
---> Accessing private date outside the class
class c1:
    __phone = '9876545698'

    def display(self):
        print(self.__phone)
c = c1()
c.display()

# Eg:3
--->Declare private method
class class1:
    def m1(self): # private method
        print(Iam private method")

    def __init__(self):
        self.__m1()

c = class1()
c.__m1() # error             
              
        
# ? Nested class

class class1:
    class class2:
        name = "Abhi"

        def display(self):
            print(self.name)
    obj1 = class2()

obj = class()
obj.obj1.display()
s







