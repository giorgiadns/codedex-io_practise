# USER INPUT
#-----------------------------------------------

# Python uses the input() function to get user input

#-----------------------------------------------
# PRACTISE
# Create a program that asks the user for two numbers,
# and then calculates the hypotenuse.

#-----------------------------------------------

print('---HYPOTHENUSE CALCULATOR---')

# ASK THE USER TO INSERT THE CATHETES 
a = float(input('Enter the lenght of the first cathetus in centimetres: '))
b = float(input('Enter the lenght of the second cathetus in centimetres: '))

# CALCULATE THE HYPOTHENUSE
c = (a**2 + b**2)**0.5

# PRINT THE RESULT
print('The hypothenuse is ', c, ' centimetres long' )
