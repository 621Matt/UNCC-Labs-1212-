# Problem 6
#n the prepwork you were introduced to the random  module. Another useful Python module is the  math module. It has several implementations of the most common math functions that might be needed for some computational solutions. This page is the official  math moduleLinks to an external site. documentation. Programmers refer to the documentation to help them understand how they can incorporate these existing solutions into their own solutions.  Start by reviewing the documentation page for the mathLinks to an external site. module and make a note of some of the functions listed on that page. For this problem we want to use the ceil, pow and sqrt functions. Your task is to design and implement a program in lab03_p6.py that asks the user to enter a real number and prints the result of the square root of that number cubed rounded up to the nearest integer.
#For example if the user enters 2 the output would be 3.

import math

rnumber = input("Enter a real number: ")
squared_number = math.sqrt (int(rnumber))
cubed_number = math.pow(3, int(squared_number))
round_number = math.ceil(int(cubed_number))

print("Final Number: ", round_number) 