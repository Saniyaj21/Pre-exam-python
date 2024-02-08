# Write a python program to find the smallest number among three user
# input numbers.

print("Enter 3 numbers : ")
num = []
for i in range(3):
    n = int(input(f'Enter {i+1}st num : '))
    num.append(n)

print(f"Biggest num is : {max(num)}")
