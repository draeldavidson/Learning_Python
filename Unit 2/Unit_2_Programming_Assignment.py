# Write a function in this file called nine_lines that uses the function three_lines (provided below) to print a total of nine lines.
def new_line():
    print('.')

def three_lines():
    new_line()
    new_line()
    new_line()
# Now add a function named clear_screen that uses a combination of the functions nine_lines, three_lines, and new_line (provided below) to print a total of twenty-five lines. 
# The last line of your program should call first nine_lines and then the clear_screen function.
# The  function three_lines and new_line are defined below so that you can see nested function calls. 
# Also, to make counting “blank” lines visually easier, the print command inside new_line will print a dot at the beginning of the line:

# ⭐️ MY SUBMISSION ⭐️

# Function called nine_lines
def nine_lines():
    #uses three_lines to print a total of nine lines.
    three_lines()
    three_lines()
    three_lines()

# add a function clear_screen that uses a combination of the functions
def clear_screen():
    #print a total of twenty-five lines.
    new_line()
    three_lines()
    three_lines()
    nine_lines()
    nine_lines()

# call first nine_lines and then the clear_screen function.
print("✅ printing nine_lines")
nine_lines()

print("✅ printing twenty-five lines")
clear_screen()







