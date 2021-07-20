# Editor: Max

# Create Time: 7/19/21 9:59 AM

# n = int(input().strip())
# if n % 2 != 0:
#     print("Weird")
# elif n % 2 == 0 and 2 <= n <= 5:
#     print(" Not Weird")
# elif n % 2 == 0 and 6 <= n <= 20:
#     print("Weird")
# elif n % 2 == 0 and n > 20:
#     print(" Not Weird")

n = int(input())
result = ""
for index in range(n):
    result = result + str(index + 1)
print(result)
