# WHILE LOOP

# A while loop looks very similar to an if statement.
# Just like an if statement, it executes the code if 
# the condition is True.
# However, the difference is that the while loop will
# continue to execute the code inside of it, over and
# over again, as long as the condition is True.
#-----------------------------------------------

# PRACTISE

# Create a guess game with a limit to th number of
# tries
#-----------------------------------------------

guess = 0
tries = 0 

while guess !=6 and tries<6:
  
  guess = int(input("Guess the number: "))
  tries += 1

  if guess != 6:
    print("NOPE! Anyway, you have", 6 - tries, " more tries")

  if guess == 6: 
    print("You got it!")
    break
