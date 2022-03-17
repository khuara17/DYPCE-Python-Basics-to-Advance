class Person:
    def __init__(myself,name,age=78):
        myself.name = name
        myself.age = age
    
    def greet(myself):
        print(f"Hello, how are you {myself.name}")

# ramesh = Person('Ramesh',67)

############# Modify Object Properties #######
# print(ramesh.age)
# ramesh.age = 68
# print(ramesh.age)

########### Delete Object Properties ###########

# del ramesh.age
# del Person.greet
# print(ramesh.greet())

######### Problem 1 ################

'''
Create a class names Mobile

Take Input as brand name, price and ram

create a function with name WillItWork in the class that will tell whether phone can be used 
for gaming
ram less than 3 gb -- It wont work
ram is between 3 to 4 -- It will work fine
ram is greater than 4 --  It will Work perfectly.
'''

class Mobile:
    def __init__(self,brand_name,price,ram):
        self.brand = brand_name
        self.ram = ram
        self.price = price

    def WillItWork(self):
        if self.ram < 3:
            print('It wont work')
        elif self.ram >= 3 and self.ram <4:
            print('It will work fine')
        else:
            print('It will Work perfectly.')

# a = Mobile('Apple', 60 , 6)
# b = Mobile('Samsung', 20, 2)
# a.WillItWork()
# b.WillItWork()
    
############## Passing Objects to Classes and function ############
#x^2 + 1

def square(x):
    return x * x

# def solve(s,x,a):
#     op = s(x) + a
#     return op

# res = solve(square,4,2)
# print(res)
# x = 6

# print(square(6))
# print(square)

### Sort the cars according to proces in asc and return the prices n asc order.

class Car:
    def __init__(self,Brand,Price):
        self.brand = Brand
        self.price = Price

# class Showroom:

#     def SortCars(self,lst):
#         out = []
#         for i in lst:
#             out.append(i.price)
#         out.sort()
#         return out


class Showroom:
    def returnobj(self,obj):
        return obj.price

    def SortCars(self,lst):
        #lst = [Ford,Maruti,Ferarri]
        lst.sort(key=self.returnobj)
        return lst


Ford = Car('Ford', 60000)
Maruti = Car('maruti',40000)
Ferarri = Car('Ferarri',80000)
Ford.price

res = [1,2,3]
for i in res:
    print(i)
xyz = Showroom()
res = xyz.SortCars([Ford,Maruti,Ferarri])
for i in res:
    print(i.brand,i.price)



# lst = ['Ramesh','Mahesh','mahesh']
# lst.sort(key=str.lower)
# print(lst)
