# ⭐️ GLOSSARY ⭐️

# persistent: Pertaining to a program that runs indefinitely and keeps at least some of its data in permanent storage.
# format operator: An operator, %, that takes a format string and a tuple and generates a string that includes the elements of the tuple formatted as specified by the format string.
    # '%d' to format an integer, 
    # '%g' to format a floating-point number, 
    # '%s' to format a string

# format string: A string, used with the format operator, that contains format sequences.
# format sequence: A sequence of characters in a format string, like %d, that specifies how a value should be formatted.
camels = 42
print('I have spotted %d camels.' % camels)

# text file: A sequence of characters stored in permanent storage like a hard drive.
    # .txt
# directory: A named collection of files, also called a folder.
    # the directory is this file is in is 'Unit 8/'
# path: A string that identifies a file.
    # the path of this file is 'Files'
# relative path: A path that starts from the current directory.
    # the relative path of this file is 'Unit 8/Files.py'
# absolute path: A path that starts from the topmost directory in the file system.

# catch: To prevent an exception from terminating a program using the try and except statements.
try:
    fin = open('bad_file')
except:
    print('Something went wrong.')
# database: A file whose contents are organized like a dictionary with keys that correspond to values.
# bytes object: An object similar to a string.
# shell: A program that allows users to type commands and then executes them by starting other programs.
# pipe object: An object that represents a 


# ⭐️ EXERCICES ⭐️

# fout = open('Unit 8/output.txt', 'w')
# line1 = "This here's the wattle,\n"
# fout.write(line1)

camels = 42
print('I have spotted %d camels.' % camels)


# Exercise 14.1. Write a function called sed that takes as arguments a pattern string, a replacement string, and two filenames; it should read the first file and write the contents into the second file (creating it if necessary). If the pattern string appears anywhere in the file, it should be replaced with the replacement string. 

# If an error occurs while opening, reading, writing or closing files, your program should catch the exception, print an error message, and exit. Solution: http: // thinkpython2. com/ code/ sed.
# py .
# Exercise 14.2. If you download my solution to Exercise 12.2 from http: // thinkpython2. com/
# code/ anagram_ sets. py , you’ll see that it creates a dictionary that maps from a sorted string of
# letters to the list of words that can be spelled with those letters. For example, 'opst' maps to the
# list ['opts', 'post', 'pots', 'spot', 'stop', 'tops'].
# Write a module that imports anagram_sets and provides two new functions: store_anagrams
# should store the anagram dictionary in a “shelf”; read_anagrams should look up a word and return
# a list of its anagrams. Solution: http: // thinkpython2. com/ code/ anagram_ db. py .

# Exercise 14.3. In a large collection of MP3 files, there may be more than one copy of the same song,
# stored in different directories or with different file names. The goal of this exercise is to search for
# duplicates.

# 1. Write a program that searches a directory and all of its subdirectories, recursively, and returns
# a list of complete paths for all files with a given suffix (like .mp3). Hint: os.path provides
# several useful functions for manipulating file and path names.
# 2. To recognize duplicates, you can use md5sum to compute a “checksum” for each files. If two
# files have the same checksum, they probably have the same contents.
# 3. To double-check, you can use the Unix command diff.
