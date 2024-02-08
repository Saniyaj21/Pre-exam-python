# Make a calculator to perform addition, subtraction, multiplication and division operations of two
# numbers and display the results.

while(1):
    choice = int(input("Enter 1 for Add\nEnter 2 for Subtrac\nEnter 3 for Multiplication\nEnter 4 for Division\nEnter 5 for Exit\n--> "))
    if choice == 5:
        break
    a = int(input("Enter 1st value : "))
    b = int(input("Enter 2nd value : "))
    
    if choice == 1:
        print(f"{a} + {b} = {a+b}\n") 
    elif choice == 1:
        print(f"{a} + {b} = {a+b}\n") 
    elif choice == 2:
        print(f"{a} - {b} = {a-b}\n") 
    elif choice == 3:
        print(f"{a} * {b} = {a*b}\n") 
    elif choice == 4:
        print(f"{a} / {b} = {a/b}\n") 

