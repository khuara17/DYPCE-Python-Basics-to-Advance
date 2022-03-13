###### Keywords ##########
# Keywords in Python programming language

# False	await	else	import	pass
# None	break	except	in	raise
# True	class	finally	is	return
# and	continue	for	lambda	try
# as	def	from	nonlocal	while
# assert	del	global	not	with
# async	elif	if	or	yield


########## Variable  ####################

''' Variables are containers to store data '''

'''
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)'''

# Can start with: a-z, A - z , _
# Cannot start with : 0-9
# Can Contain : A-Z, a-z, 0-9, _
# Cannot Contain : @, $ , % ,& , ^

########### If else ###############

'''
if condition:
    statement
else:
    statement
    '''
# "H" in "hello"
# print(4>3)
# if "H" in "hello":
#     print("4 is greater")
# else:
#     print("4 is not greater")



### elif = else if #############
'''
if condition:
    statement
elif condition:
    statement
else:
    statement
    '''
# t = 56

# if t < 56:
#     print("part 1")
# elif t == 56:
#     print("part 2")
# elif t <= 56:
#     print("part 2.5")
# else:
#     print("part 3")

# print("I am out of if")




################### for loops ##################

''' for '''
'''
for variable in range(start,endValue,Increment amount):'''

#### print numbers from 1 to 50 ##########

# for i in range(1,5,1):
#     print(i)

# i = 1 + 1 =2

## Assign the value to the variable
## Check the condition - (variable value is strictly less than end value)
## Execute whatever present in for loop
## Increment the value by whatever defined in for loop

## The conition in for loop is  "<" ,,, not <=

# i = 1
# i < 5
# print(1)
# i = i + 1


# i = 2
# 1 < 5
# print 2

# i = 3
# i < 5
# print 3

# i = 4
# i < 5
# print 4

# i = 5
# i < 5
# print 3


'''1. One parameter '''
## Default value :  start value == 0 and increment value == 1
# for i in range(5):
#     # if i == 2:
#     #     break
#     print(i)

'''2. Two parameter '''
## Default value : increment value == 1
# for i in range(3,6): 
#     print(i)


# i = 5
# i  = 5 > 1
# print(5)
# i = 5 - 1 = 4
# 4 > 1
# print(4)
# i = 4 -1 = 3
# 3 > 1
# print
# i = 3 - 1 =2
# i = 2 > 1
# print 2
# i = 2- 1 = 1
# 1 > 1


'''3. Three parameter '''
# for i in range(1,5,-1):
#     print(i)

####### While Loop #####################

''' 
Initialize variable 
whilw Check th condition 
if true: 
    then go to while loop 
    increment the variable
'''

# i = 0
# while i < 4:
#     print(i)
#     i = i + 1


#### break  ##############

# i = 0
# while i < 4:
#     if i == 2:
#         break
#     print(i)
#     i = i + 1
# print("h")

######## Continue ###########

# for i in range(9):
#     print(i)
#     if i == 3 or i ==7:
#         continue
    
# print(9)
# print(c)


######## Operators ###########

''' Arithmatic Operator '''
a = 7
b = 5
# Operator :- + , - , * , / , ** , // , %   :- Binary Operators.
# print(a**7)   # 7 ^ 7
# print(a//2) # x = 3.6 floor : 3 and ceil :- 4
# print(7%2)

# 7 / 2= 3.5


# print(a+b+6+7) # 12 + 6 = 18 + 7 = 25


############# Assignment operators ########

# Assignment op :- = , += , -= , *= , /= , **= , //=
x = 6 

x += 4 # x = x +4 = 6+4 = 10
x *= 2 # x = x * 2
# print(x)





### Bitwise operator ##############

# Bitwise Operator :- & ,  | , << , >> , ^ , ~
# 5 = 101

# 64 32 16 8 4 2 1  


print(5 | 7)
# 101             =   4 +  0 + 1 =   5  =   4 + 1   = 101
# |
# 111              = 4 + 2 + 1 = 7
# ----
# 111 = 7     

print(4 & 7)
# 100             =   4 +  0 + 1 =   5  =   4 + 1   = 101
# &
# 111              = 4 + 2 + 1 = 7
# ----
# 100 = 4   

a = 5   # ==  101 

# Right Shift 0000 0101 = 0000 0010 =  0000 00001 = 0+ 0 + 1 = 1
# a >>= 2
# print(a)

#Left Shift  0000 0101  = 0000 1010 = 0001 0100 = 20
a <<= 2  #  1010
print(a)
#XOR:- odd :- 1 and even :- 0 
t = 5
v = 7
c = t ^ v 
# 101             =   4 +  0 + 1 =   5  =   4 + 1   = 101
# ^
# 111              = 4 + 2 + 1 = 7
# ----
# 010 = 2
print(c) 

####### Comparison Operators ######## 

## Comparison Operators :- == ,!=, < , > , <= , >= 
a = 4
# print(a == 4)
# print(a!= 4)

# print(a > 6)   # 4 > 6 = False
# print(a < 6)   # 4 < 6 = True , 4 < 4 = False
# print(a <= 4)  # 4<= 4 = True
# print(a >= 4)  # 4 >= 4 = True

############# Logical Operators ######

# Logical Operators :  and, or , not
# True = 1 and False = 0 

# 4 < 5 and 5 > 6 =  False  ## If either one of the condition is false the output will be False else True
# 4 < 5 or 5 > 6 =  True   ## Either one of the condtion shoud be true.
# 
# print(not(4 < 5 or 5 > 6))

######## Identity Operators ##############

# Identity Operators : is , is not
# mystring = 'hello'
# m = "hello"
c = 'ee'
d = c
e = 'e' * 2
# print(c)
# print(e)

# print('ee' is 'e' * 2)

# print(c == e)
# print(c is e)
# print(c == d)
# print(c is d)

######## Membership Operators ##########

#Membership Operators : in , not in
m = "hello"
lst = [4,'yu',6.7,[34]]

# print('hellt' not in m)

# for i in lst:
#     print(i)

# if 4 in lst:
#     print('presnt')



################## Problem 1  ###############
'''
Create a program that takes a string and returns the number (count) of vowels contained within it.

Examples:-
count_vowels("Celebration") ➞ 5

count_vowels("Palm") ➞ 1

count_vowels("Prediction") ➞ 4

'''

#### Method 1 ########
# mystr = 'Aelebration'

# count=0
# v_list = ('a','e','i','o','u','A','E','O','I','U')

# for i in mystr:
#     if i in v_list:
#         count+=1
# print(count)


######### Method 2 #########

# x = 'celebration'
# count = 0

# for i in x:
#     if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
#         count = count + 1
# print(count)

####### Method 3 ##########

# vow = "aeiou"

# cnt = 0
# for i in a:
#     if i in vow:
#         cnt+=1
# print(cnt)

###### Space analysis of datatypes######
'''
>>> a = [1,2,3]
>>> a.__sizeof__()
64
>>> b = '123'
>>> b.__sizeof__()
54
>>> c = (1,2,4)
>>> c.__sizeof__()
48
>>> d = {1,2,3}
>>> d.__sizeof__()
200
>>> e = 123
>>> e.__sizeof__()
28
>>> f = {1:1,2:2,3:3}
>>> f.__sizeof__()
216
'''
