# Problem 4
# Write a program that accepts three values that represent 
# cost of order, tip percentage, and tax percentage and calculates 
# and displays the final purchase cost/price
print("Enter cost of order, tip percentage, and tax percentage for total cost")

cost = input("Cost of order: ")
tip = input("Tip percentage: ").strip('%')
tax = input("Tax percentage: ").strip('%')

tipdec = float(tip) * 0.01
tip = float(cost) * tipdec
taxdec =float(tax) * 0.01
tax = float(cost) * taxdec

total = float(cost) + tip + tax
print("Total cost is: $", total)
