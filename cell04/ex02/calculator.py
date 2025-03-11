num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
addition = num1 + num2
subiraction = num1 - num2
multiplication = num1 * num2
if num2 != 0:
    division = num1 / num2
else:
    division = "undefined (division by zero)"
print(f"The sum of {num1} and {num2} is: {addition}")
print(f"The difference between {num1} and {num2} is: {subiraction}")
print(f"The product of {num1} and {num2} is: {multiplication}")
print(f"The division of{num1} and {num2} is: {division}")