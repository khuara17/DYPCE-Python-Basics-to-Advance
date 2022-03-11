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
# x = p[3:9]
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
# print('abcd' == 'abcd')


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


############ List  ################
'''1. Lists are used to store multiple items in a single variable.
   2. List items are  changeable(Mutable), and allow duplicate values.
   3. List items are indexed, the first item has index [0], the second item has index [1] and so on...
   4. Lists are written with square brackets.
   5. list can have any datatype in it.'''

   ############# List Methods ###############
'''
     Method	    Description

    append()	Adds an element at the end of the list
    clear()	    Removes all the elements from the list
    copy()	    Returns a copy of the list
    count()	    Returns the number of elements with the specified value
    extend()	Add the elements of a list (or any iterable), to the end of the current list
    index()	    Returns the index of the first element with the specified value
    insert()	Adds an element at the specified position
    pop()	    Removes the element at the specified position
    remove()	Removes the item with the specified value
    reverse()	Reverses the order of the list
    sort()	    Sorts the list
'''


############ Defination #############

mylst = [4,5.6,'hjhd',[456,'sdfkdj',6.7,['type']]]

print(mylst[3][3][0])

### Removing List items ############


##### Change the element of the list


####### Accessing Elements of list #######


###### Adding an element ######


############## Special Methods #############



########### Tuple ##################
''' 1. Tuples are used to store multiple items in a single variable.
    2. Tuple items are unchangeable(Immutable), and allow duplicate values.
    3. Tuples are written with round brackets. '''


'''

Method	        Description
count()	    Returns the number of times a specified value occurs in a tuple
index()	    Searches the tuple for a specified value and returns the position of where it was found
'''