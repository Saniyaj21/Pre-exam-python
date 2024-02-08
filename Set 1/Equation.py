# Write a python program to calculate the value of ax^3 + bx^2 +c = 0 (The
# value of a, b, c and x are taken from users).

a = int(input("Enter a value of a : "))
b = int(input("Enter a value of b : "))
c = int(input("Enter a value of c : "))
x = int(input("Enter a value of x : "))

result = a*x**3 + b*x**2 + c

print("The result is : ", result)
