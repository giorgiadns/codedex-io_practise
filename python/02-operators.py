# OPERATORS
#-----------------------------------------------
# Python supports the following arithmetic operators:
# + Addition
# - Substraction
# * Multiplication
# / Division
# & Module (this operator returns the remainder)
#-----------------------------------------------
# PRACTISE

# Create a program that converts a number from 
# Fahrenheit to Celsius, then print out the converted
# temperature
#-----------------------------------------------

# ASKS THE USER TO INSERT THE INTEGER THAT REPRESENTS THE
# CURRENT TEMPERATURE IN FAHRENHEITS
current_temp_fahrenheit = int(input('Insert the current temperature in Fahrenheit: '))

# CONVERSION IN CELSIUS
current_temp_celsius = (current_temp_fahrenheit - 32) / 1.8

# PRINT THE RESULT
print('The equivalent temperature in Celsius is: ', current_temp_celsius)
