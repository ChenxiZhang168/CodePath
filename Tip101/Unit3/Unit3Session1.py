'''
Problem 1: Calling Mississippi
Copy and paste the following function:

def count_mississippi(limit):
    for num in range(1, limit):
        print( f"{num} mississippi")
Call the function so that it prints out the following to the console (without calling the function more than once):

1 mississipi
2 mississipi
3 mississipi
4 mississipi
5 mississipi
✨ AI Hint: String Interpolation
'''
def count_mississippi(limit):
    for num in range(1, limit):
        print(f"{num} mississippi")

count_mississippi(6)

'''
Problem 2: Swap Ends
Write a function swap_ends() that accepts a string my_str as a parameter and returns a new string where the first and last characters from my_str are swapped.

def swap_ends(my_str):
    pass
Example Usage:

my_str = "boat"
swapped = swap_ends(my_str)
print(swapped)
Example Output: toab

✨ AI Hint: String Indexing
💡 What's the difference between strings and lists?
'''
def swap_ends(my_str):
    if len(my_str) < 2:
        return my_str
    else:
        return my_str[-1] + my_str[1:-1] + my_str[0]

# def swap_ends(my_str):
#     end = len(my_str)
#     stringList = []
#     for i in range(len(my_str)):
#         # stringList[i] = end
#         # stringList.append(my_str[end]) IndexError: string index out of range
#         stringList.append(my_str[end - 1])
#         end -= 1
#     joined = ''.join(stringList)
#     return joined
    
# Example Usage:
my_str = "boat"
swapped = swap_ends(my_str)
print(swapped)
# this print out boat => toab, but wanna toab!!!

# Example Output: toab

'''
Problem 3: Is Pangram
Write a function is_pangram() that takes in a string my_str as a parameter and returns True if the string is a pangram and False if not. A pangram is a sentence containing every letter in the English alphabet.

def is_pangram(my_str):
    pass
Example Usage:

my_str = "The quick brown fox jumps over the lazy dog"
print(is_pangram(my_str))

str2 = "The dog jumped"
print(is_pangram(str2))
Example Output:

True
False
💡 Hint: Capitalization
✨ AI Hint: String Looping
'''
def is_pangram(my_str):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    my_str = my_str.lower()
    for letter in alphabet:
        if letter not in my_str:
            return False
    return True

# Example Usage:
my_str = "The quick brown fox jumps over the lazy dog"
print(is_pangram(my_str))

str2 = "The dog jumped"
print(is_pangram(str2))
# Example Output:
# True
# False

'''
Problem 4: Reverse String
Write a function reverse_string() that takes a string my_str as a parameter and returns the string reversed.

def reverse_string(my_str):
    pass
Example Usage:

my_str = "live"
print(reverse_string(my_str))
Example Output: evil
'''
def reverse_string(my_str):
    return my_str[::-1] # sequence[start:stop:step] python slicing
    

# my work: too complicated, but works
# def swap_ends(my_str):
#     end = len(my_str)
#     stringList = []
#     for i in range(len(my_str)):
#         # stringList[i] = end
#         # stringList.append(my_str[end]) IndexError: string index out of range
#         stringList.append(my_str[end - 1])
#         end -= 1
#     joined = ''.join(stringList)
#     return joined

# Example Usage:
my_str = "live"
print(reverse_string(my_str))
# Example Output: evil

'''
Problem 5: First Unique
Write a function first_unique_char() that given a string my_str as a parameter, it finds the first non-repeating character in it and returns its index. If it does not exist, then return -1.

def first_unique_char(my_str):
    pass
Example Usage:

my_str = "leetcode"
print(first_unique_char(my_str))

str2 = "loveleetcode"
print(first_unique_char(str2))

str3 = "aabb"
print(first_unique_char(str3))
Example Output

0
2
-1
'''
def first_unique_char(my_str):
    char_count = {}
    for char in my_str:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    for index, char in enumerate(my_str):
        if char_count[char] == 1:
            return index
    return -1

# enumerate() function returns an enumerate object. It contains the index and value of all the items in the iterable as pairs. 
# enumerate() does not return a dictionary
# It returns an iterator of (index, value) pairs

# my work: not correct, unfinished
# def first_unique_char(my_str):
#     chars = {}
#     chars = enumerate(my_str)
#     for k, v in chars.items():
#         if v > 0:
#             return k
#         else:
#             return -1
    
# Example Usage:
my_str = "leetcode"
print(first_unique_char(my_str))

str2 = "loveleetcode"
print(first_unique_char(str2))

str3 = "aabb"
print(first_unique_char(str3))

# Example Output
# 0
# 2
# -1


'''
Problem 6: Minimum Distance
Write a function min_distance() that takes in a list of strings words and two strings word1 and word2' as parameters. The function should return the minimum distance between word1 and word2 in the list of words. The distance between one word and an adjacent word in the list is 1.

def min_distance(words, word1, word2):
    pass
Example Usage:

words = ["the", "quick", "brown", "fox", "jumped", "the"]
dist1 = min_distance(words, "quick", "jumped")
dist2 = min_distance(words, "the", "jumped")
print(dist1)
print(dist2)

words2 = ["code", "path", "code", "contribute",  "practice"]
dist3 = min_distance(words2, "code", "practice")
print(dist3)
Example Output:

3
1
2
'''
# def min_distance(words, word1, word2):
#     index1 = -1
#     index2 = -1
#     min_dist = float('inf')

#     for i, word in enumerate(words):
#         if word == word1:
#             index1 = i
#         elif word == word2:
#             index2 = i

#         if index1 != -1 and index2 != -1:
#             min_dist = min(min_dist, abs(index1 - index2))

#     return min_dist if min_dist != float('inf') else -1

def min_distance(words, word1, word2):
    minDis = 99999
    w1 = -1
    w2 = -1
    
    for i in range(len(words)):
        if words[i] == word1:
            w1 = i
        elif words[i] == word2:
            w2 = i
        if (w1 != -1 and w2 != -1 and abs(w2-w1) < minDis):
        # if abs(w2-w1) < minDis:
            minDis = abs(w2-w1)
        # if w1 != -1 and w2 != -1:
        #     minDis = min(minDis, abs(w1 - w2))
            
    return minDis if minDis != 99999 else -1
    
# Example Usage:
words = ["the", "quick", "brown", "fox", "jumped", "the"]
dist1 = min_distance(words, "quick", "jumped")
dist2 = min_distance(words, "the", "jumped")
print(dist1)
print(dist2)

words2 = ["code", "path", "code", "contribute",  "practice"]
dist3 = min_distance(words2, "code", "practice")
print(dist3)

# Example Output:
# 3
# 1
# 2
