########## Problem 1 ###########

'''

Given an array of integers nums and an integer target, return indices of the two numbers such that they 
add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 
Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
'''

# 1000000Ms
lst = [2,11,7,15]
d = {2:0}
target = 9

# for index,val in enumerate(lst):
#     if target - val in d:
#         print(d[target - val],index)
#         break
#     d[val] = index


def sum(num,target):
    seen= {}
    for i, v in enumerate(num):
        remaining = target - v
        if remaining in seen:
            return [seen[remaining],i]
        seen[v] = i

    return[]
print(sum([2,7,11,15],9))
########### Problem #########

'''
Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''
# Approch
'''

indext    0    1    2    3   4   5   6   7
string    a    c    b    d   b   a   c   d
          ^                  ^
          |                  |
		left               right
		seen = {a : 0, c : 1, b : 2, d: 3} 
		# case 1: seen[b] = 2, current window  is s[0:4] , 
		#        b is inside current window, seen[b] = 2 > left = 0. Move left pointer to seen[b] + 1 = 3
		seen = {a : 0, c : 1, b : 4, d: 3} 


indext    0    1    2    3   4   5   6   7
string    a    c    b    d   b   a   c   d
						 ^   ^
					     |   |
				      left  right		
indext    0    1    2    3   4   5   6   7
string    a    c    b    d   b   a   c   d
					     ^       ^
					     |       |
				       left    right		
		# case 2: seen[a] = 0,which means a not in current window s[3:5] , since seen[a] = 0 < left = 3 
		# we can keep moving right pointer.

'''



'''.git/
indext    0    1    2    3   4   5   6   7
string    a    c    b    d   b   a   c   d

         l               r   
'''
t = 0
def lengthOfLongestSubstring(s):
    seen = {}
    l = 0
    output = 0
    for r in range(len(s)):
        if s[r] not in seen:  #If s[r] not in seen, we can keep increasing the window size by moving right pointer
            output = max(output,r-l+1)
        else:
            if seen[s[r]] < l:
                output = max(output,r-l+1)
            else:
                l = seen[s[r]] + 1
        seen[s[r]] = r
    return output

    """
    There are two cases if s[r] in seen:
    case1: s[r] is inside the current window, we need to change the window by moving left pointer to seen[s[r]] + 1.
    case2: s[r] is not inside the current window, we can keep increase the window
    """

# print(lengthOfLongestSubstring('pwwkew'))