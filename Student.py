# Editor: Max

# Create Time: 7/21/21 5:50 PM

# Use for Classes & Objects.py

class Student:
    def __init__(self, name, major, gpa, is_on_probation):  # Don't type it wrong into "int", that's a rookie mistake
        self.name = name                                    # call function __init__
        self.major = major                                  # actual value of name is self.name
        self.gpa = gpa
        self.is_on_probation = is_on_probation

    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False
