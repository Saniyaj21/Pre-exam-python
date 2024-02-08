# Write a python program to compute the sum of digits of an user input
# number using loop.

num = int(input("Enter a num : "))
sum = 0
for i in str(num):
    sum += int(i)

print(sum)