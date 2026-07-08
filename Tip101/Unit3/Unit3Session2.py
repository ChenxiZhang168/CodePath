'''
Problem 1: Sum of Strings
Write a function sum_of_number_strings() that takes in a list of strings nums. Each string is a representations of integers. The function should return the sum of these strings as an integer.

def sum_of_number_strings(nums):
    pass
Example Usage:

nums = ["10", "20", "30"]
sum = sum_of_number_strings(nums)
print(sum)
Example Output: 60
-----------------------------------------------------
Problem 1: Sum of Strings
U: 
    - function takes a string of numbers 
    - returns the sum of strings as an integer 
P: 
    1. create a sum var
    2. convert all the strings to number using casting
    3. add them up to sum var and then return "sum"

I: 
    
'''

def sum_of_number_strings(nums):
    string_sum = 0 
    for n in nums:
        string_sum = string_sum + int(n)
    return string_sum
    
nums = ["10", "20", "30"]
sum = sum_of_number_strings(nums)
print(sum)


'''
Problem 2: Remove Duplicates
Write a function remove_duplicates() that takes in a sorted list of integers nums as a parameter and removes all duplicates in the list. The function returns the modified list.

def remove_duplicates(nums):
    pass
Example Input: nums = [1,1,1,2,3,4,4,5,6,6]
Example Output: no_dups = [1,2,3,4,5,6]

✨ AI Hint: While Loops
💡 Hint: While Loops (more detail)
------------------------------------------------
Problem 2: Remove Duplicates
U:  - func accepts a list of numbers 
    - func removes all duplicates 
    - returns the same list as modified 

P: 
    1. create a dictionary to store the key(alphabet) and value(frequency) as a pair
    2. run thru entire list if the frequency is greater than 1, use the pop method to remove the duplicate alphabet
    3. return the modify list

'''

def remove_duplicates(nums):
    dic = {}
    for n in nums:
        if n not in dic:
            dic[n] = 1
        else:
            # dic[n] = dic[n] + 1
            print(dic[n])
            # print('here2: ', nums)
        
        if(dic[n] > 1):
            nums.remove(n)
            
    print('here: ', nums)
    # return nums


nums = [1,1,1,2,3,4,4,5,6,6]
# print(remove_duplicates(nums))
# [1,2,3,4,5,6]

'''
Problem 2: Remove Duplicates
U:  - func accepts a list of numbers 
    - func removes all duplicates 
    - returns the same list as modified 

P: 
    1. create a dictionary to stoe the key(alphabet) and value(frequency) as a pair
    2. run thru entire list if the frequency is greater than 1, use the pop method to remove the duplicate alphabet
    3. return the modify list

'''


# def remove_duplicates(nums):
#     dic = {}
#     for n in nums:
#         if n not in dic:
#             dic[n] = 1
#         else:
#             dic[n] = dic[n] + 1
#         nums.remove(n)
#     return nums


# nums = [1,1,1,2,3,4,4,5,6,6]
# print(remove_duplicates(nums))

'''
Problem 3: Reverse Letters

U: 
    - take in a string, and reverse the letters within the
      string and keeps Non-letter characters as it is

p: 
    - Loop through the string 
        1. if current character is not a letter, do nothing. For example, i == '-': do nothing 
        2. using a ASCII Chart, https://www.ascii-code.com/
         - 65 for uppercase A to 90 for uppercase Z
         - 97 for lowercase a to to 122 for lower case z 

'''
# def reverse_only_letters(s):
#     newString
#     for items in s:
#         if (int(s.lower()) >= 97 and int(s.lower()) <= 122):
#             newString = newString + items
#         else:
#             newString = newString + items
#     return newString


# # Example Usage:
# s = "a-bC-dEf-ghIj"
# # Example Output: j-Ih-gfE-dCba
# reversed_s = reverse_only_letters(s)
# print(reversed_s)