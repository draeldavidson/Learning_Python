# solving word puzzles by searching for words that have certain properties.

fin = open('Unit 8/words.txt')

def print_fin(txt):
    counter = 0
    for line in txt:
        word = line.strip()
        counter += 1
        print(word)
    print(counter)

# print_fin(fin)

# ⭐️ Write a program that reads words.txt and prints only the words with more than 20 characters (not counting whitespace)
def print_over_20(word):
    if len(word) > 20:
        print(word)
    

#print_over_20(fin)


# ⭐️ Write a function called has_no_e that returns True if the given word doesn’t have the letter “e” in it.
def has_no_e(word):
    e = word.find('e')
    if e == -1:
        print(word)
        return True

#has_no_e('word')

# ⭐️ Write a program that reads words.txt and prints only the words that have no “e”. 
def no_e(txt):
    counter = 0
    total = 0
    for line in txt:
        total += 1
        e = line.find('e')
        if e == -1:
            word = line.strip()
            counter += 1
            print(word)
    percentage = int(counter / total * 100)
    # Compute the percentage of words in the list that have no “e”.
    print(f'{percentage}% of words in the list dont have the letter "e".')

# print('printing no e')
# no_e(fin)

# ⭐️ Write a function named avoids that takes a word and a string of forbidden letters

def avoids(word,string):
    for letter in string:
        if letter in word:
            return False
    print(word)
    return True   

# avoids('happy','bvf')




# Write a function named uses_only that takes a word and a string of letters, and that returns True if the word contains only letters in the list.

def uses_only(word,uses):
    for letter in word:
        if letter not in uses:
            return False
    print(word)
    return True


# Write a function named uses_all that takes a word and a string of required letters, and that returns True if the word uses all the required letters at least once.

def uses_all(word,all):
    for letter in all:
        if letter not in word:
            return False
    print(word)
    return True


# Write a function called is_abecedarian that returns True if the letters in a word appear in alphabetical order (double letters are ok)

def is_abecedarian(word):
    sort = ''.join(sorted(word))
    if word == sort:
        print(word)

# is_abecedarian('aabcd')


def print_all(txt):
    # Modify your program to prompt the user to enter a string of forbidden letters 
    
    print('enter a string')
    string = input() 
    for line in txt:
        word = line.strip()
        # print_over_20(word)
        # has_no_e(word)
        avoids(word,string)
        # uses_only(word,'acefhlo')
        # uses_all(word,'aeiouy')
        # is_abecedarian(word)
        

print_all(fin)



