'''
Problem 1: Pokemon Class
Step 1: Copy the following code into your IDE.

Step 2: Add a line of code (outside of the class) to instantiate an instance of the class Pokemon and store it in a variable named my_pokemon. The Pokemon instance created should have name "Pikachu" and its types should be ["Electric"].

class Pokemon:
    def __init__(self, name, types):
        self.name = name
        self.types = types
        self.is_caught = False
✨ AI Hint: Intro to Object Oriented Programming
'''
class Pokemon:
    def __init__(self, name, types):
        self.name = name
        self.types = types
        self.is_caught = False

my_pokemon = Pokemon("Pikachu", "Electric")
print(my_pokemon.name)
print(my_pokemon.types)
print(my_pokemon.is_caught)

'''
Problem 2: Create Squirtle
Step 1: Add the print_pokemon definition below to your code on your IDE.

Step 2: Instantiate an instance of the class Pokemon and store it in a variable named squirtle. The Pokemon instance created should have name "Squirtle" and its types should be ["Water"].

Step 3: Call the method print_pokemon() on your new Pokemon instance squirtle.

class Pokemon:
    def __init__(self, name, types):
        self.name = name
        self.types = types
        self.is_caught = False

    def print_pokemon(self):
        print({
            "name": self.name,   
            "types": self.types, 
            "is_caught": self.is_caught 
        })
Example Usage:

squirtle = Pokemon("Squirtle", ["water"])
squirtle.print_pokemon()
Example Output
{'name': 'Squirtle', 'types': ['water'], 'is_caught': False}
✨ AI Hint: Class Methods
'''
class Pokemon:
    def __init__(self, name, types):
        self.name = name
        self.types = types
        self.is_caught = False

    def print_pokemon(self):
        print({
            "name": self.name,   
            "types": self.types, 
            "is_caught": self.is_caught 
        })
# Example Usage:
print("-------------------")
squirtle = Pokemon("Squirtle", ["water"])
squirtle.print_pokemon()

# Example Output
# {'name': 'Squirtle', 'types': ['water'], 'is_caught': False}

'''
Problem 3: Is Caught
Using your code from Problem 2, update your squirtle Pokemon so that is_caught is updated to True. Use the print_pokemon() function to verify that squirtle's is_caught property was updated.

Expected Output:

{
    "name": "Squirtle",
    "types": ["Water"],
    "is_caught": True
}
Example Output

{'name': 'Squirtle', 'types': ['water'], 'is_caught': True}
✨ AI Hint: Class Attributes
'''
print("-------------------")
squirtle.is_caught = True
squirtle.print_pokemon()

'''
Problem 4: Catch Pokemon
Update the Pokemon class with a new method catch() that takes in no parameters except self.

The method should update the Pokemon's is_caught attribute to True and not return any value.

class Pokemon():
	...
	
	def catch(self):
		pass
Example Usage:

my_pokemon = Pokemon("rattata", ["Normal"])
my_pokemon.print_pokemon()

my_pokemon.catch()
my_pokemon.print_pokemon()
Example Output:

{'name': 'rattata', 'types': ['Normal'], 'is_caught': False} # First print statement
{'name': 'rattata', 'types': ['Normal'], 'is_caught': True}  # Second print statement
✨ AI Hint: Writing Methods
'''
class Pokemon:
    def __init__(self, name, types):
        self.name = name
        self.types = types
        self.is_caught = False

    def print_pokemon(self):
        print({
            "name": self.name,   
            "types": self.types, 
            "is_caught": self.is_caught 
        })
    
    def catch(self):
        self.is_caught = True

# Example Usage:
print("-------------------")
my_pokemon = Pokemon("rattata", ["Normal"])
my_pokemon.print_pokemon()
my_pokemon.catch()
my_pokemon.print_pokemon()

# Example Output:
# {'name': 'rattata', 'types': ['Normal'], 'is_caught': False} # First print statement
# {'name': 'rattata', 'types': ['Normal'], 'is_caught': True}  # Second print statement

