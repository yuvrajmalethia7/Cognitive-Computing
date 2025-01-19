# Write a Python program to print "Anything You find cool."

print("Goodbye World")

# 2.1 Write a program to add two numbers and print the result.

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

print(f"a + b = {a+b}")

# 2.2 Write a program to concatenate two strings and print the result.

print("Hello" + "World")

# 2.3 Write a program to concatenate a string and a number and print the result.
word = "Iron Man Mark"
num = 42
print(f"{word} {num}")

# 3.1 Write a Python program to check if a number is positive, negative, or zero using an if-else statement.
number = float(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
# 3.2 Write a program to check if a given number is odd or even.
number = int(input("Enter an integer: "))

if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")
# 4.1 Write a program to print numbers from 1 to 10 using a for loop.

for i in range(1, 11):
    print(i)

# 4.2 Write a program to print numbers from 1 to 10 using a while loop.

i = 1
while i <= 10:
    print(i)
    i += 1
# 4.3 Write a program to calculate the sum of numbers from 1 to 100 using a loop.

sum = 0
for i in range(1, 101):
    sum += i

print(sum)

# 5.1 Create a list of 5 numbers. Write a program to find the largest and smallest numbers in the list.

num_list = [10, 50, 40, 39, 63]
print(min(num_list))
print(max(num_list))

# 5.2 Create a dictionary with at least 3 key-value pairs. Write a program to retrieve the value of a given key

dog = {"name": "sid", "age": 21, "gender": "M", "city": "gangtok"}
print(dog.get("name"))

# 5.3 Write a program to sort a list of numbers in ascending and descending order.

num = [34, 65.84, 24, 12, 676, 566, 323]
print(sorted(num))
print(sorted(num, reverse=True))

# 5.4 Write a program to merge two dictionaries into one.

marvel = {"Hluk": "Smash", "Iron Man": "Uni-beam"}
dc = {"Superman": "Heat Vision", "Batman": "Money", "Flash": "Super Speed"}
marvel.update(dc)
print(marvel)

# 6.1 Write a program to count the number of vowels in a given string.

string = input(f"enter a string: ")
count = 0
for i in range(0, len(string)):
    if (
        string[i] == "a"
        or string[i] == "e"
        or string[i] == "i"
        or string[i] == "o"
        or string[i] == "u"
        or string[i] == "A"
        or string[i] == "E"
        or string[i] == "I"
        or string[i] == "O"
        or string[i] == "U"
    ):
        count += 1
print(count)

# 6.2 Write a program to reverse a string and print it.

string = input("Enter a string: ")
revstr = string[::-1]
print(revstr)

# 6.3 Write a program to check if a string is a palindrome.

string = input("Enter a string: ")
revstr = string[::-1]
if string == revstr:
    print("it is palindrome")
else:
    print("it is not palindrome")


# 7.1 Write a program to create a text file, write some text into it, and then read and print the content.

with open("file.txt", "w") as file:
    file.write("Taarak Mehta Ka Ooltah Chashmah\n")
    file.write("Duniya Ne Undha Chasma\n")

with open("file.txt", "r") as file:
    print(file.read())

# 7.2 Write a program to append text to an existing file and print the updated content

with open("file.txt", "a") as file:
    file.write("Jethalal Champaklal Gada, Gada Electronics \n")

with open("file.txt", "r") as file:
    print(file.read())

# 7.3 Write a program to count the number of lines in a text file.

with open("file.txt", "r") as file:
    lines = file.readlines()
print(len(lines))

# 8.1 Write a program to handle division by zero using a try-except block.

try:
    num = int(input("numerator: "))
    deno = int(input("denominator: "))

    ans = num / deno
    print(f"The result is: {ans}")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

# 8.2 Write a program to handle invalid input (e.g., when the user enters a string instead of a number).

try:
    num = int(input("Enter a number: "))
    print(f"Your number is: {num}")
except ValueError:
    print("Error: Invalid input. Please enter a valid integer.")

# 8.3 Write a program to demonstrate the use of finally in exception handling.

try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    ans = a / b
    print(f"The answer is: {ans}")
except ZeroDivisionError:
    print("Error: Cannot divide by zero")
except ValueError:
    print("Error: Please enter valid numbers")
finally:
    print("code is executed")

# 9.1 Write a program to generate 5 random numbers between 1 and 100 and print them.

import random

for _ in range(5):
    print(random.randint(1, 100))

# 9.2 Write a program to generate a random number and check if it is prime.

import random


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


num = random.randint(1, 100)
print(f"Random number: {num}")
print("Prime" if is_prime(num) else "Not Prime")

# 9.3 Write a program to simulate rolling a six-sided die.

import random

print(f"You rolled a: {random.randint(1, 6)}")

# 9.4 Write a program to shuffle a list of numbers.

import random

list = [1, 2, 3, 4, 5]
print(list)
random.shuffle(list)
print(list)

# 9.5 Write a program to randomly select an item from a list.

import random

list = [1, 2, 3, 4, 5]
print(list)
random.shuffle(list)
print(list)

# 9.6 Write a program to generate a random password of given length.

import random
import string

length = int(input("Enter password length: "))
characters = string.ascii_letters + string.digits + string.punctuation
password = "".join(random.choices(characters, k=length))
print(f"Generated password: {password}")


# 9.7 Write a program to pick a random card from a standard deck of 52 cards.

import random

suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
deck = [f"{rank} of {suit}" for suit in suits for rank in ranks]

print(f"Random card: {random.choice(deck)}")

# 10.1 Write a program to accept two numbers as command-line arguments, add them, and print the result.


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("num1", type=int, help="First number")
parser.add_argument("num2", type=int, help="Second number")
args = parser.parse_args()
result = args.num1 + args.num2
print("Sum:", result)

# 10.2 Write a program to accept a string as a command-line argument and print its length.

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("string", type=str, help="Input string")

args = parser.parse_args()

input_string = args.string
string_length = len(input_string)
print("Length of the string:", string_length)


# 11.1 Write a program to use the math library to calculate the square root of a given number.

import math

number = float(input())
print(math.sqrt(number))

#  11.2 Write a program to use the datetime library to print the current date and time.
import datetime

print(datetime.datetime.now())

# 11.3 Write a program to use the os library to list all files in the current directory

import os

print(os.listdir())
