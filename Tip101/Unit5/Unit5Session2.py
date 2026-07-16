'''
Problem 1: Battle Pokemon
Given the Pokemon class below, copy the code and add it to your IDE.

class Pokemon():
	def  __init__(self, name, hp, damage):
		self.name = name
		self.hp = hp # hit points
		self.damage = damage # The amount of damage this pokemon does to its opponent every attack
		
	def attack(self, opponent):
		pass
Then, write a method attack() that takes in a Pokemon object opponent and decreases opponent's hp by their self's damage amount.

If damaging the opponent leads to the opponent having an hp of 0 or less, the function should set the opponent's hp to 0 and print out "<Opponent name> fainted>.

Otherwise, the function should print out "<Pokemon name> dealt <damage> damage to <opponent name>".

Example Usage:

pikachu = Pokemon("Pikachu", 35, 20)
bulbasaur = Pokemon("Bulbasaur", 45, 30) 

opponent = bulbasaur
pikachu.attack(opponent)
Example Output: Pikachu dealt 20 damage to Bulbasaur
'''
class Pokemon():
	def  __init__(self, name, hp, damage):
		self.name = name
		self.hp = hp # hit points
		self.damage = damage # The amount of damage this pokemon does to its opponent every attack
		
	def attack(self, opponent):
		opponent.hp -= self.damage
		# print(self.name + " dealt " + str(self.damage) + " damage to " + opponent.name + ".") or alternatively
		print(f"{self.name} dealt {self.damage} damage to {opponent.name}.")
		if (opponent.hp < 0):
			opponent.hp = 0
			print(opponent.name + " fainted.")

# Example Usage:z
pikachu = Pokemon("Pikachu", 35, 20)
bulbasaur = Pokemon("Bulbasaur", 45, 30) 
opponent = bulbasaur
pikachu.attack(opponent)
pikachu.attack(opponent)
pikachu.attack(opponent)

# Example Output: Pikachu dealt 20 damage to Bulbasaur

'''
Problem 2: Convert to Linked List
A linked list is a new data type that, similar to a normal list or array, allows us to store pieces of data sequentially. The difference between a linked list and a normal list lies in how each element is stored in a computer’s memory.

In a normal list, individual elements of the list are stored in adjacent memory locations according to the order they appear in the list. If we know where the first element of the list is stored, it’s really easy to find any other element in the list.

In a linked list, the individual elements called nodes are not stored in sequential memory locations. Each node may be stored in an unrelated memory location. To connect nodes together into a sequential list, each node stores a reference or pointer to the next node in the list.

Using the provided Node class below, create the normal Python list ["Jigglypuff", "Wigglytuff"] as a linked list.

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
Example Usage (after completing the problem with variable names node_1 and node_2):

print(node_1.value, "->", node_1.next.value)
print(node_2.value, "->", node_2.next)
Example Output:

Jigglypuff -> Wigglytuff
Wigglytuff -> None
Result Linked list: Jigglypuff -> Wigglytuff

✨ AI Hint: Linked Lists
'''
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
		
node_2 = Node("Wigglytuff")
node_1 = Node("Jigglypuff", node_2)
# Example Usage (after completing the problem with variable names node_1 and node_2):
print(node_1.value, "->", node_1.next.value)
print(node_2.value, "->", node_2.next)

# Example Output:
# Jigglypuff -> Wigglytuff
# Wigglytuff -> None
# Result Linked list: Jigglypuff -> Wigglytuff

'''
Problem 3: Add First
Write a function add_first() that takes in a head of a linked list and a new_node from the Node class as parameters.

It should insert new_node as the new head of the linked_list. The function returns new_node.

Note: The "head" of a linked list is the first element in the linked list. Equivalent to lst[0] of a normal list.

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
		
		
def add_first(head, new_node):
	pass
Example Usage:

# Using the Linked List from Problem 2
print(node_1.value, "->", node_1.next.value)

new_node = Node("Ditto")
node_1 = add_first(node_1, new_node)

print(node_1.value, "->", node_1.next.value)
Example Output:

Jigglypuff -> Wigglytuff 
Ditto -> Jigglypuff
'''

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
		
		
def add_first(head, new_node):
	new_node.next = head
	return new_node

