def right_justify(s):
    space = ' '
    seventy = 70 - len(s)
    spaces = space * seventy
    print(spaces+s)

right_justify('monty')