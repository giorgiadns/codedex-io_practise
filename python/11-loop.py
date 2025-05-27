# LOOP

# In programming, a loop is used to repeat a block 
# of code until a specified condition is satisfied. 
# The first kind of loop that we are going to learn 
# is the while loop. 

#-----------------------------------------------

# PRACTISE

# Create a program that checks the PIN for an ATM.
# The correct code is 1234.
#-----------------------------------------------

print(' _____________________')
print('|                     |')
print('| ------------------- |')
print('| | BANK OF CODEDEX | |')
print('| ------------------- |')
print('|_____________________|')

pin=int(input('Enter your PIN: '))

while pin != 1234:
  pin = int(input('Incorrect PIN. Enter your PIN again: '))

if pin == 1234:
  print('PIN ACCEPTED!')
