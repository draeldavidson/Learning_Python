# ⭐️ UNIT 2 JOURNAL ASSIGNMENT ⭐️

# PART 1:

# Write a function called print_volume(r) that takes an argument for the sphere's radius and prints the sphere's volume.
# Call your print_volume function three times with different values for radius.

import math

# Write a function called print_volume(r) that takes an argument.
def print_volume(r):
    volume = (4/3)*(math.pi)*(r**3)
    # print the sphere's volume.
    print(f"The volume of a sphere with the radius of {r} is {volume}")

# Call your print_volume function three times with different values for radius.
print_volume(2)
print_volume(5)
print_volume(10)

# PART 2:

# Write your own function that illustrates a feature that you learned in this unit. 
# (Variables Expressions Statements Functions)

def my_greeting(name,birth_year):
    age = 2023-birth_year
    print(f'Hello, my name is {name} I was born in {birth_year} this year i will be {age}')

my_greeting("Robert", 2000)
my_greeting("Bob", 1983)
my_greeting("Suzie", 1973)

# The function that I created is called my_greeting, the parameters are name and birth year. 
# The feature of this function is to take the arguments, and put it into a sentence. 
# Also to take birth_year and subtract it from the current year, in order to estimate an age. 
# When using this function, you only have to enter your name and a birth year.
# The function will automatically enter it into the sentence, and calculate your approximate age.
