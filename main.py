num1 = input("Enter a number: ")
op = input("Enter operator (+, -, *, /): ")
num2 = input("Enter another number: ")

num1 = float(num1)
num2 = float(num2)

if op == '+':
    result = num1 + num2
    print(f"The sum of {num1:.0f} and {num2:.0f} is: {result}")
elif op == '/':
    result = num1 / num2
    print(f"The sum of {num1:.0f} and {num2:.0f} is: {result}")
elif op == '*':
    result = num1 * num2
    print(f"The sum of {num1:.0f} and {num2:.0f} is: {result}")
elif op == '-':
    result = num1 - num2
    print(f"The sum of {num1:.0f} and {num2:.0f} is: {result}")
else:
    print("Invalid Operator")



