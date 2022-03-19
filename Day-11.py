######### Precendance & Associativity ##########
'''
Category	        Operator	        Associativity

Postfix	            () []           	Left to right
Multiplicative  	* / %	            Left to right
Additive	        + -	                Left to right
Shift	            << >>	            Left to right
Relational	        < <= > >=	        Left to right
Equality	        == !=	            Left to right
Bitwise AND	            &	            Left to right
Bitwise XOR	            ^	            Left to right
Bitwise OR	            |	            Left to right
Assignment	        = += -= *= /= %=>>= <<= &= ^= |=	Right to left
Comma	                    ,	                Left to right
'''

# x = 6 + (7*8) / 2 * 3 - 6 + 1

# 336 / 2 * 3 - 6 + 1

# print(x)




############ Recursion #################
'''
1.  Recursion means that a function calls itself. 
    This has the benefit of meaning that you can loop through data to reach a result.
2.  should be very careful with recursion as it can be quite easy to slip into  writing a function
    which never terminates, or one that uses excess amounts of  memory or processor power.
3.  Every recursive function must have a base condition that stops the recursion or 
    else the function calls itself infinitely.
4.  However, when written correctly recursion can be a very efficient and mathematically-elegant 
    approach to programming.
5.  The Python interpreter limits the depths of recursion to help avoid infinite recursions,
    resulting in stack overflows.
6.  By default, the maximum depth of recursion is 1000.
    If the limit is crossed, it results in RecursionError.
'''

######## Advantages of Recursion ###########
'''
1. Recursive functions make the code look clean and elegant.
2. A complex task can be broken down into simpler sub-problems using recursion.
3. Sequence generation is easier with recursion than using some nested iteration.
'''
################# Disadvantages of Recursion #########
'''
1. Sometimes the logic behind recursion is hard to follow through.
2 .Recursive calls are expensive (inefficient) as they take up a lot of memory and time.
3 .Recursive functions are hard to debug. '''


############## Examples ###########

# def myfunction():
#    myfunction()

# def myfunction2():
#     print(myfunction())

# myfunction()







######  Write a function to display factorial of number ##############

# 6! =  6 * 5 * 4 *   3 * 2 * 1


# n= 3

# fact=1

# if n==0:
#     print("factorial: ",fact)
# elif n<0:
#     print("factorial does not exist")
# else:
#     for i in range(1,n+1):
#         fact=fact*i
#     print("Factorial: ",fact)

# 6! =  6 * 5 * 4 *   3 * 2 * 1

#3

def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n-1)

# |             |
# | 2 * Fact(1) |
# | 3 * fact(2) |
# _______________

# Fact(3) = 3 * fact(2)= 3 * 2 = 6
# Fact(2) = 2 * Fact(1) = 2 * 1 = 2
# Fact(1) = 1


######### problem 2 ############

''' Write a function to calaulate sum of first n numbers. 

ex: n = 3 
op == 6  ( 3 + 2 +1 )
'''

def addition(n):
    sum = 0
    for i in range(n+1):
        sum += i
    return sum

# print(addition(3))


# 4 + 3 + 2 + 1
def addition_Rec(n):
    if n == 1:
        return 1
    else:
        return n + addition_Rec(n-1)

# addition_Rec(3)  === 3 + addition_Rec(2)   __3___    <------
#                                                            |
# addition_Rec(2)  === 2 + addition_Rec(1) <-   ===> 3  ------
#                                           |
# addition_Rec(1)  ==== 1    ---------------

# addition_Rec(2)  === 2 + 1 = 3

# addition_Rec(3)  === 3 + 3 = 6



# print(addition_Rec(3))


# |                      |
# | 2 + addition_Rec(1)  |
# | 3 + addition_Rec(2)  |
# |___                   |












######## Problem 3 ########## 

'''Write a program to display first n elements of fibonacci series 

0 1 1  2 3                              5 8 13 21 ..................

1 2 3 4 5 6
'''

def fibo(n):
    f1 = 0
    f2 = 1
    if n < 1:
        return 
    print(f1,end="->")
    for c in range(1,n):
        print(f2,end="->")
        next = f1 + f2
        f1 = f2
        f2 = next
# fibo(5)    


def fibonacci(n): # n = no of elements
    if n == 1:
        return 1
    elif n < 0:
        return 0
    elif n == 0:
        return 0
    else:
        return fibonacci(n-1)+fibonacci(n-2)
