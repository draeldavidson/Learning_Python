# ⭐️ GLOSSARY ⭐️

# variable: A name that refers to a value.
cat = 'cat is the variable'

# assignment: A statement that assigns a value to a variable.
    # the equal sign is the assignment

# operand: One of the values on which an operator operates.
print(4 + 5) #the 4 and 5 are operands

# expression: A combination of variables, operators, and values that represents a single result.
express = 4 + 5 # This is a expression

# statement: A section of code that represents a command or action. So far, the statements we have seen are assignments and print statements.
print(express) # This and the above is a statement

# evaluate: To simplify an expression by performing the operations in order to yield a single value.
print(4+5*10) 

# order of operations: Rules governing the order in which expressions involving multiple operators and operands are evaluated.
 #P.E.M.D.A.S

# concatenate: To join two operands end-to-end.
a = 'concatenate: '
b = 'To join two operands end-to-end.'
print(a + b)

# comment: Information in a program that is meant for other programmers (or anyone reading the source code) and has no effect on the execution of the program.

# ⭐️ OTHER TERMS ⭐️ 

# state diagram: A graphical representation of a set of variables and the values they refer to.
# keyword: A reserved word that is used to parse a program; you cannot use keywords like if, def, and while as variable names.
# execute: To run a statement and do what it says.
# interactive mode: A way of using the Python interpreter by typing code at the prompt.
# script mode: A way of using the Python interpreter to read code from a script and run it.
# script: A program stored in a file.
# syntax error: An error in a program that makes it impossible to parse (and therefore impossible to interpret).
# exception: An error that is detected while the program is running.
# semantics: The meaning of a program.
# semantic error: An error in a program that makes it do something other than what the programmer intended.

# ⭐️ EXERCISES⭐️

# Try it in interactive mode and make errors on purpose to see what goes wrong.

# We’ve seen that n = 42 is legal. What about 42 = n?
    #42 = n
    #SyntaxError: cannot assign to literal

# How about x = y = 1?
    #x = y = 1
    #SyntaxError: cannot assign to literal

# In some languages every statement ends with a semi-colon, ;. What happens if you put a semi-colon at the end of a Python statement?
sem=1;
print(sem)
    #Adding a semicolon does not affect the statement.

# What if you put a period at the end of a statement?
    #print(h).
    #SyntaxError: invalid syntax

# In math notation you can multiply x and y like this: xy. What happens if you try that in Python? The volume of a sphere with radius r is 4/3πr^3
    # xy
    # NameError: name 'xy' is not defined. Did you mean: 'x'?

# What is the volume of a sphere with radius 5?
pie = 3.14
x = 4/3
rad = 5**3
vol = x*pie*rad
print(vol)

# Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. Shipping costs $3 for the first copy and 75 cents for each additional copy. What is the total wholesale cost for 60 copies?
book= 24.95
discount= book*.40
indbook=book-discount
print("individual book =", indbook)
firstcopy=indbook+3
othercopy=indbook+.75
print("first copy =", firstcopy, " & other copies will =", othercopy, ", each.")
sixtybooks= firstcopy+(59*othercopy)
print('sixty books =',sixtybooks)


# If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at tempo (7:12 per mile) and 1 mile at easy pace again, what time do I get home for breakfast?
onemi=8*60+15
threemi=3*(7*60+12)
print(onemi, " ", threemi)
totime=(onemi+threemi+onemi)/60
print(totime)
    #38.1
