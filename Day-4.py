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

############ Special Functions ##############
mylst = [4,5.6,'hjhd',[456,'sdfkdj',6.7,['type']],34]
# mylst1 = ['Es','mgd','eS','es']
# x = mylst.copy()
x = mylst
x[0] = 90
# print(mylst)
# print(x)

# mylst.reverse()
# mylst1.sort(reverse=True,key=str.lower)

# salve
# # surve
# print(mylst1)
# print(x)
# print(mylst.count(34))


############ Defination #############

mylst = [4,5.6,'hjhd',[456,'sdfkdj',6.7,['type']]]


####### Accessing Elements of list #######

# print(mylst[3][3][0])

##### Change the element of the list

mylst[1:4] = [1,2,3,7,[12]]

###### Adding an element ######
mylst1 = 'ret'
# mylst.append(78)
# mylst.extend(mylst1)
# mylst.insert(2,'imto')

### Removing List items ############
mylst = [4,5.6,'hjhd',[456,'sdfkdj',6.7,['type']]]

# mylst.remove('hjhd')
x = mylst.pop()
del mylst[1]
# mylst.clear()
# print(mylst)
# print(x)

mylst = [4,5,'hello',[34,68,[44,5,'mumbai']]]
#1. Print Mumbai
# print (myslt[3][2][2])
# 2.  To change the value 44 to 67
# myslt[3][2][0]=67

# 3. to change the e from hello to t
# myslt[2][1] = 't'
# print(mylst[2].replace('e','t'))
# print(mylst)

########### Tuple ##################
''' 1. Tuples are used to store multiple items in a single variable.
    2. Tuple items are unchangeable(Immutable), and allow duplicate values.
    3. Tuples are written with round brackets. '''


'''

Method	        Description
count()	    Returns the number of times a specified value occurs in a tuple
index()	    Searches the tuple for a specified value and returns the position of where it was found
'''

mytple = (2,5.6,'hh',[3,4],(4,5))

# print(mytple)

######## Unpacking ############
# mytuple = (2,3,7,9)

# i,*j,t = mytuple
# print(i,j,t)

########## adding an element into tuple ######
# mytple2 = ('90',)
# print(mytple+mytple2)
# x = list(mytple)
# x.append(90)
# mytple = x
# print(mytple)


###### Type Conversion ###############

# int, float , str ,bool, list ,tuple, dict , set

# x = float('3')
# x = bool()
# x = str(3)
# print(x)

mytuple = [2,5.6,'hh',[3,4],(4,5)]

mylist3 = tuple(mytuple)
# mylist3.append(80)
# mytuple = tuple(mylist3)


# print(mylist3)

# mytuple = (3.4,2,  2, 3.4,3.4,   'tuple',  True ,  ('hi',6.7) )
# mylist =  [3.4,2,  2, 3.4,3.4,   'tuple',  True ,  ('hi',6.7) ]
# myset = set(mylist)
# mylist = tuple(myset)
# print(mylist)




########### Set ##################
''' 1. Set items are unchangeable(Immutable), and do not allow duplicate values and unordered.
    2. Sets are written with curly brackets.. '''


'''
Method	        Description
add()	    Adds an element to the set
clear()	    Removes all the elements from the set
copy()	    Returns a copy of the set
discard()	Remove the specified item
pop()	    Removes an element from the set
remove()	Removes the specified element
update()	Update the set with the union of this set and others
'''
myset = { 2, 2, 3.4,   'tuple',  True ,  ('hi',6.7)}
myset2  =  { 8,9}
# myset[2] = 4
# print(myset)


########### Add items to the set  ##########

# myset.add('newvalue')
# myset.update(myset2)
# print(myset)

###### Remove Item from the set ######

# myset.remove(8)
# myset.discard(8)
myset = { 2, 2, 3.4,   'tuple',  True ,  ('hi',6.7)}

# myset.pop(2)
# del myset[2]
# print(myset)

########### Dictonary ############
''' 1. Dictionaries are used to store data values in key:value pairs.
    2. A dictionary is a collection which is changeable(mutable) and does not allow duplicate Keys.
    3. Dictionaries are written with curly brackets, and have keys and values.
    4. For keys we can have only non-iterable data types
    5. For values we can have any data type. '''


'''
Method	            Description
clear()	        Removes all the elements from the dictionary
copy()	        Returns a copy of the dictionary
fromkeys()	    Returns a dictionary with the specified keys and value
get()	        Returns the value of the specified key
items()	        Returns a list containing a tuple for each key value pair
keys()	        Returns a list containing the dictionary's keys
pop()	        Removes the element with the specified key
popitem()	    Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	    Updates the dictionary with the specified key-value pairs
values()	    Returns a list of all the values in the dictionary
'''

# mylist[1] = [3,4]

# int , x= 6
# c = [3,4,5]

rollno = {
    1: 'ramesh',
    2 : 'sita'
}

# store = {
#     'soap' : 30,
#     'rice' : 50
# }

mydict = {
    1 : 'hello',
    'hello' : 4,
    3.4 : [2,3,[4,5],(2,3)],
    'key' : True,
    'key' : 4,
    True : {
        1 : 'word',
        2 : {
            3 : 'foo'
        }
    }
}
# print(mydict[True][2][3])

########## Accessing an element of dict ############
# print(mydict[True][2][3])
# print(mydict[3.4][3][0]) 

######## Updating valuess ##########
# mydict[3.4] = [3,4]
# mydict.update({'keyss':False})

###### Adding an item to dict #####

# mydict[7] = 85
# print(mydict)

############# Removing an item from dict #######

mydict = {
    1 : 'hello',
    'hello' : 4,
    3.4 : [2,3,[4,5],(2,3)],
    'key' : 4
}

# mydict.pop()
# mydict.popitem()
# del mydict
# mydict.clear()
# print(mydict)

######### Special Methods ########

print(type(mydict.keys()))
print(mydict.values())
print(mydict.items())




# for i in mydict.items():
#     m,n = i
#     print(m,n)
# x = ('key1','key2','key3')
# y = (0,0,0)
# mydict = dict.fromkeys(x,y)
# mylist = [2,3,4]
# for i in mylist:
#     print(mydict[i])
# print(mydict.get(2))

