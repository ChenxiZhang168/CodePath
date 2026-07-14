'''
Problem 1: Prime Number
Write a function is_prime() that takes in a positive integer n and returns True if it is a prime number and False otherwise. A prime number is a number greater than 1 that has no positive divisors other than 1 and itself.

def is_prime(n):
    pass
Example Usage:

print(is_prime(5))
print(is_prime(12))
print(is_prime(9))
Example Output:

True
False
False
✨ AI Hint: While Loops
💡 Hint: While Loops (more detail)

Uderstanding:
    print true if the number is prime, false otherwise
Plan:
    use while loop to check if the number is divisible by any number from 2 to n-1, if it is divisible by any number in that range, return false, otherwise return true
Implementation:
    below
'''
def is_prime(n):
    num = 2
    while(num < n):
        if n % num == 0:
            return False
        num += 1
    return True
    
# Example Usage:
print(is_prime(5))
print(is_prime(12))
print(is_prime(9))

# Example Output:
# True
# False
# False

'''
Problem 2: Two-Pointer Reverse List
Write a function reverse_list() that takes in a list lst and returns elements of the list in reverse order. The list should be reversed in-place without using list slicing (e.g. lst[::-1]).

Instead, use the two-pointer approach, which is a common technique in which we initialize two variables (also called a pointer in this context) to track different indices or places in a list or string, then moves the pointers to point at new indices based on certain conditions. In the most common variation of the two-pointer approach, we initialize one variable to point at the beginning of a list and a second variable/pointer to point at the end of list. We then shift the pointers to move inwards through the list towards each other, until our problem is solved or the pointers reach the opposite ends of the list.

def reverse_list(lst):
    pass
Example Input: [1, 2, 3, 4, 5]
Example Output: [5, 4, 3, 2, 1]

💡 Hint: Two Pointer Technique

Understanding:
    reverse the list in place using two pointers, one at the start and one at the end, swapping elements until they meet in the middle.

Plan:
    initialize two pointers, one at the beginning (0) and one at the end (len(lst) - 1)
    swap the elements at these pointers
    move the pointers towards each other until they meet

Implementation:
    below
'''

def reverse_list(lst):
    start = 0
    end = len(lst) - 1
    while (start < end):
        temp = lst[start]
        lst[start] = lst[end]
        lst[end] = temp
        start += 1
        end -= 1
    return lst

print(reverse_list([1, 2, 3, 4, 5]))
# Example Input: [1, 2, 3, 4, 5]
# Example Output: [5, 4, 3, 2, 1]

'''
Problem 3: Evaluating Solutions
The reverse_list() problem can also be solved without using the two pointer technique (as you may have seen it in previous units)! Evaluate the time and space complexity of your two-pointer solution.

Then, evaluate the time and space of the following solution:

def reverse_list(lst):
    # Create a new reversed list
    reversed_lst = lst[::-1]
    # Copy the elements back into the original list
    for i in range(len(lst)):
        lst[i] = reversed_lst[i]
Which has better time complexity?
Which has better space complexity?

💡 Hint: Big O (Time & Space Complexity)
✨ AI Hint: Decoding Big O
'''

# - new solution: O(n) time complexity, O(n) space complexity (due to creating a new list)
#  - two-pointer solution: O(n/2) time complexity, O(1) space complexity (in-place reversal)

'''
Problem 4: Move Even Integers
Write a function sort_list_by_parity() that takes in an integer list nums as a parameter and moves all the even integers at the beginning of the list followed by all the odd integers. The function returns any list that satisfies this condition.

def sort_array_by_parity(nums):
    pass
Example Usage:

nums = [3,1,2,4]
nums2 = [0]
print(sort_array_by_parity(nums))
print(sort_array_by_parity(nums2))
Example Output:

[2,4,3,1]
# Additional acceptable outputs are [4,2,3,1], [2,4,1,3], and [4,2,1,3]
[0]
'''
def sort_array_by_parity(nums):
    even_nums = []
    odd_nums = []
    
    for num in nums:
        if num % 2 == 0:
            even_nums.append(num)
        else:
            odd_nums.append(num)
    
    return even_nums + odd_nums

# def sort_array_by_parity(nums):
#     front = 0
#     back = len(nums) - 1
    
#     while (front < back):
#         if (nums[front] % 2 != 0 and nums[back] % 2 == 0):
#             temp = nums[front]
#             nums[front] = nums[back]
#             nums[back] = temp
#         # elif ():

#         # elif ():
            
#         # else:
#         front += 1
#         back -= 1
    
