# Write a python program to check that an user input number is prime
# or not?

num = int(input("Enter the number to check prime or not : "))
temp = 0
for i in range (1, num+1):
    if num % i ==  0:
        temp += 1

if temp > 2:
    print(f"{num} is not prime :")
else:
    print(f"{num} is  prime :")














