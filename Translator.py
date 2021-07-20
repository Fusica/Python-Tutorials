# Editor: Max

# Create Time: 7/20/21 10:14 PM

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "aeiou":
            translation = translation + "g"
        elif letter in "AEIOU":
            translation = translation + "G"
        else:
            translation = translation + letter
    return translation


print(translate(input("Enter a phrase: ")))