#     return nums
            
# Example Usage:
nums = [3,1,2,4]
nums2 = [0]
print(sort_array_by_parity(nums))
print(sort_array_by_parity(nums2))

# Example Output:
# [2,4,3,1]
# # Additional acceptable outputs are [4,2,3,1], [2,4,1,3], and [4,2,1,3]
# [0]


'''
Problem 5: Palindrome
Write a function first_palindrome() that takes in a list of strings words as a parameter and returns the first palindromic string in the list. A string is palindromic if it reads the same forward and backward. If there is no such string, return an empty string ""

def first_palindrome(words):
    pass
Example Usage:

words = ["abc","car","ada","racecar","cool"]
palindrome1 = first_palindrome(words)
print(palindrome1)

words2 = ["abc","racecar","cool"]
palindrome2 = first_palindrome(words2)
print(palindrome2)

words3 = ["abc", "def", "ghi"]
palindrome3 = first_palindrome(words3)
print(palindrome3)
Example Output:

ada
racecar

💡 Hint: Helper Functions
'''

def first_palindrome(words):
    for word in words:
        if word == word[::-1]: # word[::-1] reverses the string.
            return word
    return ""
'''
This is a slice expression in Python. The general form is:

sequence[start : stop : step]

So in your case:

word[::-1]

means:

start → (empty) → start from the beginning
stop → (empty) → go until the end
step → -1 → move backwards
'''

# my solution is below, but I think the above solution is more efficient and cleaner.
# # helper function to check if a string is a palindrome
# def is_palindrome(start, end, word):
#     start = 0
#     end = len(word) - 1
    
#     while (start < end):
#         if (word[start] != word[end]):
#             return False
#         start += 1
#         end -= 1
#     return True
    
# def first_palindrome(words):    
#     for i in range(len(words)):
#         start = 0
#         end = len(words[i]) - 1
        
#         palindromeOrNot = is_palindrome(start, end, words[i])
        
#         if (palindromeOrNot):
#             return words[i]
        
#     return ""

# Example Usage:
words = ["abc","car","ada","racecar","cool"]
palindrome1 = first_palindrome(words)
print(palindrome1)

words2 = ["abc","racecar","cool"]
palindrome2 = first_palindrome(words2)
print(palindrome2)

words3 = ["abc", "def", "ghi"]
palindrome3 = first_palindrome(words3)
print(palindrome3)

# Example Output:
# ada
# racecar

'''
Problem 6: Remove Duplicates with O(1)
Write a function remove_duplicates() that takes in a sorted list of integers nums as a parameter and removes the duplicates in-place such that each element appears only once. Do not allocate extra space for another array; you must do this by modifying the input list with O(1) extra memory. The function returns the new length of the list.

def remove_duplicates(nums):
    pass
Example Usage:

nums = [1,1,2,3,4,4,4,5]
print(nums)
print(remove_duplicates(nums))
print(nums) # same list
Example Output:

[1,1,2,3,4,4,4,5]
5
[1,2,3,4,5]
'''

#  my solution below
def remove_duplicates(nums):
    first = 0
    second = 1
    duplicate_count = 0
    count = 0
    
    while(second < len(nums)):
        if (nums[first] == nums[second]):
            # nums[second] = nums[second + 1]
            duplicate_count += 1
            # nums.pop(second)
            nums.remove(nums[second])
            # nums[second] = None
            # count += 1

        else: # if (nums[first] != nums[second]):
            first += 1
            second +=1
            # count += 1
        # count += 1

    # return nums, len(nums)
    return len(nums)

# Example Usage:
nums = [1,1,2,3,4,4,4,5]
print(nums)
print(remove_duplicates(nums))
print(nums) # same list
print("--------------------")

def remove_duplicates2(nums):
    if not nums:
        return 0

    first = 0  # points to last unique element

    for second in range(1, len(nums)):
        if nums[second] != nums[first]:
            first += 1
            nums[first] = nums[second]

    return first + 1  # number of unique elements

nums2 = [1,1,2,3,4,4,4,5]
print(nums2)

k = remove_duplicates2(nums2)

print(k)
print(nums2[:k])  # only take the unique part
print(nums2)  # same list

'''
It uses list slicing syntax:

sequence[start : stop]

In your case:

nums2[:k]

means:

start → omitted → defaults to 0
stop → k (not included)

👉 So it reads as:

“Take elements from index 0 up to (but not including) index k”
'''
# Example Output:
# [1,1,2,3,4,4,4,5]
# 5
# [1,2,3,4,5]