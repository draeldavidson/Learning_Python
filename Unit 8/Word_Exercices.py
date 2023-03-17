# solving word puzzles by searching for words that have certain properties.

fin = open('Unit 8/words.txt')

def print_all(fin):
    for line in fin:
        word = line.strip()
        print(word)

# Write a program that reads words.txt and prints only the words with more than 20 characters (not counting whitespace)
def print_over_20(txt):
    for line in txt:
        if len(line) > 20:
            word = line.strip()
            print(word)

print_over_20(fin)


# Write a function called has_no_e that returns True if the given word doesn’t have the letter “e” in it.
def has_no_e(word):
    e = word.find('e')
    if e == -1:
        return True



has_no_e('word')
