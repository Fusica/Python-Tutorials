# Editor: Max

# Create Time: 7/21/21 1:08 AM

try:
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err1:
    print(err1)
except ValueError as err2:
    print(err2)
