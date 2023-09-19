# Problem 2
# Write a program that accepts am integer value 
# and prints its previous and next numbers
# separated by a comma.

print("Enter an integer number:")
num1 = input("First Number:")
prev = int(num1) - 1
next1 = int(num1) + 1
print(prev,",",num1,",",next1)