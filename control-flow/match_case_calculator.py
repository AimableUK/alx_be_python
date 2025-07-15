num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
operation = input("Choose the operation (+, -, *, /):")

result = 0
if operation == "+":
    result = num1 + num2

elif operation == "-":
    result = num1 - num2

elif operation == "*":
    result = num1 * num2

elif operation == "/":
    try:
        result = num1 / num2
    except ZeroDivisionError:
        print("Cannot divide by zero.")

else:
    result = "Operation Invalid"

print(f"The result is {result}")
