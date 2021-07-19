# Editor: Max

# Create Time: 7/19/21 2:30 PM

def calculator(num1, num2, ope):
    if ope == "+":
        return num1 + num2
    elif ope == "-":
        return num1 - num2
    elif ope == "*":
        return num1 * num2
    elif ope == "/":
        return num1 / num2
    else:
        return "Invalid operator"


# ope = input("Enter an operator: ")
# num1 = int(input("Enter your first num: "))
# num2 = int(input("Enter your second num: "))
# print(calculator(num1, num2, ope))

# Better Version
str1 = input("What you want to calculate? ")
str1.split()
print(calculator(float(str1[0]), float(str1[2]), str1[1]))
