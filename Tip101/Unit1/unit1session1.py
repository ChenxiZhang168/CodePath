from typing import List

# Unit 1: Session 1

# Problem 1: Hello World!
# Given the following lines of code, work with your group members to place the lines in order and write and call your first Python function!
# a. print("Hello world!")
# b. def hello_world():
# c. hello_world()
# The correct order of the lines of code is:
def hello_world():
    print("Hello world!")
hello_world()

# Problem 2: Today's Mood
# The following function uses a variable, mood to print out "Today's mood: 😎". Copy this code into your IDE and update the mood variable to print out your mood for today.
# def todays_mood():
#     mood = "😎"
#     print("Today's mood: " + mood)
# todays_mood()
# Example Output: Today's mood: 🥱
def todays_mood():
    mood = "🥱"
    print("Today's mood: " + mood)
todays_mood()

# Problem 3: Return Doubled List
# The following function accepts one parameter menu. Copy this code into your IDE and add a function call so that "Lunch today is: 🍕" is printed to the console.
# def print_menu(menu):
#     print("Lunch today is: " + menu)
# Example Output: Lunch today is: 🍕
def print_menu(menu):
    print("Lunch today is: " + menu)
print_menu("🍕")

# Problem 4: Sum of Two Integers
# The following function returns the sum of two integers: a and b.
# def sum(a, b):
#     return a + b
# Use the sum() function to calculate the sum of 13 and 27. Then, use the sum() function again to double the calculated sum and print the result to the console.
# Note: Do not use any mathematical operators such as +, -, *, or / when solving this problem.
# Example Input: 20 and 8
# Example Output: 56
def sum(a, b):
    return a + b
print(sum(sum(13, 27), sum(13, 27)))

# Problem 5: Product of Two Integers
# Write a function product() that returns the product of two integers, a and b.
# Example Input: 22 and 7
# Example Result: 154
def product(a, b):
    return a * b
print(product(22, 7))

# Problem 6: Classify Age
# Write a function classify_age() that takes an integer age as a parameter and returns "child" if the age is less than 18, and returns "adult" otherwise.
# Example Usage:
# output = classify_age(18)
# print(output)
# output = classify_age(7)
# print(output)
# output = classify_age(50)
# print(output)
# Output:
# adult
# child
# adult
def classify_age(age: int) -> str:
    if age < 18:
        return "child"
    else:
        return "adult"
output = classify_age(18)
print(output)
output = classify_age(7)
print(output)
output = classify_age(50)
print(output)

# roblem 7: What time is it?
# Let's put what we learned in Problems 1-4 all together! Write a function named what_time_is_it() that takes an integer hour as a parameter.
# If hour is 2, the function should return "taco time 🌮".
# If hour is 12, the function should return "peanut butter jelly time 🥪”.
# Otherwise, the function should return "nap time 😴".
# ----------------------
# Example Usage:
# ----------------------
# time = what_time_is_it(2)
# print(time)
# time = what_time_is_it(7)
# print(time)
# time = what_time_is_it(12)
# print(time)
# Output:
# ----------------------
# taco time 🌮
# nap time 😴
# peanut butter jelly time 🥪
# def what_time_is_it(hour: int) -> str:
def what_time_is_it(hour):
    if hour == 2:
        return "taco time 🌮"
    elif hour == 12:
        return "peanut butter jelly time 🥪"
    else:
        return "nap time 😴"
print(what_time_is_it(2))
print(what_time_is_it(7))
print(what_time_is_it(12))

# Problem 8: Blackjack
# In the game Blackjack, players try to draw a hand of cards that totals as close to 21 as possible. Players "bust" if their cards total more than 21. Players say "Hit me!" if they want the dealer to give them another card.
# ---------------------------------
# Write a function called blackjack() that takes an integer score as a parameter.
# If score equals 21, print "Blackjack!".
# If score is greater than 21, print "Bust!".
# If score is greater than or equal to 17 and less than 21, print "Nice hand!".
# If score is less than 17, print "Hit me!".
# ---------------------------------
# Example Usage:
# ---------------------------------
# blackjack(21)
# blackjack(24)
# blackjack(19)
# blackjack(10)
# Output:
# ---------------------------------
# Blackjack!
# Bust!
# Nice hand!
# Hit me!
d