# Example Usage:
# Using the Linked List from Problem 2
print(node_1.value, "->", node_1.next.value)
new_node = Node("Ditto")
node_1 = add_first(node_1, new_node)
print(node_1.value, "->", node_1.next.value)

# Example Output:
# Jigglypuff -> Wigglytuff 
# Ditto -> Jigglypuff

'''
Problem 4: Get Tail
Write a function get_tail() that takes in the head of a linked list as a parameter.

Return the value of the tail. If the list is empty, return None.

Note: The "tail" of a list is the last element in the linked list. Equivalent to lst[-1] in a normal list.

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

def get_tail(head):
	pass
Example Usage:

# Build: num1 -> num2 -> num3
num1 = Node("num1")
num2 = Node("num2")
num3 = Node("num3")
num1.next = num2
num2.next = num3

head = num1
tail = get_tail(head)   # or get_tail(num1)
print(tail)             # expected: num3
Example Output: num3

💡 Hint: Linked List Traversal
'''
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

def get_tail(head):
	current = head
	if head is None:
		return None
	else:
		while current.next is not None:
			current = current.next
	return current, current.value

# Example Usage:
# Build: num1 -> num2 -> num3
num1 = Node("num1")
num2 = Node("num2")
num3 = Node("num3")
num1.next = num2
num2.next = num3
head = num1
tail = get_tail(head)   # or get_tail(num1)
print(tail)             # expected: num3
# Example Output: num3

'''
Problem 5: Replace Node
Using the Node class, write a function ll_replace() that updates in place every node whose value == original to have value = replacement. The function returns None.

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
		
def ll_replace(head, original, replacement):
	pass

 
def to_string(head): # to test your list
    parts, cur = [], head
    while cur:
        parts.append(str(cur.value))
        cur = cur.next
    return " -> ".join(parts) if parts else "EMPTY"
Example Usage:

num3 = Node(5)
num2 = Node(6, num3)
num1 = Node(5, num2)
# initial linked list: 5 -> 6 -> 5

head = num1
ll_replace(head, 5, "banana")
updated linked list: "banana" -> 6 -> "banana"
'''
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
		
def ll_replace(head, original, replacement):
	current = head

	while(current is not None):
		if current.value == original:
			current.value = replacement
			
			# print (f"{current.value} ->")
		# else:
			# print (f"{current.value} ->")
		current = current.next
	# return head
 
def to_string(head): # to test your list
    parts, cur = [], head
    while cur:
        parts.append(str(cur.value))
        cur = cur.next
    return " -> ".join(parts) if parts else "EMPTY"
	
# Example Usage:
num3 = Node(5)
num2 = Node(6, num3)
num1 = Node(5, num2)
# initial linked list: 5 -> 6 -> 5
head = num1
ll_replace(head, 5, "banana")
print(to_string(head))
# print(head.value) # test

# updated linked list: "banana" -> 6 -> "banana"

'''
Problem 6: List Nodes
Write a function listify_first_n() that takes in a head of a linked list and a non-negative integer n as parameters.

The function returns a list of values of the first n nodes.

If n is greater than the length of the linked list, return a list of the values of all nodes in the linked list.
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

def listify_first_n(head, n):
	pass
Example Usage:

# linked list: a -> b -> c
head = a
lst = listify_first_n(head,2)
print(lst)

# linked list: j -> k -> l 
head2 = j
lst2 = listify_first_n(head2,5)
print(lst2)
Example Output:

['a', 'b']
['j', 'k', 'l']
'''

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

def listify_first_n(head, n):
	count = 0
	current = head
	lst = []

	while (current and count < n): # loop stops when either you reach the end (current == None) or you collected n elements (count == n)
		lst.append(current.value)
		current = current.next
		count += 1

	return lst

# Example Usage:
# linked list: a -> b -> c
c = Node("c")
b = Node("b", c)
a = Node("a", b)

