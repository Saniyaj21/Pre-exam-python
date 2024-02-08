# Write a python program to check that an user input year is leap year
# or not.

flag = False
year  = int(input("Eneter a year to check if Leap Year or not : "))
if year % 4 == 0:
    flag = True
    if year % 100 == 0:
        if year % 400 != 0:
            flag = False
if flag:
    print(f"{year} is leap Year.")
else:
    print(f'{year} is not leap')