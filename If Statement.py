# Editor: Max

# Create Time: 7/18/21 3:28 PM

is_male = False
is_tall = True

if is_male and is_tall:  # not use && or ||
    print("You are a tall male")
elif is_male and not is_tall:
    print("You are a short male")
elif not is_male and is_tall:
    print("You are a tall female")
else:
    print("You are not ok")
