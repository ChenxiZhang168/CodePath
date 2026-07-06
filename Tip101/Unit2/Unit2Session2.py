'''
Problem 1: Cast Vote
Write a function cast_vote() that records a vote for a candidate in an election. The function accepts a dictionary votes that maps candidates to their current number of votes and a string candidate that represents the candidate the user would like to vote for. If the candidate doesn't exist, add them to the dictionary. The function should return the updated dictionary.

def cast_vote(votes, candidate):
    pass
Example Usage:

votes = {"Alice": 5, "Bob": 3}
cast_vote(votes, "Alice")
print(votes)
cast_vote(votes, "Gina")
print(votes)
Example Output:

{'Alice': 6, 'Bob': 3}
{'Alice': 6, 'Bob': 3, 'Gina': 1}
✨ AI Hint: Accessing Values in a Dictionary
💡 Hint: Dictionary Access options
'''
def cast_vote(votes, candidate):
    if candidate in votes:
        votes[candidate] += 1
    else:
        votes[candidate] = 1
    return votes

# my work: too complicated...
# def cast_vote(votes, candidate):
#     names = list(votes.keys())
#     for i in range(len(votes)):
#         # if candidate == votes[i]:
#         # if candidate == list(votes.keys())[i]: ==> if candidate == names[i]:
#         if candidate == names[i]:
#             votes[names[i]] += 1
#         else:
#             votes[candidate] = 1

# Example Usage:
votes = {"Alice": 5, "Bob": 3}
cast_vote(votes, "Alice")
print(votes)
cast_vote(votes, "Gina")
print(votes)

# Example Output:
# {'Alice': 6, 'Bob': 3}
# {'Alice': 6, 'Bob': 3, 'Gina': 1}

'''
Problem 2: Keys in Common
Write a function that takes in two dictionaries, dict1 and dict2 and finds all keys common to both dictionaries. The function returns a list of common keys.

def common_keys(dict1, dict2):
	pass
Example Usage:

dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 4, "c": 5, "d": 6}
common_list = common_keys(dict1, dict2)
print(common_list)
Example Output:

['b', 'c']
💡 Hint: Accessing Keys, Values, and Key-Value Pairs
💡 Hint: Looping over Key-Value Pairs
'''
def common_keys(dict1, dict2):
    common = []
    for key in dict1:
        if key in dict2:
            common.append(key)
    return common

# my work: too complicated, but I was trying to use nested loops instead of the "in" operator.
# def common_keys(dict1, dict2):
#     commonKeys = []
#     for keys in dict1:
#         for k in dict2:
#             if keys == k:
#                 commonKeys.append(keys);
#     return commonKeys
        
# Example Usage:
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 4, "c": 5, "d": 6}
common_list = common_keys(dict1, dict2)
print(common_list)

# Example Output:
['b', 'c']

'''
Problem 3: Frequency Count
Write a function that takes in a list of integers nums and counts the number of occurrences of each integer. The function returns the result as a dictionary with integers as keys and their counts as values.

def count_occurrences(nums):
    pass
Example Input: nums = [1, 2, 2, 3, 3, 3, 4]
Example Output: {1: 1, 2: 2, 3: 3, 4: 1}

✨ AI Hint: Frequency Maps
'''
def count_occurrences(nums):
    counts = {}
    for num in nums:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    return counts

# my work: too complicated, but I was trying to use position as the key instead of the number itself.
# def count_occurrences(nums):
#     numsDict = {}
#     # position = 0
#     position = 1
#     for i in range(len(nums)):
#         if nums[i] not in numsDict:
#             numsDict[position] = 1
#             position += 1
#             print(numsDict)
#         elif nums[i] in numsDict:
#             number = nums[i]
#             numsDict[number] += 1
#             print(numsDict)
#     return numsDict

# # Example Input: 
# nums = [1, 2, 2, 3, 3, 3, 4]
# print(count_occurrences(nums))
# # Example Output: {1: 1, 2: 2, 3: 3, 4: 1}

'''
Problem 4: Highest Priority Task
Given a dictionary tasks where keys are task names and values are priorities (1-10, where 10 is the highest priority), write a function get_highest_priority_task() that removes the task with the highest priority from the dictionary and returns its name.
If two tasks have the same priority, return the task that comes first in the alphabet.

def get_highest_priority_task(tasks):
	pass
Example Usage:

tasks = {"task1": 8, "task2": 10, "task3": 9, "task4": 10, "task5": 7}
perform_task = (get_highest_priority_task(tasks))
print(perform_task)

perform_task = (get_highest_priority_task(tasks))
print(perform_task)

perform_task = (get_highest_priority_task(tasks))
print(perform_task)

print(tasks)
Example Output:

task2
task4
task3
{'task1': 8,'task5': 7}
💡 Hint: Removing Key-Value Pairs from a Dict
'''
# def get_highest_priority_task(tasks):
#     highest_priority = -1
#     highest_task = None
#     for task, priority in tasks.items():
#         if priority > highest_priority or (priority == highest_priority and task < highest_task):
#             highest_priority = priority
#             highest_task = task
#     if highest_task is not None:
#         del tasks[highest_task]
#     return highest_task

# my work:
def get_highest_priority_task(tasks):
    highest = 0
    position = 0
    for i in range(len(tasks)):
        # if (task.values())[i] > highest:
        if list(tasks.values())[i] > highest:
            position = i
    tasks.pop(list(tasks.keys())[position], "ERROR: invalid syntax")
            
# Example Usage:
tasks = {"task1": 8, "task2": 10, "task3": 9, "task4": 10, "task5": 7}
perform_task = (get_highest_priority_task(tasks))
print(perform_task)

perform_task = (get_highest_priority_task(tasks))
print(perform_task)

perform_task = (get_highest_priority_task(tasks))
print(perform_task)

print(tasks)

# Example Output:
# task2
# task4
# task3
# {'task1': 8,'task5': 7}

# thoughts: pop, or max, or remove method