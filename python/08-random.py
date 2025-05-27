# RANDOM

# In Python, modules are .py files containing
# code that can be imported inside another Python
# program. 
# We can use the .randint() function from a module
# called random to generate a random number from a 
# range.

#-----------------------------------------------
# PRACTISE

# Create a program that can respond to any
# yes or no question each time it executes.
#-----------------------------------------------

#IMPORT THE 'RANDOM' MODULE
import random

#ASK THE USER TO ENTER A QUESTION
question = input('Enter your question: ')

#GENERATE A RANDOM INTEGER NUMBER BETWEEN 1 AND 9
num = random.randint(1,9)

#BASED ON THE RANDOM NUMBER, PRINT AN ANSWER
if num == 1:
  print("Yes - definitely.")
elif num == 2:
  print("It is decidedly so.")
elif num == 3:
  print("Without a doubt.")
elif num == 4:
  print("Reply hazy, try again.")
elif num == 5:
 print("Ask again later.")
elif num == 6:
  print("Better not tell you now.")
elif num == 7:
  print("My sources say no.")
elif num == 8:
  print("Outlook not so good.")
elif num == 9:
  print("Very doubtful.")
