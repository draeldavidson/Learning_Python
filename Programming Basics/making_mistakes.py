# ⭐️ GLOSSARY ⭐️

# Program: is a sequence of instructions that specifies how to perform a computation. The computation might be something mathematical, such as solving a system of equations or finding the roots of a polynomial, but it can also be a symbolic computation, such as searching and replacing text in a document or something graphical, like processing an image or playing a video.

# print statement: An instruction that causes the Python interpreter to display a value on the screen.
print('Hello, World')

# input: Get data from the keyboard, a file, the network, or some other device.
print('Enter your name:')
# prompt: Characters displayed by the interpreter to indicate that it is ready to take input from the user.
i = input()
print('Hello, ' + i)

# output: Display data on the screen, save it in a file, send it over the network, etc.
    # Hello, Drae

# math: Perform basic mathematical operations like addition and multiplication. conditional execution: Check for certain conditions and run the appropriate code.
import math # to use built in math functions

# repetition: Perform some action repeatedly, usually with some variation.
tap = 'tap '
print(tap * 3)

# operator: A special symbol that represents a simple computation like addition, multiplication, or string concatenation.
print(2+4)

# value: One of the basic units of data, like a number or string, that a program manipulates.
name = 'Drae' #the value is 'Drae'

# type: A category of values. The types we have seen so far are integers (type int), floatingpoint numbers (type float), and strings (type str).
# integer: A type that represents whole numbers.
print('the type 45 is',type(45))

# floating-point: A type that represents numbers with fractional parts.
print('the type 45.0 is',type(45.0))

# string: A type that represents sequences of characters.
print('the type 45 is',type('45'))

# token: One of the basic elements of the syntactic structure of a program, analogous to a word in a natural language.
    # Keywords there are 33 keywords in python
    # Identifiers: names given to any variable, function, class, list, methods, etc. for their identification. 
    # Literals or Values: String literals, Numeric literals, Boolean literals, Literal Collections, Special literals
    # Operators: + - * / % ** //
    # Punctuators: [ ] { } ( ) @  -=  +=  *=  //=  **==  = , etc.

# bug: An error in a program.
#prnt('Oh no there is a bug')
    # Output: Traceback (most recent call last):
    #    prnt('Oh no there is a bug')
    # NameError: name 'prnt' is not defined

# debugging: The process of finding and correcting bugs.
print('Oh no there is a bug')


# ⭐️ OTHER TERMS ⭐️ 

# problem solving: The process of formulating a problem, finding a solution, and expressing it.
# high-level language: A programming language like Python that is designed to be easy for humans to read and write.
# low-level language: A programming language that is designed to be easy for a computer to run; also called “machine language” or “assembly language”.
# portability: A property of a program that can run on more than one kind of computer.
# interpreter: A program that reads another program and executes it
# natural language: Any one of the languages that people speak that evolved naturally.
# formal language: Any one of the languages that people have designed for specific purposes, such as representing mathematical ideas or computer programs; all programming languages are formal languages.
# syntax: The rules that govern the structure of a program.
# parse: To examine a program and analyze the syntactic structure.

# ⭐️ EXERCISES⭐️

# 💢 Exercise 1.1.

# MAKING MISTAKES on purpose helps you understand errors and what they could mean

print('Hello World!')

# what happens if you leave out one of the quotation marks? What if you leave out both?
#print('Hello World!)
    # Output: SyntaxError: unterminated string literal (detected at line 6)
# print(Hello World)
    #Output:print(Hello World)
    #             ^^^^^^^^^^^
    #SyntaxError: invalid syntax. Perhaps you forgot a comma?

# What if you spell print wrong?
#prit('Hello World!')
    #Output: NameError: name 'prit' is not defined. Did you mean: 'print'?

# what happens if you leave out one of the parentheses, or both?
# print("Hello World!"
    # Output: SyntaxError: '(' was never closed

#print"Hello World!"
    #Output: SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?

# If you are trying to print a string, what happens if you leave out one of the quotation marks, or both?
    #See Example Above

# You can use a minus sign to make a negative number like -2. What happens if you put a plus sign before a number? What about 2++2?
print(-2)
    # Output: -2
print(+2)
    # Output: 2
print(2++2)
    # Output: 4

# In math notation, leading zeros are ok, as in 02. What happens if you try this in Python?
#print(09)
    # Output: SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers

# What happens if you have two values with no operator between them?
#print(7 8)
    #Output: SyntaxError: invalid syntax. Perhaps you forgot a comma?

# 💢 Exercise 1.2.

# How many seconds are there in 42 minutes 42 seconds?
time_minutes = 42
time_seconds = 42
total_seconds = (time_minutes*60)+time_seconds

#f is a Literal String Interpolation or more commonly as F-strings a convenient way to embed python expressions inside string literals for formatting.
print(f'There are {total_seconds} seconds in {time_minutes} minutes {time_seconds} seconds')
    #Output: There are 2562 seconds in 42 minutes 42 seconds

# How many miles are there in 10 kilometers? Hint: there are 1.61 kilometers in a mile.
kilometers = 10
total_miles = (kilometers/1.61)
print(f'There are {total_miles} miles in {kilometers} kilometers')
    #Output: There are 6.211180124223602 miles in 10 kilometers

# If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average pace (time permile in minutes and seconds)? What is your average speed in miles per hour?
seconds_in_hr = 60*60
speed = (total_miles)/(total_seconds/seconds_in_hr)
print(f'If you run a {kilometers} kilometer race in {time_minutes} minutes {time_seconds} seconds, your average pace is {speed} mph')
    #Output: If you run a 10 kilometer race in 42 minutes 42 seconds, your average pace is 8.727653570337614 mph
