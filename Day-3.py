##### Multingle Strings #########

### Syntax ###

mystring = ''' this is my first program
 I love programming 
 I love python ''' 

m = "I love python" 


##### len()  ########
 
# print(  len(m)  )

######### String Slicing ###########

# If accessing single index and out of range :- error
# If accessing range(slicing) and out of range :- It will go till last index and stop.

p = "banana"

# x = p[1:6]
# x = p[:9]
# x = p[9]

x = p[-3:-1]

# print(x)


######## String Formatting #######

# Method 1
age = 28
friendage = 24
myage = "My age is {} and my friend age is {}".format(friendage,age)

# print(myage)


# Method 2
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {1} dollars for {0} pieces of item {1}."

# print(myorder.format(quantity, itemno)) 

# Method 3

# print(f"I want to pay {'mystr****'} dollars for {itemno} pieces of item {12}")

###### Functions for string ###############

a = " heLlo world!"

# print(a.upper())
# print(a.lower())
# print(a.capitalize())
# print(a.islower())
# print(a)
# print(a.strip())
# print(a.replace("o","P"))
# print(a.split(","))
# print(a.count('l'))
# print(a.find('o',6,10))
# print(' abcd' == 'abcd')


##### String concatenation #########

a = 'Naruto'
b = 'Uzumaki'

# print(a + ' Minato ' + b)



####### Escape characters ###########

x = "Book \tname \n is \'bhagwatgita\""
# print(x)

a = 6
c = 9.5
x = 'rty'


