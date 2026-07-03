'''
Problem 1: Print List
Write a function print_list() that takes in a list lst as a parameter and prints out each item in the list.

def print_list(lst):
    pass
Example Input: lst = ["squirtle", "gengar", "charizard", "pikachu"]
Example Output:

squirtle
gengar
charizard
pikachu
'''
def print_list(lst):
    for item in lst:
        print(item)
# test case
lst = ["squirtle", "gengar", "charizard", "pikachu"]
print_list(lst)

'''
Problem 2: Print Doubled List Items
Write a function doubled() that takes in a list of integers lst as a parameter and prints each item in the list multiplied by two.

def doubled(lst):
    pass
Example Input: lst = [1,2,3]
Example Output:

2
4
6
'''
def doubled(lst):
    for item in lst:
        print(item * 2)
# test case 
lst = [1, 2, 3]
doubled(lst)

'''
Problem 3: Return Doubled List
Modify the function doubled() so that instead of printing the items, it returns a new list of the doubled numbers.

Example Usage:

lst = [1,2,3]
new_lst = doubled(lst)
print(new_lst)
Example Output:

[2, 4, 6]
'''
def doubled(lst):
	newLst=[]
	for item in lst:
		newLst.append(item * 2)
	return newLst
lst = [1,2,3]
new_lst = doubled(lst)
print(new_lst)
		
'''
Problem 4: Flip Signs
Write a function flip_sign() that takes in a list of integers lst as a parameter and returns a new list where each number in the original list has been multiplied by -1.

def flip_sign(lst):
    pass
Example Usage:

lst = [1,-2,-3,4]
flipped_lst = flip_sign(lst)
print(flipped_lst)
Example Output:

[-1, 2, 3, -4]
'''
def flip_sign(lst):
	flipped=[]
	for item in lst:
		flipped.append(item*-1)
	return flipped
lst = [1,-2,-3,4]

flipped_lst = flip_sign(lst)
print(flipped_lst)

'''
Problem 5: Max Difference
Write a function max_difference() that takes in a list of integers lst and returns the difference between the smallest and largest value in the list.

def max_difference(lst):
    pass
Example Usage:

lst = [5,22,8,10,2]
max_diff = max_difference(lst)
print(max_diff)
Example Output: 20
'''
def max_difference(lst):
	max = -99999999
	min = 99999999
	for item in lst:
		if item > max:
			max = item
		if item < min:
			min = item
	return max - min

lst = [5,22,8,10,2]
max_diff = max_difference(lst)
print(max_diff)

'''
Problem 6: Below Threshold
Write a function count_less_than() that takes in a list of integers numbers and an integer threshold as parameters and returns the number of items in numbers that are less than threshold.

def count_less_than(numbers, threshold):
    pass
Example Usage:

numbers = [12,8,2,4,4,10]
counter = count_less_than(numbers,5)
print(counter)
Example Output: 3
'''
def count_less_than(numbers, threshold):
	count = 0
	for item in numbers:
		if item < threshold:
			count += 1
	return count

numbers = [12,8,2,4,4,10]
counter = count_less_than(numbers,5)
print(counter)

'''
Problem 7: Evens List
Write a function get_evens() that takes in a list of integers lst as a parameter and returns a list of all even numbers in the list.

def get_evens(lst):
    pass
Example Usage:

lst = [1,2,3,4]
evens_lst = get_evens(lst)
print(evens_lst)
Example Output:

[2, 4]
💡 Remainders with Modulus Division
'''
def get_evens(lst):
	even = []
	for item in lst:
		if item % 2 == 0:
			even.append(item)
	return even

lst = [1,2,3,4]
evens_lst = get_evens(lst)
print(evens_lst)

'''
Problem 8: Multiples of Five
Write a function multiples_of_five() that prints out multiples of 5 between 1 and 100 (inclusive).

def multiples_of_five():
    pass
Example Output:

5
10
15
20
25
....
90
95
100
'''
def multiples_of_five():
    for i in range(5, 101, 5):
        # if i % 5 == 0:
        print(i)

multiples_of_five()

'''
Problem 9: Divisors
Write a function find_divisors() that takes in an integer n as a parameter that returns a list of all divisors of n.

def find_divisors(n):
    pass
Example Usage:

lst = find_divisors(6)
print(lst)
Example Output:

[1, 2, 3, 6]
'''
def find_divisors(n):
	divisor = []
	for i in range (1, n+1):
		if n % i == 0:
			divisor.append(i)
	return divisor

lst = find_divisors(6)
print(lst)

'''
Problem 10: FizzBuzz
Write a function fizzbuzz() that takes in an integer n as a parameter and prints the numbers from 1 to n.
For multiples of 3, print "Fizz" instead of the number.
For multiples of 5, print "Buzz" instead of the number.

def fizzbuzz(n):
    pass
Example Usage: fizzbuzz(13)

Example Output:

1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
'''
def fizzbuzz(n):
	for i in range(1, n+1):
		if i % 3 == 0:
			print("Fizz")
		elif i % 5 == 0:
			print("Buzz")
		else:
			print(i)
fizzbuzz(13)

'''
Problem 11: Print the Index
Write a function print_indices() that takes in an integer list lst as a parameter and prints out the index of each item in the given list.
Use the function range() to loop through the list indices.

def print_indices(lst):
    pass
Example Usage:

lst = [5,1,3,8,2]
print_indices(lst)
Example Output:

0
1
2
3
4
'''
def print_indices(lst):
	for i in range(len(lst)):
		print(i)

lst = [5,1,3,8,2]
print_indices(lst)

'''
Problem 12: Linear Search
Write a function linear_search() that takes in a list lst and value target as parameters. The function returns the index of target in lst if found. If target is not found in lst, return -1.

def linear_search(lst, target):
    pass
Example Usage:

lst = [1,4,5,2,8]
position = linear_search(lst,5)
print(position)
Example Output: 2


Example Usage:

lst = [1,4,5,2,8]
position = linear_search(lst,10)
print(position)
Example Output: -1
'''
def linear_search(lst, target):
	for item in lst:
		if (item == target):
			return lst.index(item)
	else:
		return -1
		
# def linear_search(lst, target):
# 	for i in range(len(lst)):
# 	    if (lst[i] == target):
# 		    return i
# 	else:
# 		return -1
		
lst = [1,4,5,2,8]
position = linear_search(lst,5)
print(position)