head = a
# head = "a"
lst = listify_first_n(head,2)
print(lst)

# linked list: j -> k -> l 
l = Node("l")
k = Node("k", l)
j = Node("j", k)

head2 = j
lst2 = listify_first_n(head2,5)
print(lst2)

# Example Output:
# ['a', 'b']
# ['j', 'k', 'l']

'''
Problem 7: Insert Value
Write a function ll_insert() that takes in a head of a linked list, a value val, and an index i as parameters.

The function should insert a new Node with value val at index i of the linked list, then return the head of the linked list.

If i is greater than the length of the list, insert the new node at the end of the list.
Hint: Linked lists do not have built-in indices so you will need to track the indices yourself.

Write a helper function to help you print the new list!

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
		
def ll_insert(head, val, i):
	pass
Example Usage:

# linked list: 3 -> 8 -> 12 -> 9
ll_insert(head, 20, 2)

# result linked list: 3 -> 8 -> 20 -> 12 -> 9
'''
# important
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
		
def ll_insert(head, val, i):
    new_node = Node(val)

    # Case 1: Empty list OR insert at head
    if head is None or i == 0:
        new_node.next = head
        return new_node

    current = head
    count = 0

    # Traverse to position OR last node
    while current.next is not None and count < i - 1:
        current = current.next
        count += 1

    # Insert node
    new_node.next = current.next
    current.next = new_node

    return head

# '2nd' attempt
	new_node = Node(val)

	# # edge case
	# if head is None:
	# 	return new_node
	
	# # Case 1: insert at head
	# if i == 0:
	# 	new_node.next = head
	# 	return new_node
	
	# current = head
	# index = 0

    # # Move to node BEFORE index i
	# while current and index < i - 1:
	# 	current = current.next
	# 	index += 1

    # # Insert if possible
	# if current:
	# 	new_node.next = current.next
	# 	current.next = new_node
		
	# return head
# -------------------------------------------
# `1st` attempt
	# current = head
	# index = 0
	# # need to create a new node
	# new_node = Node(val)

	# if(not head): # if linked list is empty
	# 	head = new_node

	# # while(current and index < i): 
	# # 	if (index == i):
	# # 		temp = current.next
	# # 		# current.next = val
	# # 		current.next = new_node
	# # 		current.next.next = temp
	# # 		break

	# # not right code, correct test case by accident
	# while(current and index < i ):  # not right code, correct test case by accident
	# 	temp = current.next
	# 	current.next = new_node
	# 	current.next.next = temp

	# 	# new_node.next = current.next
	# 	# current.next = new_node

	# 	current = current.next
	# 	index += 1
	# 	# 3 -> 8 -> 12 -> 9
	# 	# 3 -> 20 -> 8 -> 12 -> 9
	# 	# 3 -> 20 -> 8 -> 12 -> 9
	# 	# 3 -> 77 -> 20 -> 8 -> 12 -> 9
	# 	# 3 -> 25 -> 77 -> 20 -> 8 -> 12 -> 9
	# 	# 3 -> 55 -> 8 -> 12 -> 9
	
	# while current and index < i - 1: # need to stop before index i, not index < i, should be index < i - 1
	# 	current = current.next
	# 	index += 1

	# new_node.next = current.next
	# current.next = new_node

	# # If i is greater than the length of the list, insert the new node at the end of the list.
	# if (index < i):
	# 	# current.next = val
	# 	current.next = new_node

	# return head
	

# def printLL(head):
# 	current = head
def to_string(head): # to test your list
    parts, cur = [], head
    while cur:
        parts.append(str(cur.value))
        cur = cur.next
    return " -> ".join(parts) if parts else "EMPTY"

def print_list(head):
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")

# Example Usage:
# linked list: 3 -> 8 -> 12 -> 9

d = Node("9")
c = Node("12", d)
b = Node("8", c)
a = Node("3", b)
head = a

# to_string(head)
# print(to_string(head))
print_list(head)
ll_insert(head, 20, 2)
# to_string(head)
# print(to_string(head))
print_list(head)

