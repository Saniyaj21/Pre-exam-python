# Write a python program to display DA of an employee based on Basic Salary (BS).
# BS	DA
# If	Rs. 12,000	10%
# If	Rs. 10,000	8%
# If	Rs.  8,000	6%
# If	Rs.  4,000	4%
# Else	2%
bs = int(input("Enter Base Salary of Employee: "))
da = 0

if bs == 12000:
    da = (bs * 10) / 100
elif bs == 10000:
    da = (bs * 8) / 100
elif bs == 8000:
    da = (bs * 6) / 100
elif bs == 4000:
    da = (bs * 4) / 100
else:
    da = (bs * 2) / 100

print("Dearness Allowance (DA):", da)
