num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
choice=int(input("\n enter the choice : 1:addition, 2:subtraction, 3:multiplication, 4:division:"))
if choice==1:
    print(f" The result is: {num1+num2}")
elif choice==2:
    print(f" The result is: {num1-num2}")
elif choice==3:
    print(f" The result is: {num1*num2}")
elif choice==4:
    if num2==0:
        print("Error: Division by zero is not allowed.")
    else:
        print(f" The result is: {num1/num2}")
else:
    print("Error: Invalid choice.")