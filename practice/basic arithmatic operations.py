num1=float(input("Enter the first number: "))
num2=float(input("Enter the second number: "))
print("choose the operation you want to perform (1-4): 1-addition, 2-subtraction, 3-multiplication, 4-division")
choice=int(input("Enter your choice"))
if choice==1:
    result=num1+num2
    print("The result is: ", result)
elif choice==2:
    result=num1-num2
    print("The result is: ", result)
elif choice==3:
    result=num1*num2
    print("The result is: ", result)
elif choice==4:
    if num2==0:
        print("Error: Division by zero is not allowed.")
    else:
        result=num1/num2
        print("The result is: ", result)
else:
    print("Error: Invalid choice.")
