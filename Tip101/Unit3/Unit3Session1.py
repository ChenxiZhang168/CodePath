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
# def swap_ends(my_str):
#     if len(my_str) < 2:
#         return my_str
#     else:
#         return my_str[-1] + my_str[1:-1] + my_str[0]

def swap_ends(my_str):
    end = len(my_str)
    stringList = []
    for i in range(len(my_str)):
        # stringList[i] = end
        # stringList.append(my_str[end]) IndexError: string index out of range
        stringList.append(my_str[end - 1])
        end -= 1
    joined = ''.join(stringList)
    return joined
    
# Example Usage:
my_str = "boat"
swapped = swap_ends(my_str)
print(swapped)
# this print out boat => toab, but wanna toab!!!

# Example Output: toab