n = 3
# for i in range(n):
#     print(fibonacci(i))        



#                                           fibonacci(3)   == 2   
#                   fibonacci(2)  == 1                +               fibonnaci(1) == 1    
#               
#               fibonaaci(1) + fibonaaci(0)                         
#                   1               0                                   




################# Min, Max, Sum ##########

# print(min(3,4))
# print(max(3,4))
# x = (2,3,4)
# print(sum(x))


x = ['ravi','ram','vishal']
# print(min(3,4,5,6))
# print(max(x))

# print(sum(x))

############### Round #############
# 4 4.5 5
# print(round(4.5648,3))
# print(type(round(4.3678)))

############# enumerate ###############

x = ['ravi','ram','vishal',78,7.7]

y = enumerate(x,10)
# for i,j in y:
#     print(i,j)
# print(y)

# e,r,t=(3,4,5)

# for i,j in enumerate(x):
#     print(i,j)


############## Eval ##################
a = 4
# print(eval('a+5'))

############# Slice ##############

# slice(start,end,steps)

myls = ['a','b','c','d','e','t','i','o']
# mtls[0:2]
x = slice(1,8,3)
# print(x)
# print(myls[x])


############### Sorted #################
'''
The sorted() function returns a sorted list of the specified iterable object.

You can specify ascending or descending order. Strings are sorted alphabetically, 
and numbers are sorted numerically.

Note: You cannot sort a list that contains BOTH string values AND numeric values.
'''

# Syntax
# sorted(iterable, key=key, reverse=reverse)
# def example(tup):
#     return tup[0]

# a = ["h", "b", "a", "c", "f", "d", "e", "g"]
# x = sorted(a, reverse=False)
# print(a)
# print(x)
# y = a.sort(reverse= False)
# print(y)
# print(a)

# x = [(2,3),(89,5),(9,0)]
# x = sorted(x, key=lambda tup:tup[1] , reverse=False)
# print(x)

# x.sort()


################### getattr ################3
'''
The getattr() method returns the value of the named attribute of an object.
If not found, it returns the default value provided to the function.'''
'''
The syntax of getattr() method is:
getattr(object, name)


The above syntax is equivalent to:
object.name
'''

class Person:
    age = 23
    name = "Adam"

person = Person()
print('The age is:', getattr(person, "address"))
print('The age is:', person.age)









'''
EXCEPTIONS              Desciption

Exception           Base class for all exceptions

ArithmeticError     Base class for all errors that occur for numeric calculation.

OverflowError       Raised when a calculation exceeds maximum limit for a numeric type.

FloatingPointError  Raised when a floating point calculation fails.

ZeroDivisionError   Raised when division or modulo by zero takes place for all numeric types.

AttributeError      Raised in case of failure of attribute reference or assignment.

EOFError            Raised when there is no input from either the raw_input() or input() function and the end of file is reached.

ImportError         Raised when an import statement fails.

KeyboardInterrupt   Raised when the user interrupts program execution, usually by pressing Ctrl+c.

IndexError              Raised when an index is not found in a sequence.
	
KeyError                Raised when the specified key is not found in the dictionary.

NameError               Raised when an identifier is not found in the local or global namespace.

UnboundLocalError       Raised when trying to access a local variable in a function or method but no value has been assigned to it.

EnvironmentError        Base class for all exceptions that occur outside the Python environment.
	
IOError                 Raised when an input/ output operation fails, such as the print statement or the open() function when trying to open a file that does not exist.

IOError                 Raised for operating system-related errors.

SyntaxError             Raised when there is an error in Python syntax.

IndentationError        Raised when indentation is not specified properly.

SystemError             Raised when the interpreter finds an internal problem, but when this error is encountered the Python interpreter does not exit.
		
ValueError              raised when the built-in function for a data type has the valid type of arguments, but the arguments have invalid values specified.
'''

# x = 2
# c = {
#     2 : 'z'
# }
# try:
#     print(x)
#     # print(c[4])
#     # x = x / 0
# # except ZeroDivisionError:
# #     print("ZeroDivisionError has occured...")
# except Exception as e:
#     print("Some Error has occured..."+str(e))
# else:
#     print("I am else part")
# # except KeyError as i:
# #     print("Keyerror has occured"+ str(i))
# # except IndentationError:
# #     print("Intendatio error")
# # except Exception as e:
# #     print("Some Error has occured..."+str(e))
# finally:
#     print("I will get executed everytime..")
