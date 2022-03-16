####### Python Classes/Objects ########## 
'''

Python is an object oriented programming language.

Almost everything in Python is an object, with its properties and methods.

A Class is like an object constructor, or a "blueprint" for creating objects.

'''


'''Syntax'''
# class ClassName:
#     Body


class point:
    '''This is a Doctstring for my class'''
    x = 4
    y = 5


# x = point() #x == Object of class , point() == Class Initialization.
# r = point()
# print(x,r)
# print(x.__doc__)
# print(r.y)



############# The __init__() Function ############
''' 

The examples above are classes and objects in their simplest form, 
and are not really useful in real life applications.

To understand the meaning of classes we have to understand the built-in __init__() function.

All classes have a function called __init__(), which is always executed when the class is being initiated.

Use the __init__() function to assign values to object properties, or 
other operations that are necessary to do when the object is being created:

'''
######## The self Parameter:-  ##########
''' 
The self parameter is a reference to the current instance of the class, and
 is used to access variables that belongs to the class.

It does not have to be named self , you can call it whatever you like,
 but it has to be the first parameter of any function in the class:

'''

# Variable :- Local Variables
# Attributes  :- We define these with self.


# class Person:
#     def __init__(self,name,age=78):
#         self.name = name
#         self.age = age
#         v = 20
#         print(self.name+str(self.age))
    
#     def greet(self):
#         print(f"Hello, how are you {self.name}")

class Person:
    def __init__(name,age=78):
        pass
        # myself.name = name
        # myself.age = age
        # v = 20
        # print(myself.name+str(myself.age))
    
    def greet(myself):
        print(f"Hello, how are you {myself.name}")


p1 = Person('john') # self.name = 'john'
p2 = Person("Mary", 23) # self.name , 
# p2.greet()

# print(p1.name,p2.name)
# print(p1.age,p2.age)



############# Object Methods &  The self Parameter
'''
Object Methods
Objects can also contain methods. Methods in objects are functions that belong to the object.
'''




