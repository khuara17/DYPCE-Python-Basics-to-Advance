###################### Inheritance #####################
'''
Inheritance is the capability of one class to derive or inherit the properties from another class. 

The benefits of inheritance are: 
1. It represents real-world relationships well.
2. It provides reusability of a code. We don’t have to write the same code again and again. 
3. Also, it allows us to add more features to a class without modifying it.

Syntax:-

class BaseClass:    --- Parent class
    Body of base class

class DerivedClass(BaseClass):   --- Child Class.
    Body of derived class
'''

class Person:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname= lname

    def printname(self):
        print(self.fname,self.lname)

# class Student(Person):
#     def __init__(self,fname,lname):
#         Person.__init__(self,fname,lname)
#         print("I am child Class")

class Student(Person):
    def __init__(self,fname,lname,schoolname):
        super().__init__(fname,lname)
        # print("I am child Class")
        self.graduationyear = 2019
        self.schoolname = schoolname

    def printname(self):
        print("Hi I am base class")

    
# x = Student('ramesh','shah','xyz')
# x.printname()

######################### Different forms of Inheritance ##################'

'''
Base Cases:-

class A():
    pass
class B():
    pass

'''
'''
1. Single inheritance:- 

When a child class inherits from only one parent class, it is called single inheritance.

Example:    
    class c(A):
        pass
'''


'''
2. Multiple inheritance:- 

When a child class inherits from multiple parent classes, it is called multiple inheritance. 


Example:    
    class c(A,B):
        pass
'''

class Base1:
    def __init__(self) -> None:
        # super(Base1,self).__init__()
        self.myattr1 = 'Base1'

class Base2:
    def __init__(self) -> None:
        # super(Base2,self).__init__()
        self.myattr2 = 'Base2' 

class Base3:
    def __init__(self) -> None:
        # super(Base3,self).__init__()
        self.myattr3 = 'Base3' 

class Derived(Base1,Base2,Base3):
    def __init__(self) -> None:
        print("Derived")
        super(Derived,self).__init__()
        print(self.myattr2)
        
    
    def printPrentattr(self):
        print(self.myattr1,self.myattr2,self.myattr3)

# ob = Derived()
# ob.printPrentattr()


'''

3. Multilevel inheritance: 

When we have a child and grandchild relationship. 

A - B - C

Example:    
    class c(B):
        pass

    class B(A):
        pass
'''

class Base:
    def __init__(self,name) -> None:
        self.name = name

    def getName(self):
        print(self.name)

class Child(Base):
    def __init__(self,name,age) -> None:
        # super().__init__(name)
        Base.__init__(self,name)
        self.age = age

    def getAge(self):
        print(self.age)

class Grandchild(Child):
    def __init__(self,name,age,address) -> None:
        Child.__init__(self,name,age)
        self.address = address
        print(self.name,self.age,self.address)


    def GetAddr(self):
        print(self.address)
        


# myclass = Grandchild('Reva',20,'Mumbai')
# myclass.getAge()
# myclass.getName()
# myclass.GetAddr()


'''

4.  Hybrid inheritance: 

This form combines more than one form of inheritance. Basically, 
it is a blend of more than one type of inheritance.    

Example:    
    class c(B,D):
        pass

    class B(A):
        pass
'''
class Test:
    pass
class Base:
    def __init__(self,name) -> None:
        self.name = name

    def getName(self):
        print(self.name)

class Child(Base):
    def __init__(self,name,age) -> None:
        # super().__init__(name)
        Base.__init__(self,name)
        self.age = age

    def setAge(self):
        print(self.age)

class Grandchild(Test,Child):
    def __init__(self,name,age,address) -> None:
        Child.__init__(self,name,age)
        self.address = address
        print(self.name,self.age,self.address)


    def GetAddr(self):
        print(self.address)


Myclass = Grandchild('Reva',20,'Mumbai')
