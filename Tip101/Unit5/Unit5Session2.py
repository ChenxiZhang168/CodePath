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