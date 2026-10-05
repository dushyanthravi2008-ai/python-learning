number1 = input("Enter the first number: ")
num1 = float(number1)
sign = input("Enter the operator sign (+, -, *, /): ")
number2 = input("Enter the second number: ")
num2 = float(number2)
if sign == "+":
    result = num1 + num2
    print("The result is: ", result)
elif sign == "-":
    result = num1 - num2
    print("The result is: ", result)
elif sign == "*":
    result = num1 * num2
    print("The result is: ", result)
elif sign == "/":
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        result = num1 / num2
        print("The result is: ", result)
else:
    print("Error: Invalid operator sign.")
    