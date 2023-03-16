# ⭐️ GLOSSARY ⭐️

# a function is a named sequence of statements that performs a computation. 
# parameter: A name used inside a function to refer to the value passed as an argument.
def welcome(name):
# body: The sequence of statements inside a function definition.
    # local variable: A variable defined inside a function. A local variable can only be used inside its function.
    greeting = "nice to meet you"
    # return value: The result of a function. If a function call is used as an expression, the return value is the value of the expression.
    # fruitful function: A function that returns a value.
    return name, greeting

# function call: A statement that runs a function. It consists of the function name followed by an argument list in parentheses.
# argument: A value provided to a function when the function is called. This value is assigned to the corresponding parameter in the function.
fruit_funct = welcome('Drael')
print(fruit_funct)

# void function: A function that always returns None.
def void_fun(x):
    print(x*10)

void_fun(9)

# None: A special value returned by void functions.
type(None)

# import statement: A statement that reads a module file and creates a module object.
import math

# dot notation: The syntax for calling a function in another module by specifying the module name followed by a dot (period) and the function name.
math.sqrt(9)

# ⭐️ OTHER TERMS ⭐️ 

# module: A file that contains a collection of related functions and other definitions.
# module object: A value created by an import statement that provides access to the values defined in a module.
# composition: Using an expression as part of a larger expression, or a statement as part of a larger statement.
# flow of execution: The order statements run in.
# stack diagram: A graphical representation of a stack of functions, their variables, and the values they refer to.
# frame: A box in a stack diagram that represents a function call. It contains the local variables and parameters of the function.
# traceback: A list of the functions that are executing, printed when an exception occurs.

# ⭐️ EXERCISES⭐️

# 💢 Exercise 3.1.

#Write a function named right_justify that takes a string named s as a parameter and prints the string with enough leading spaces so that the last letter of the string is in column 70 of the display.

def right_justify(s):
    space = ' '
    seventy = 70 - len(s)
    spaces = space * seventy
    print(spaces+s)

right_justify('monty')

# 💢 Exercise 3.2

# A function object is a value you can assign to a variable or pass as an argument. For example, do_twice is a function that takes a function object as an argument and calls it twice:
# Modify do_twice so that it takes two arguments, a function object and a value, and calls the function twice, passing the value as an argument.

def do_twice(fun,val):
    fun(val)
    fun(val)

#Copy the definition of print_twice from earlier in this chapter to your script
def print_twice(bruce):
    print(bruce)
    print(bruce)

# Use the modified version of do_twice to call print_twice twice, passing 'spam' as an argument
do_twice(print_twice,'spam')

# 💢 Exercise 3.3.

#Write a function that draws a grid 
plus = '+ '
minus = '- '
line = '|'
space= ' '

def grid():

    print(plus+ (minus*4)+ plus+(minus*4)+ plus)
    print(line+(space*9)+line+(space*9)+line)
    print(line+(space*9)+line+(space*9)+line)
    print(line+(space*9)+line+(space*9)+line)
    print(line+(space*9)+line+(space*9)+line)
    print(plus+ (minus*4)+ plus+(minus*4)+ plus)
    print(line+(space*9)+line+(space*9)+line)
    print(line+(space*9)+line+(space*9)+line)
    print(line+(space*9)+line+(space*9)+line)
    print(line+(space*9)+line+(space*9)+line)
    print(plus+ (minus*4)+ plus+(minus*4)+ plus)


grid()

def big_grid():
    row = (plus +(minus*4)+ plus +(minus*4)+ plus +(minus*4)+ plus+(minus*4)+ plus)
    column = line+(space*9)+line+(space*9)+line+(space*9)+line+(space*9)+line
    print(row)
    print(column)
    print(column)
    print(column)
    print(column)
    print(row)
    print(column)
    print(column)
    print(column)
    print(column)
    print(row)
    print(column)
    print(column)
    print(column)
    print(column)
    print(row)
    print(column)
    print(column)
    print(column)
    print(column)
    print(row)


big_grid()