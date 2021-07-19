# Editor: Max

# Create Time: 7/19/21 10:12 PM

def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result


print(raise_to_power(2, 12))
