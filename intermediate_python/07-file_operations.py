# FILE OPERATIONS

# THE 'TRY-FINALLY' STATEMENT
# The try-finally statement is made up of two blocks:
# - the try block with the code that we attempt to run;
# - the finally block that always closes the file to finish
# the statement.

# FILE CURSOR 
# The file cursor is necessary for reading or modifying
# specific parts of the file. Methods like seek() move
# the cursor to a desired location within the file:
#  with open('example.txt','r') as file:
#    file.seek(10) #Move to the 10th byte
#    content = file.read()
# The truncate method allows us to modify file size.
# This is useful when we want to remove or reset content
# beyond a certain point. 
#  with open('example.txt','a') as file:
#    file.truncare(20)  #limit file size to 20 bytes

#-----------------------------------------------

# PRACTISE

# Create a sent_message.txt file and write a secret 
# message to it. 
# Read the message ans use seek() to move the cursor
# to the beginning (0).
# Use truncate() to reset the ocntent to the lenght of
# the unsend message.
# Save the new message to the file and print it.
#-----------------------------------------------

sent_message = 'This is a secret message.'

# Save message to the file
with open('sent_message.txt','w') as file:
    file.write(sent_message)


# r+ indicates that both reading and writing are allowed
with open('sent_message.txt','r+') as file:

    #Read the sent message from the file
    original_message = file.read()

    #Move the cursor to the beginning of the file
    file.seek(0)

    unsent_message = 'This message has been unsent.'
 
    #Truncate the file to the lenght of the unsent_message
    file.truncate(len(unsent_message))

    file.write(unsent_message)

    print('Original message: ', sent_message)
    print('Unsent message: ', unsent_message)
