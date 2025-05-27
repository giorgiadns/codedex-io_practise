# STRING INTERPOLATION

# String interpolation is a process of substituting 
# values of variables into placeholders in a string.
#-----------------------------------------------
# PRACTISE

# Create a program and use a for loop and a range() 
# function to print out all the verses of 
# "99 Bottles of Beer."
#-----------------------------------------------

for i in range(99, 0, -1):
  print(f"{i} bottles od beer on the wall")
  print(f"{i} bottles od beer")
  print("Take one down, pass it around")
  print(f"{i - 1} bottles of beer on the wall")
