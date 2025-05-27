# RELATIONAL OPERATORS

# A lot of the times inside conditions, 
# we are comparing two values.
# To do so, we need to use a different type 
# of operators called relational operators that 
# compares values:
# == equal to
# != not equal
# > greater than
# < less than 
# >= greater than or equal to
# <= less than or equal to

# ELIF

# One or more elif statements (short for "else if") 
# can be optionally added in between the if and else 
# to provide additional condition(s) to check. 
# Sometimes two is simply not enough.


#-----------------------------------------------

# PRACTISE

# Create a program that checks whether 
# a pH level is basic, acidic, or neutral.
#-----------------------------------------------

#ASK THE USER TO ENTER THE PH VALUE
ph=int(input('Enter a pH level between 0 and 14: '))

# CHECK THE VALUE
if ph>7:
  print('Basic')
elif ph<7:
  print('Acidic')
else:
  print('Neutral')