'''
Problem 5: Choose Pokemon
Update the Pokemon class with a new method choose() that takes in no parameters except self.

If the Pokemon is caught, the method should print the string "<Pokemon name> I choose you!".

Otherwise, it should print "<Pokemon name> is wild! Catch them if you can!".

class Pokemon():
	...
	
	def choose(self):
		pass
Example Usage:

my_pokemon = Pokemon("rattata", ["Normal"])
my_pokemon.print_pokemon()

my_pokemon.choose()
my_pokemon.catch()
my_pokemon.choose()
Example Output:

{'name': 'rattata', 'types': ['Normal'], 'is_caught': False}
rattata is wild! Catch them if you can!
rattata I choose you!
'''

class Pokemon():
    def __init__(self, name, types):
        self.name = name
        self.types = types
        self.is_caught = False

    def print_pokemon(self):
        print({
            "name": self.name,   
            "types": self.types, 
            "is_caught": self.is_caught 
        })
    
    def catch(self):
        self.is_caught = True

    def choose(self):
        if (self.is_caught):
            print(self.name + " I choose you!")
        else:
            print(self.name + " is wild! Catch them if you can!")

print("-------------------")
# Example Usage:
my_pokemon = Pokemon("rattata", ["Normal"])
my_pokemon.print_pokemon()
my_pokemon.choose()
my_pokemon.catch()
my_pokemon.choose()

# Example Output:
# {'name': 'rattata', 'types': ['Normal'], 'is_caught': False}
# rattata is wild! Catch them if you can!
# rattata I choose you!

'''
Problem 6: Add Pokemon Type
Update the Pokemon class with a new method add_type() that takes in a string new_type as a parameter.

It should add new_type to the Pokemon's list of types.

class Pokemon():
	...
	
	def add_type(self, new_type):
		pass
Example Usage:

jigglypuff = Pokemon("Jigglypuff", ["Normal"])
jigglypuff.print_pokemon()

jigglypuff.add_type("Fairy")
jigglypuff.print_pokemon()
Example Output:

{'name': 'Jigglypuff', 'types': ['Normal'], 'is_caught': False}
{'name': 'Jigglypuff', 'types': ['Normal', 'Fairy'], 'is_caught': False}
'''
class Pokemon():
    def __init__(self, name, types):
        self.name = name
        self.types = types
        self.is_caught = False

    def print_pokemon(self):
        print({
            "name": self.name,   
            "types": self.types, 
            "is_caught": self.is_caught 
        })
    
    def catch(self):
        self.is_caught = True

    def choose(self):
        if (self.is_caught):
            print(self.name + " I choose you!")
        else:
            print(self.name + " is wild! Catch them if you can!")

    def add_type(self, new_type):
        self.types.append(new_type)

# Example Usage:
print("-------------------")
jigglypuff = Pokemon("Jigglypuff", ["Normal"])
jigglypuff.print_pokemon()
jigglypuff.add_type("Fairy")
jigglypuff.print_pokemon()

# Example Output:
# {'name': 'Jigglypuff', 'types': ['Normal'], 'is_caught': False}
# {'name': 'Jigglypuff', 'types': ['Normal', 'Fairy'], 'is_caught': False}

'''
Problem 7: Get Pokemon
Outside the Pokemon class, write a new function get_by_type() that takes in a list of Pokemon instances my_pokemon and a string pokemon_type as parameters.

The function should return a list of all Pokemon instances from my_pokemon that have the type pokemon_type.

Hint: To test, loop over Pokemon in return list and print the Pokemon's name

class Pokemon():
	...
	
def get_by_type(my_pokemon, pokemon_type):
	pass
Example Usage:

# initializing pokemons
jigglypuff = Pokemon("Jigglypuff", ["Normal", "Fairy"])
diglett = Pokemon("Diglett", ["Ground"])
meowth = Pokemon("Meowth", ["Normal"])
pidgeot = Pokemon("Pidgeot", ["Normal", "Flying"])
blastoise = Pokemon("Blastoise", ["Water"])

my_pokemon = [jigglypuff, diglett, meowth, pidgeot, blastoise]
normal_pokemon = get_by_type(my_pokemon, "Normal")
print(normal_pokemon)
Example Output: [Jigglypuff, Meowth, Pidgeot]
'''
class Pokemon():
    def __init__(self, name, types):
        self.name = name
        self.types = types
        self.is_caught = False

    def print_pokemon(self):
        print({
            "name": self.name,   
            "types": self.types, 
            "is_caught": self.is_caught 
        })
    
    def catch(self):
        self.is_caught = True

    def choose(self):
        if (self.is_caught):
            print(self.name + " I choose you!")
        else:
            print(self.name + " is wild! Catch them if you can!")

    def add_type(self, new_type):
        self.types.append(new_type)

