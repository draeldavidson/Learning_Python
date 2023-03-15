# MAKING MISTAKES on purpose helps you understand errors and what they could mean

print('Hello World!')

# ⭐️ what happens if you leave out one of the quotation marks? What if you leave out both?
#print('Hello World!)
    # Output: SyntaxError: unterminated string literal (detected at line 6)
print(Hello World)
    #Output:print(Hello World)
    #             ^^^^^^^^^^^
    #SyntaxError: invalid syntax. Perhaps you forgot a comma?

# ⭐️ What if you spell print wrong?
#prit('Hello World!')
    #Output: NameError: name 'prit' is not defined. Did you mean: 'print'?

# ⭐️ what happens if you leave out one of the parentheses, or both?
# print("Hello World!"
    # Output: SyntaxError: '(' was never closed

#print"Hello World!"
    #Output: SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?

# ⭐️ If you are trying to print a string, what happens if you leave out one of the quotation marks, or both?
    #See Example Above

# ⭐️ You can use a minus sign to make a negative number like -2. What happens if you put a plus sign before a number? What about 2++2?
print(-2)
    # Output: -2
print(+2)
    # Output: 2
print(2++2)
    # Output: 4

# ⭐️ In math notation, leading zeros are ok, as in 02. What happens if you try this in Python?
#print(09)
    # Output: SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers

# ⭐️ What happens if you have two values with no operator between them?
#print(7 8)
    #Output: SyntaxError: invalid syntax. Perhaps you forgot a comma?

# ⭐️ How many seconds are there in 42 minutes 42 seconds?
time_minutes = 42
time_seconds = 42
total_seconds = (time_minutes*60)+time_seconds

#f is a Literal String Interpolation or more commonly as F-strings a convenient way to embed python expressions inside string literals for formatting.
print(f'There are {total_seconds} seconds in {time_minutes} minutes {time_seconds} seconds')
    #Output: There are 2562 seconds in 42 minutes 42 seconds

# ⭐️ How many miles are there in 10 kilometers? Hint: there are 1.61 kilometers in a mile.
kilometers = 10
total_miles = (kilometers/1.61)
print(f'There are {total_miles} miles in {kilometers} kilometers')
    #Output: There are 6.211180124223602 miles in 10 kilometers

# ⭐️ If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average pace (time permile in minutes and seconds)? What is your average speed in miles per hour?
seconds_in_hr = 60*60
speed = (total_miles)/(total_seconds/seconds_in_hr)
print(f'If you run a {kilometers} kilometer race in {time_minutes} minutes {time_seconds} seconds, your average pace is {speed} mph')
    #Output: If you run a 10 kilometer race in 42 minutes 42 seconds, your average pace is 8.727653570337614 mph
