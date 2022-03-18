# ######## Lamda function ############
# '''
# A lambda function is a small anonymous function.

# A lambda function can take any number of arguments, but can only have one expression.

# Syntax
# lambda arguments : expression

# The expression is executed and the result is returned:
# '''
# # Example
# # Add 10 to argument a, and return the result:

# # def x(a):
# #   return a+ 10

# # print(x(5))

# # x = lambda a,b : a + b+ 10
# # print(x(5,5))
# def myfunct(n):
#   return lambda a : a * n

# # def myfunct(n):
# #   def x(a):
# #     return a * n
# #   return x

# def x(a):
#   return a *2
  
# # x = myfunct(2)
# # print(x(5))




# ######### Encapsulation  ########
# '''Using OOP in Python, we can restrict access to methods and variables.
#  This prevents data from direct modification which is called encapsulation.
#   In Python, we denote private attributes using underscore as the prefix 
#   i.e single _ or double __.
#   '''

# class Computer:
#   def __init__(self):
#     self.__maxprice = 900
  
#   def sell(self):
#     print(f"The seeling prices is {self.__maxprice}")

#   def setmaxprice(self,price):
#     self.__maxprice = price

# class Derived(Computer):
#   def __init__(self):
#     Computer.__init__(self)
#     self.__maxprice = 199
#     print("Calling private attr of Parent class",self.__maxprice)


# c = Computer()
# c.sell()

# # Change the price
# c.__maxprice = 1000
# c.sell()

# # Change the price using the setter method
# c.setmaxprice(1000)
# c.sell()

# d = Derived()


# ######### Polymorphism #####
# '''
# Polymorphism is an ability (in OOP) to use a common interface for multiple forms (data types).

# Suppose, we need to color a shape, there are multiple shape options (rectangle, square, circle).
# However we could use the same method to color any shape. This concept is called Polymorphism.

# '''
# class Parrot:
#   def fly(self):
#     print("Parrots can fly")

#   def swim(self):
#     print("Parrots cannot swim")


# class Penguin:
#   def fly(self):
#     print("Penguin cannot fly")

#   def swim(self):
#     print("Penguin can swim")

# class Dog:
#   def bark(self):
#     print("Dog can bark")
# ## Common Interface

# def flying_test(bird):
#   bird.fly()

# ## Objects for classes
# p = Parrot()
# Pe = Penguin()
# d = Dog()
# ### Passing the object
# flying_test(p)
# flying_test(Pe)
# flying_test(d)


####### Abstraction ########
'''
Abstraction is used to hide the internal functionality of the function from the users. 
The users only interact with the basic implementation of the function, but inner working is hidden. 
User is familiar with that "what function does" but they don't know "how it does."

In simple words, we all use the smartphone and very much familiar with its functions such as camera, 
voice-recorder, call-dialing, etc., but we don't know how these operations are happening in the background. 

Let's take another example - When we use the TV remote to increase the volume. 
We don't know how pressing a key increases the volume of the TV.
 We only know to press the "+" button to increase  the volume.
 '''
#### Method 1

# import AbstractFile

# AbstractFile.Helloworl()
# print(AbstractFile.x)

# obj = AbstractFile.Base()

### Method 2

from AbstractFile import Base,x

# print(x)

# obj = Base()

class Derived(Base):
  def __init__(self):
    Base.__init__(self)
    print("I am Derived")

x = Derived()