def get_by_type(my_pokemon, pokemon_type):
    toReturn = []
    for items in my_pokemon:
        # if (items.types == pokemon_type):
        if pokemon_type in items.types:
            # toReturn.append(items)
            toReturn.append(items.name)
    return toReturn

# Example Usage:
print("-------------------")
# initializing pokemons
jigglypuff = Pokemon("Jigglypuff", ["Normal", "Fairy"])
diglett = Pokemon("Diglett", ["Ground"])
meowth = Pokemon("Meowth", ["Normal"])
pidgeot = Pokemon("Pidgeot", ["Normal", "Flying"])
blastoise = Pokemon("Blastoise", ["Water"])

my_pokemon = [jigglypuff, diglett, meowth, pidgeot, blastoise]
normal_pokemon = get_by_type(my_pokemon, "Normal")
print(normal_pokemon)

# Example Output: [Jigglypuff, Meowth, Pidgeot]

'''
Problem 8: Pokemon Evolution
Some Pokemon can evolve into other species of Pokemon. In the updated Pokemon class below, each instance of Pokemon has an attribute evolution. The attribute will either be the default value of None or another Pokemon instance.

Write a function get_evolutionary_line() that takes in a Pokemon object starter_pokemon as a parameter.

The function should return a list of itself and the Pokemon that the starter_pokemon can evolve into.

class Pokemon():
	def  __init__(self, name, types, evolution = None):
		self.name = name
		self.types = types
		self.is_caught = False
		self.evolution = evolution
 
def get_evolutionary_line(starter_pokemon):
	pass
Example Usage:

charizard = Pokemon("Charizard", ["fire", "flying"])
charmeleon = Pokemon("Charmeleon", ["fire"], charizard)
charmander = Pokemon("Charmander", ["fire"], charmeleon)

charmander_list = get_evolutionary_line(charmander)
print(charmander_list)

charmeleon_list = get_evolutionary_line(charmeleon)
print(charmeleon_list)

charizard_list = get_evolutionary_line(charizard)
print(charizard_list)
Example Output:

[`Charmander`, `Charmeleon`, `Charizard`]
[`Charmeleon`, `Charizard`]
['Charizard']
'''

class Pokemon():
    #  def __init__(self, name, types):
    #     self.name = name
    #     self.types = types
    #     self.is_caught = False
	def  __init__(self, name, types, evolution = None):
		self.name = name
		self.types = types
		self.is_caught = False
		self.evolution = evolution
        
    # def print_pokemon(self):
    #     print({
    #         "name": self.name,   
    #         "types": self.types, 
    #         "is_caught": self.is_caught 
    #     })
    
    # def catch(self):
    #     self.is_caught = True

    # def choose(self):
    #     if (self.is_caught):
    #         print(self.name + " I choose you!")
    #     else:
    #         print(self.name + " is wild! Catch them if you can!")

    # def add_type(self, new_type):
    #     self.types.append(new_type)
        
def get_by_type(my_pokemon, pokemon_type):
    toReturn = []
    for items in my_pokemon:
        # if (items.types == pokemon_type):
        if pokemon_type in items.types:
            # toReturn.append(items)
            toReturn.append(items.name)
    return toReturn

def get_evolutionary_line(starter_pokemon):
    #  return(starter_pokemon.evolution)
    list = []
    # list.append(starter_pokemon)

    current = starter_pokemon
    while current is not None:
        # add something to list
        # list.append(current)
        list.append(current.name)

        # move to next evolution
        # current = current.
        current = current.evolution
    
    return list
     
# Example Usage:
print("-------------------")
charizard = Pokemon("Charizard", ["fire", "flying"])
charmeleon = Pokemon("Charmeleon", ["fire"], charizard)
charmander = Pokemon("Charmander", ["fire"], charmeleon)

charmander_list = get_evolutionary_line(charmander)
print(charmander_list)

charmeleon_list = get_evolutionary_line(charmeleon)
print(charmeleon_list)

charizard_list = get_evolutionary_line(charizard)
print(charizard_list)

# Example Output:
# [`Charmander`, `Charmeleon`, `Charizard`]
# [`Charmeleon`, `Charizard`]
# ['Charizard']

