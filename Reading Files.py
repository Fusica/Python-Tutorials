# Editor: Max

# Create Time: 7/21/21 1:09 AM

employee_file = open("employee.txt", "r")

# print(employee_file.readable())  # see if this file can be operated
# print(employee_file.read())      # print all
for line in employee_file:
    print(line)

employee_file.close()

