
# ⭐️ Define a function that takes an argument. Call the function. Identify what code is the argument and what code is the parameter.
    # The function my_name takes the parameter ‘name’ and returns a string “Hi, my name is ‘name’”. When calling the function with my_name(“Bob”) the argument is Bob.

def my_name(name):
    print("Hi, my name is",name +'.')

my_name("Bob")


# ⭐️ Call your function from Example 1 three times with different kinds of arguments: a value, a variable, and an expression. Identify which kind of argument is which.

me = "Robert"
full_name = (me+ ' ' + "Robertson")
my_name(me) # This is a variable
my_name(full_name) # This is an expression
my_name('Ned') # This is a value

# ⭐️ Construct a function with a local variable. Show what happens when you try to use that variable outside the function. Explain the results.
    #This is a function that has a local variable x. The way it works is when you call the function you put in an argument, like your birth year, and X subtract that year from 2023 and then it prints of sentence "I am 'x' years old."

def age(year):
    x = 2023 - year
    print(f'I am {x} years old.')

age(2000)

#print(x)
    # Output: NameError: name 'x' is not defined
# When you try to use X outside of the function, you get a trace back error because X is a local variable that isn’t accessible globally.

# ⭐️ Construct a function that takes an argument. Give the function parameter a unique name. Show what happens when you try to use that parameter name outside the function. Explain the results.
#print(year)
    # Output: NameError: name 'year' is not defined
# When trying to call the perimeter “year” from the age function, we receive another trace back error because year is not defined.


# ⭐️ Show what happens when a variable defined outside a function has the same name as a local variable inside a function. Explain what happens to the value of each variable as the program runs.
x="harry"
print(x)
# Output: harry

#As the program runs, the variable x=”harry” is defined outside of the function so print(x) is only able to access the x outside of the function and not the one inside of the function.
