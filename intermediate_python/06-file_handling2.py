# FILE HANDLING 2

# OPENING FILES

# When handling a file, you have to open it first.
# In python, we use the open() function:
# file = open(file_path, mode)
# this methos returns a file object.
# There are 3 modes you can open a file with:
# - 'r' for reading
# - 'w' for writing
# - 'a' for writing from the end of a file
# [BE CAREFUL WITH 'w' MODE, IT OVERWRITES ANY CONTENT]

# WRITING TO FILES
# The write() method wirtes data to a file:
# file.write('text')
# To write on multiple lines, this method must be
# used multiple times with the \n (newline) character
# You can also write multiple lines to a file
# using the writelines() method:
#  lines = ['This is the first line\n', 'This is the second line\n']
#  file.writelines(lines)

# READING FILES
# The read() method lets you read the entire content
# of a file. This method can be saved to a variable 
# to the terminal:
#  file = open('filename.txt')
#  content = file.read()
#  print(content)
# The readline() method lets you read a file one line
# at a time:
#  line1 = file.readline()
#  print(line1, end='')
#  line2= file.readLine()
#  print(line2, end='')
# To print each line on a single line withoud adding \n
#  at the end, we use the end='' option in the print
# function (by deafault, it ends with \n).

# CLOSING FILES 
# The close() method is used to finish working with 
# a file and free up resources:
#  file.open('filename.txt')
#  file.close()
# Always call .close() after reading or writing to 
# the file to ensure everything is saved.
# You can also use a 'with' block to open a file,
# handle it, and close it automatically:
#  with open('filename', 'r') as f
#-----------------------------------------------

# PRACTISE
# Define a dictionary to store songs, write the
# songs to a file.
#-----------------------------------------------

# Define the dictionary
songs = {
    'MAURI':'Salmo',
    'Safe and sound':'Capital Cities',
    'Fantasy':'JADE',
    'Renaissance':'Eminem',
    'You Go Your Way':'Perrie',
    'Una Chiave':'Caparezza',
    'Forbidden Fruit':'Leigh-Anne'
    
}

# Function to write the songs to a file
def write_songs_to_file(songs, file_name):

    with open(file_name, 'w') as file:

        file.write('Liked songs:\n')
        for title, artist in songs.items():
            file.write(f' {title} by {artist}\n')


write_songs_to_file(songs, "likedsongs.txt")
