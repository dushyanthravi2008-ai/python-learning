import datetime
name=input("Enter the name: ")
year_of_birth=int(input("Enter the year of birth: "))
current_year=datetime.datetime.now().year
age=current_year-year_of_birth
if age>=60:
    print(f"\n{name} is a senior citizen")
else:
    print(f"\n{name} is not a senior citizen")