# result linked list: 3 -> 8 -> 20 -> 12 -> 9

ll_insert(head, 99, 0)
# print(to_string(head))
print_list(head)
# # result linked list: 99 -> 3 -> 8 -> 20 -> 12 -> 9

ll_insert(head, 77, 1)
# print(to_string(head))
print_list(head)
# # result linked list: 99 -> 77 -> 3 -> 8 -> 20 -> 12 -> 9

ll_insert(head, 25, 2)
# print(to_string(head))
print_list(head)
# # result linked list: 99 -> 77 -> 25 -> 3 -> 8 -> 20 -> 12 -> 9

ll_insert(head, 55, 8)
# print(to_string(head))
print_list(head)
# # result linked list: 99 -> 77 -> 20 -> 3 -> 8 -> 20 -> 12 -> 9 -> 55

'''
Problem 8: Linked Listify
Write a function list_to_linked_list() that takes in a list lst as a parameter and converts it to a linked list. The function should return the head of the linked list.

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def list_to_linked_list(lst):
    pass
Example Usage:

normal_list = ["Betty", "Veronica", "Archie", "Jughead"]
linked_list = list_to_linked_list(normal_list)


# This prints ONLY the head node's value:
print(linked_list.value)   # => "Betty"

# (Optional) Traverse to print the whole linked list:
current = linked_list
while current:
    end_arrow = " -> " if current.next else "\n"
    print(current.value, end=end_arrow)
    current = current.next


# Print the head node's VALUE:
print(linked_list.value)        # expected: Betty

Example Output:

Betty

Betty -> Veronica -> Archie -> Jughead
'''


#################################################################################################### 
'''
Problem Set Version 2
Problem 1: Poker Two-Pair Hand
In poker, players are given a hand of five cards. A player has a "two-pair" hand if they have two cards of the same rank and another two cards of another rank. The fifth card isn’t used here.

Given the Card class below, write a function is_two_pair() that takes in a list player_hand that contains 5 Card objects.

The function returns True if the player has a two pair hand and False otherwise.

Cards in the hand are guaranteed to be unique and are guaranteed to have on the following suits and ranks:

The suit is one of the following values: "Hearts", "Spades", "Clubs", "Diamonds"
The rank is one of the following values: '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace'
class Card():
	def  __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank

def is_two_pair(player_hand):
	pass
Example Usage:

card_one = Card("Hearts", "Ace")
card_two = Card("Hearts", "4")
card_three = Card("Diamonds", "Ace")
card_four = Card("Diamonds", "4")
card_five = Card("Diamonds", "6")
card_six = Card("Diamonds", "7")

player_one_hand = [card_one, card_two, card_three, card_four, card_five]
print(is_two_pair(player_one_hand))

player_two_hand = [card_two, card_three, card_four, card_five, card_six]
print(is_two_pair(player_two_hand))
Example Output:

True  # Two Aces + Two 4s (+ Unused 6)
False # Two 4s (+ Ace + 6 + 7)
✨ AI Hint: Writing Methods
'''
class Card():
	def  __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank

def is_two_pair(player_hand):
	card_occurence = {} # dictionary
	count = 0

	for card in player_hand:
		# if card_occurence[card.rank] in card_occurence:
		if card.rank in card_occurence:
			card_occurence[card.rank] += 1
		else:
			card_occurence[card.rank] = 1

	for card, rank in card_occurence.items():
		if (rank == 2):
			count += 1
	
	return count == 2

print("---------------------")
card_one = Card("Hearts", "Ace")
card_two = Card("Hearts", "4")
card_three = Card("Diamonds", "Ace")
card_four = Card("Diamonds", "4")
card_five = Card("Diamonds", "6")
card_six = Card("Diamonds", "7")

player_one_hand = [card_one, card_two, card_three, card_four, card_five]
print(is_two_pair(player_one_hand))

player_two_hand = [card_two, card_three, card_four, card_five, card_six]
print(is_two_pair(player_two_hand))
# True  # Two Aces + Two 4s (+ Unused 6)
# False # Two 4s (+ Ace + 6 + 7)