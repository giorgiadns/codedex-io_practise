# LOGICAL OPERATORS

# Also known as boolean operators, logical operators
# combine and evaluate two conditions. 
# There are 3 operators:
# - 'and' returns 'True' if both conditions are true, it returns 'False' otherwise;
# - 'or' returns 'True' if at least one of the conditions is 'True', and 'False' otherwise;
# - 'not' returns 'True' if the condition is false, and vice versa.
#-----------------------------------------------

# PRACTISE 

# Create a program that asks the user their height and
# how many credits they have. 
# Use a combination of relational and logical operators to create the rules:
# If they are tall enough and have enough credits, print "Enjoy the ride!"
# Else if they have enough credits, but they aren't tall enough, print "You are not tall enough to ride."
# Else if they are tall enough, but they don't have enough credits, print "You don't have enough credits."
# Else, print a message saying they have not met either requirement.

#-----------------------------------------------

# ASK THE USER TO ENTER THEIR HEIGHT AND CREDITS
h = int(input('Height in cm: '))
c = int(input('Credits: '))

# CHECK THE VALUES AND PRINT THE RESPONSE
if (h>=137) and (c>=10):
  print('Enjoy the ride!')
elif (h>=137) and (c<10):
  print("Sorry, you don't have enough credits.")
elif (h<137) and (c>=10):
  print("You are not tall enough.")
elif (h<137) and (c<10):
  print("You don't have enought credits and you're not tall enough.")
