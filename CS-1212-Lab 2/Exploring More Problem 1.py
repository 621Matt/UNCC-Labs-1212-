# Module 2
# Use this file to complete the Explore More problem
#Given two integer numbers, one is the number of teachers and the other is the number of apples. We want to distribute the apples evenly among them. The remaining (the indivisible) part remans in the basket. Write an algorithm using pseudocode that would display the number of apples each single teacher gets and the number of apples remaining in the basket. Translate your algorithm to Python code. 

print("Please enter the number of teachers and apples.")
teacher = int(input("Enter the amount of teachers: "))
apple = int(input("Enter the amount of apples: "))

if apple >= teacher:
    apple_for_teacher = apple // teacher
    remainder = apple % teacher
    print("Each teacher gets", apple_for_teacher, "apples.")
    print("Apples left in basket: ",remainder)
else:
    print("Not enough apples to evenly distribute.")