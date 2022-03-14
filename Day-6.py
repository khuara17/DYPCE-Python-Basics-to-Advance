# a = 1000
# b = 1000
# counter= 2
# print(id(a),id(b))
# a = a + 6
# counter = 1
# b += 1
# counter = 0
# print(id(a),id(b))
# print(a is b)
# print(a==b)


#             1500  <-b  , 1001 <- a
#  988            998  
# counter = 0
# a = 1000
# b = 1000
# b = 1500
# a = 1001



########## Function Defination (Function Declaration) ###########

'''
def function_name(arguments):
    Body/Logic.

'''
def myfunction(x:int,y:int,z=10) -> int:
    '''
    x : int
    y : int
    This function does addition operation
    '''
    print(x,y,z)
    return x + y + z

t,v = 8,9


######## Function Call ########

# myfunction(t,v) # When function is returning nothing
x = myfunction(t,v) # When function is returning Some values
print(x)

############### DocString ########

# print(myfunction.__doc__)

## Create a function that takes 3 inputs i.e, two operand and 
# one operator and wil return the output according to the operator


# x = input("Enter a number: ")
# print(type(x))


############ Calculator #############

# Input(Consider Datatypes) --> Logic --> Output Formatting

# 2 + 3 



# Input :- 2 Operands(Int,Float) and 1 Operator (str)
# Output :- Int , Float


############ Input ##################

# x = int(input("Enter The first Number: "))
# y = int(input("Enter the second number: "))
# z = input("Enter the operator: ")
# print(type(x))

######## Logic Part ###########
def calculator(a,b,c):
    c = a+b
    return c
    # if c == '+':
    #     return a+b
    # elif c == '-':
    #     return a-b
    # elif c == '*':
    #     return a * b
    # elif c == '/':
    #     return a/b
    # else:
    #     return "Wrong Operator entered..."
x = 7
y = 8
# res = calculator(x,y,8)

########## Output #######

# print(f"Output of Operaion is: {res}. ")


############# Arbitrary Arguments, *args ###########
'''
1. If you do not know how many arguments that will be passed into your function,
    add a * before the parameter name in the function definition.
2. It will create a tuple of values.    
'''

def addition(t,*numbers):
    sum = 0
    for i in numbers:
        sum += i
    return t, numbers

# print(addition(2,3,4,5))

############ Keyword Arguments, **kwargs ###########
'''
1. You can also send arguments with the key = value syntax.
2. It will create a dictonary of key-value pairs.
'''

def averageMarks(**marks):
    average = 0
    for i in marks.values():
        average += i
    # average = (marks['ravi']+marks['sangeeta']+marks['anmol'])/3
    average /= len(marks)
    print(marks)
    return average

# print(averageMarks(ravi=30,sangeeta=78,anmol=80))



############# Problem 1 ################
''' Write a function that stutters a word as if someone is struggling to read it. 
The first two letters are repeated twice with an ellipsis ... and space after each, and 
then the word is pronounced with a question mark ?.

Examples
stutter("incredible") ➞ "in... in... incredible?"

stutter("enthusiastic") ➞ "en... en... enthusiastic?"

stutter("outstanding") ➞ "ou... ou... outstanding?"

Notes
Assume all input is in lower case and at least two characters long. '''


def stutter(word):
    pass



########## Passing list or other datatype as an input ############

ls = [2,3,4,5]
MyTuple = (3,4,0)

def MyFunction(mylist,mytuple):
    for i in mylist:
        print(i)

MyFunction(ls,MyTuple)

################# Problem 2 ################

'''In this challenge, a farmer is asking you to tell him how many legs can be counted among all his 
animals.
The farmer breeds three species:
chickens = 2 legs
cows = 4 legs
pigs = 4 legs
The farmer has counted his animals and he gives you a subtotal for each species.
 You have to implement a function that returns the total number of legs of all the animals.
(chickens,cows,pigs)
Examples
animals(2, 3, 5) ➞ 36
animals(1, 2, 3) ➞ 22
animals(5, 2, 8) ➞ 50
'''

chicleg=2
cowleg=4
pigleg=4
def animals(chicken,cows,pigs):
    ## Code
    return No_of_legs


# chickens=int(input("Enter no of chickens:"))
# cows=int(input("Enter no of cows:"))
# pigs=int(input("Enter no of pigs:"))
# print(animals(chickens,cows,pigs))


###################### Problem 3 ##############

'''

ARS Gems Store sells different varieties of gems to its customers.

Write a Python program to calculate the bill amount to be paid by a customer 

based on the list of gems and quantity purchased.

Any purchase with a total bill amount above Rs.30000 is entitled for 5% discount.
 
 If any gem required by the customer is not available in the store, 
 
 then consider total bill amount to be -1.

Assume that quantity required by the customer for any gem will always be greater than 0.

Perform case-sensitive comparison wherever applicable.

'''
# discount amount = total amount - (total amout * (discount/100))

def calculate_bill_amount(gems_list, price_list, reqd_gems,reqd_quantity):
    bill_amount=0
    #Write your logic here
    return bill_amount

#List of gems available in the store
gems_list=["Emerald","Ivory","Jasper","Ruby","Garnet"]

#Price of gems available in the store. gems_list and price_list have one-to-one correspondence
price_list=[1760,2119,1599,3920,3999]

#List of gems required by the customer
reqd_gems=["Ivory","Emerald","Garnet"]

#Quantity of gems required by the customer. reqd_gems and reqd_quantity have one-to-one correspondence
reqd_quantity=[3,10,12]

# bill_amount=calculate_bill_amount(gems_list, price_list, reqd_gems, reqd_quantity)
# print(bill_amount)

# 2119*3 + 1760 * 10 + 12* 3999


######## Scope (Local and Global Variables) ###########
# global : y = 40, x = 90
# local :  

# y = 40
# x = 90
# y = 00

def myfunction():
    global y 
    y = 30
    # def myinsidefunction():
        # z = 20
        # print(x) 
    # myinsidefunction()
    
    # x = x + y
    print(y)

# myfunction()
# print(y)
# print(x)