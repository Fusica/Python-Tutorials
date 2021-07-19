# Editor: Max

# Create Time: 7/19/21 4:18 PM

secret_word = "max"
guess = input("Guess a name: ")
i = 0

while guess != secret_word:
    if i < 9:
        guess = input("You guess it wrong, try again: ")
        i += 1
    else:
        print("You are out of time")
        break

if i < 9:
    print("Congrats")
