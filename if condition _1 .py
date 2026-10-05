# if condition: This program checks if a number is divisible by 9 and prints the result.
num=int(input("Enter a number: "))
if num%9==0:
    print("the number is divisible by 9")
    print("the number is divisible by 9 by:", num/9)
else:
    print("the number is not divisible by 9")
    print("the number is not divisible by 9 by as it has decimal value of:", num/9)
