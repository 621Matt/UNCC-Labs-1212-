# Problem 3
#Consider the code in lab03_p3.py, that takes two numbers and calculates the average. Before running it try to do it on a paper and use a calculator. What is the average of two numbers like: 7 and 9? Now, run the program with these numbers. Do you get the result you expected? Obviously, your result is wrong, but Python is not complaining at all! This is because a logical or semantic mistake has been made. There is nothing wrong with the syntax, but your calculation is wrong. Fix the code to give you the expected result every time, with any pair of numbers the user specifies.

x = float(input('Enter a number: '))

y = float(input('Enter a number: '))

z = (x+y)/2

print('The average of the two numbers you have entered is: ',z)