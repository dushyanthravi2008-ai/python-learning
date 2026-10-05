num1, num2, num3, num4=int(input("enter the number1: ")), int(input("enter the number2: ")), int(input("enter the number3: ")), int(input("enter the number4: "))
if num1>num2 and num1>num3 and num1>num4:
    print("the greater number is:", num1)
elif num2>num1 and num2>num3 and num2>num4:
    print("the greater number is:", num2)
elif num3>num1 and num3>num2 and num3>num4:
    print("the greater number is:", num3)
else:
    print("the greater number is:", num4)