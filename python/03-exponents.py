# EXPONENTS
#-----------------------------------------------

# Python can also perform exponentiation.
# Since exponentiation is super similar to multiplication, Python uses the notation **.

#-----------------------------------------------
# PRACTISE
# Create a program that calculates BMI.

#-----------------------------------------------


print('---BMI CALCULATOR---')

# ASK THE USER TO INSERT THE HEIGHT
height = float(input('Please insert you height in meters: '))

# ASK THE USER TO INSERT THE MASS
mass = float(input('Please insert you mass in kilograms: '))

# CALCULATE THE BMI
bmi = (mass)/((height) ** 2)

# PRINT THE RESULT
print('Your BMI is: ', bmi)
