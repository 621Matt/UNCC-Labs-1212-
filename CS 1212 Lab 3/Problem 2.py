# Problem 2
#Consider the code in lab03_p2.py. We want the user to enter the age of their dog and we want to write a program that will output the age of the dog in human years. The rule you want your program to follow is that 1 dog year is 7 human years. We wrote some code for you, but it has some errors. Fix the code to give you the expected result every time, with any number the user specifies.
#For example, if my dog is 7 years old, I expect to see the following output: Your dog’s age is equivalent to 49 human years.

dog_year = input("Please provide your dog's age:")

to_human = int(dog_year) * 7

print("Your dog's age is equivalent to", to_human, "human years")