# RECAP SECOND PART
#-----------------------------------------------

# We have seen:
# - if statement;
# - elif clause ;
# - relational operators;
# - logical operators.

#-----------------------------------------------
# PRACTISE
# Write a program that asks the user some questions:

# Q1) Do you like Dawn or Dusk?
#     1) Dawn
#     2) Dusk
# If answer is equal to 1, Gryffindor and Ravenclaw both get a +1.
# Else if answer is equal to 2, Hufflepuff and Slytherin both get a +1.
# Else, output the message "Wrong input."

# Q2) When I’m dead, I want people to remember me as:
#    1) The Good
#    2) The Great
#    3) The Wise
#    4) The Bold
# If the answer is 1, Hufflepuff +2.
# Else if answer is 2, Slytherin +2.
# Else if answer is 3, Ravenclaw +2.
# Else if answer is 4, Gryffindor +2.
# Else, output the message "Wrong input."

# Q3) Which kind of instrument most pleases your ear?
#    1) The violin
#    2) The trumpet
#    3) The piano
#    4) The drum
# If the answer is 1, Slytherin +4.
# Else if the answer is 2, Hufflepuff +4.
# Else if the answer is 3, Ravenclaw +4.
# Else if the answer is 4, Gryffindor +4.
# Else, output "Wrong input."
# Lastly, print out the score for each house.
#-----------------------------------------------

Gryffindor=0
Hufflepuff=0
Ravenclaw=0
Slytherin=0

print('---THE SORTING HAT---')
print('---------------------')

# FIRST QUESTION
print("Q1) Do you like Dawn or Dusk?")
print("1) Dawn")
print("2) Dusk")

a1=int(input("Answer: "))

if a1 == 1:
  Gryffindor += 1
  Ravenclaw += 1
elif a1 == 2:
  Slytherin += 1
  Hufflepuff += 1
else:
    print("Wrong input")

# SECOND QUESTION  
print('---------------------')
print("Q2) When I'm dead, I want people to remenber me as: ")
print("1) The good")
print("2) The great")
print("3) The wise")
print("4) The bold")

a2=int(input("Answer: "))

if a2 == 1:
  Hufflepuff += 4
elif a2 == 2:
  Slytherin += 4
elif a2 == 3:
  Ravenclaw += 4
elif a2 == 4:
  Gryffindor += 4
else:
  print("Wrong input")

# THIRD QUESTION
print('---------------------')
print("Q3) Which kind of instrument most pleases your ear?")
print("1) The violin")
print("2) The trumpet")
print("3) The piano")
print("2) The drum")

a3=int(input("Answer: "))

if a3 == 1:
  Slytherin += 4
elif a3 == 2:
  Hufflepuff += 1
elif a3 == 3:
  Ravenclaw += 1
elif a3 == 4:
  Gryffindor += 1
else:
    print("Wrong input")

# PRINT THE SCORES
print('---------------------')
print("END OF THE QUIZ, LET'S SEE YOUR SCORES...")
print("Gryffindor:", Gryffindor, " points")
print("Hufflepuff:", Hufflepuff, " points")
print("Ravenclaw:", Ravenclaw, " points")
print("Slytherin:", Slytherin, " points")
print('---------------------')

# CHECK THE MAX VALUE
winner = max(Gryffindor, Slytherin, Hufflepuff, Slytherin)

if Gryffindor == winner:
  print('Congrats, you are a Griffindor!')
elif Slytherin == winner:
  print('Congrats, you are a Slytherin!')
elif Hufflepuff == winner:
  print('Congrats, you are a Hufflepuff!') 
else:
  print('Congrats, you are a Ravenclaw!')
