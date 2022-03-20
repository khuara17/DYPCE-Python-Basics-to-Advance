######### Prob 1 ########

'''# Write a function TO DO MULTIPLICATION WITOUT USING THE * OPERATOR.
'''
# 4 * 2 = 2 + 2 + 2 + 2 == 4 + 4 = 8

def MULTIPLICATION(a:int,b:int) -> int:
	sum = 0
	for i in range(b):
		sum += a
	return sum

# print(MULTIPLICATION(10,20))

######### Prob 2 ############

'''
Create a function that takes three arguments a, b, c and 
returns the sum of the numbers that are evenly divided by c from the range a, b inclusive.

Examples
evenly_divisible(1, 10, 20) ➞ 0
# No number between 1 and 10 can be evenly divided by 20.

evenly_divisible(1, 10, 2) ➞ 30
# 2 + 4 + 6 + 8 + 10 = 30

evenly_divisible(1, 10, 3) ➞ 18
# 3 + 6 + 9 = 18
'''

# def problem2(a:int,b:int,c:int) -> int:
# 	sum = 0
# 	a += c- a%c
# 	print(a)
# 	for i in range(a,b+1,c):
# 		sum += i
# 	return sum

# print("problem2 : ", problem2(1,10,3))

# def problem2(a:int,b:int,c:int) -> int:
# 	sum = 0
# 	for i in range(a,b+1):
# 		if i%c == 0:
# 			sum += i
# 	return sum

# print(problem2(1,10,2))





############## Problem 3 ###############3333

'''
Create a function that returns True if a given inequality expression is correct and False otherwise.

Examples
correct_signs("3 < 7 < 11") ➞ True

correct_signs("13 > 44 > 33 > 1") ➞ False

correct_signs("1 < 2 < 6 < 9 > 3") ➞ True
'''

def correct_signs(mylst):
    print(eval(mylst))

# correct_signs("1 < 2 < 6 < 9 > 3")

############## Problem 4 ###############
'''
Write a function that moves all elements of one type to the end of the list.

Examples
move_to_end([1, 3, 2, 4, 4, 1], 1) ➞ [3, 2, 4, 4, 1, 1]
# Move all the 1s to the end of the array.

move_to_end([7, 8, 9, 1, 2, 3, 4], 9) ➞ [7, 8, 1, 2, 3, 4, 9]

move_to_end(["a", "a", "a", "b"], "a") ➞ ["b", "a", "a", "a"]
'''

def move_to_end(a,b):
	d = 0
	c = []
	for i in a:
		if i != b:
			c.append(i)
		else:
			d = d + 1
	for i in range(d):
		c.append(b)
	print(c)

# move_to_end([7, 8, 9, 1, 2, 3, 4], 9)
# move_to_end(["a", "a", "a", "b"], "a")

########## Take list a input from user ####
# n = int (input("Entter the no of elements"))
# ip = []
# for i in range(n):
# 	x = int(input("Ener a no:-"))
# 	ip.append(x)
# print(ip)

############## Problem 5 #############

'''
Create a function that takes a string (will be a person's first and last name) and 
returns a string with the first and last name swapped.

Examples
name_shuffle("Donald Trump") ➞ "Trump Donald"

name_shuffle("Rosie O'Donnell") ➞ "O'Donnell Rosie"

name_shuffle("Seymour Butts") ➞ "Butts Seymour"

Notes
There will be exactly one space between the first and last name.
'''


s = "Donald Trump"
def rev(s):
	lst = s.split(' ')
	return ' '.join(lst[::-1])

# print(rev(s))





################ Problem 6 ################ 
'''
Create a function that takes a list of numbers between 1 and 10 (excluding one number) 
and returns the missing number.

Examples
missing_num([1, 2, 3, 4, 6, 7, 8, 9, 10]) ➞ 5

missing_num([7, 2, 3, 6, 5, 9, 1, 4, 8]) ➞ 10

missing_num([10, 5, 1, 2, 4, 6, 8, 3, 9]) ➞ 7

Notes
The list of numbers will be unsorted (not in order).
Only one number will be missing.
'''

# 55 - x = 50
# x = 55 -50
# def missing (l:list)->int:
# 	for i in range(1,11):
# 		if i  not in(l):
# 			print(i)


def missing_num(l):
	return 55 - sum(l)
	
print("missing elenmets",missing_num([10, 5, 1, 2, 4, 6, 8, 7, 9]))


############ Prob 7 ##########

'''
Write a function that takes a string, breaks it up and returns it with vowels first, consonants second.
For any character that's not a vowel (like special characters or spaces), treat them like consonants.

Examples
split("abcde") ➞ "aebcd"

split("Hello!") ➞ "eoHll!"

split("What's the time?") ➞ "aeieWht's th tm?"

Notes
Vowels are a, e, i, o, u.
'''