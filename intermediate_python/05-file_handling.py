# FILE HANDLING

# We can use Python to work with other files.
# File handling lets us interact with external 
# files for various purposes, including:
# - saving information to a file by writing to it;
# - reading from a file to use its information;
# - maintaining your computer's file system
# 
# The open() method can create a file or open
# an already existing file.
# The write() method writes on the specified file.
#-----------------------------------------------

# PRACTISE

# Use the open() method to create a new diaries.txt
# file, fill it with whatever you like, each entry
# should be separated by a new line
#-----------------------------------------------

diary = open('diary.txt', 'w')
diary.write('Hello! This is my first time trying to use file handling methods in python.\n')
diary.write('I hope to learn more!')
