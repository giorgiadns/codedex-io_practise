# RECAP FIRST PART
#-----------------------------------------------

# We have seen:
# - data types;
# - arithmetic operations;
# - the exponentiation;
# - the input() function.

#-----------------------------------------------
# PRACTISE
# We just got home from a fun trip to South America, 
# specifically Colombia, Peru, and Brazil. 
# Create a program that asks the user for the amount
# they have in pesos, soles and reais and calculates
# the total in USD
#-----------------------------------------------

# ASK THE USER TO ENTER THE LEFTOVER MONEY

pesos=int(input('Colombian pesos left: '))
soles=int(input('Peruvian soles left: '))
reais=int(input('Brazilian reais left: '))

# CONERT THE VALUES IN USD
pesos_to_dollars = pesos * 0.052
soles_to_dollars = soles * 0.27
reais_to_dollars = reais * 0.18

# CALCULATE THE TOTAL
dollars_left = pesos_to_dollars + soles_to_dollars + reais_to_dollars

# PRINT THE RESULT
print('We have ', dollars_left, ' dollars left')