'''
Problem 9: Node Class
A linked list is a new data type that, similar to a normal list or array, allows us to store pieces of data sequentially. The difference between a linked list and a normal list lies in how each element is stored in a computer’s memory.

In a normal list, individual elements of the list are stored in adjacent memory locations according to the order they appear in the list. If we know where the first element of the list is stored, it’s really easy to find any other element in the list.

In a linked list, the individual elements called nodes are not stored in sequential memory locations. Each node may be stored in an unrelated memory location. To connect nodes together into a sequential list, each node stores a reference or pointer to the next node in the list.

Using the provided Node class below, create two nodes:

The first node should have value a and be stored in a variable node_one.
The second node should have value b and be stored in a variable node_two.
You do not need to connect the nodes together yet.

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
Example Usage:

print(node_one.value) 
print(node_one.next) 
print(node_two.value)
print(node_two.next) 
Example Output:

a
None
b
None
✨ AI Hint: Linked Lists
'''

'''
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

node_one = Node("a")
node_two = Node("b")

# Example Usage:
print("-------------------")
print(node_one.value) 
print(node_one.next) 
print(node_two.value)
print(node_two.next) 

# Example Output:
# a
# None
# b
# None
'''

'''
Problem 10: Linking Nodes
Building off the Node class from Problem 9, now we will link the nodes together.

To link the nodes, we can set a node's next attribute to hold another node. Update node_one from the Problem 9 to point to node_two.

Example Usage (after updating node_one's next property):

print(node_one.value)
print(node_one.next.value)
print(node_two.value)
Example Output:

a
b
b
'''


class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

# node_one = Node("a", node_two)
node_two = Node("b")
node_one = Node("a", node_two)

# Example Usage (after updating node_one's next property):
print("-------------------")
print(node_one.value)
print(node_one.next.value)
print(node_two.value)

# Example Output:
# a
# b
# b



'''
Problem 11: Mario Party
Create the list ["Mario", "Luigi", "Wario", "Toad"] as a linked list given the Node class:

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
Result Linked List would be: Mario -> Luigi -> Wario -> Toad

Example Usage (after completing the problem with variable names node_1, node_2, node_3, and node_4.):

print(node_1.value, "->", node_1.next.value)
print(node_2.value, "->", node_2.next.value)
print(node_3.value, "->", node_3.next.value)
print(node_4.value, "->", node_4.next)
Example Output:

Mario -> Luigi
Luigi -> Wario
Wario -> Toad
Toad -> None
'''
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
          
# Result Linked List would be: Mario -> Luigi -> Wario -> Toad
# Example Usage (after completing the problem with variable names node_1, node_2, node_3, and node_4.):

# node_1, node_2, node_3, node_4
# node_1 = Node("Mario", node_2)
# node_2 = Node("Luigi", node_3)
# node_3 = Node("Wario", node_4)
# node_4 = Node("Toad", None)
node_4 = Node("Toad")
node_3 = Node("Wario", node_4)
node_2 = Node("Luigi", node_3)
node_1 = Node("Mario", node_2)

print("-------------------")
print(node_1.value, "->", node_1.next.value)
print(node_2.value, "->", node_2.next.value)
print(node_3.value, "->", node_3.next.value)
print(node_4.value, "->", node_4.next)

# Example Output:
# Mario -> Luigi
# Luigi -> Wario
# Wario -> Toad
# Toad -> None


'''
Problem 12: Printing Linked List
Write a function print_linked_list() that takes in a head node as a parameter and prints the linked list using the string " -> " to separate each node.

Note: The "head" of a linked list is the first element in the linked list, equivalent to lst[0] of a normal list.

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next= next
		
def print_linked_list(head):
	pass
Example Input:

# input linked list: a->b->c->d->e
print_linked_list(a)
Example Output:

a -> b -> c -> d -> e
💡 Hint: Linked List Traversal
'''
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next= next
		
def print_linked_list(head):
    current = head
    values = []

    # while current is not None:
    #     print(current.value)
    #     if (current.next is not None):
    #         print(" -> ")
    #     current = current.next

    while current is not None:
        values.append(current.value)
        current = current.next
        
    print(" -> ".join(values))

# Example Input:
# input linked list: a->b->c->d->e
e = Node("e")
d = Node("d", e)
c = Node("c", d)
b = Node("b", c)
a = Node("a", b)
print_linked_list(a)

# Example Output:
# a -> b -> c -> d -> e