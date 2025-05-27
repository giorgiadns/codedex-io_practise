# FIZZBUZZ

# Create a fizz_buzz.py program that outputs 
# numbers from 1 to 100.
# Here's the catch:
# For multiples of 3, print "Fizz" instead of the number.
# For multiples of 5, print "Buzz" instead of the number.
# For multiples of 3 and 5, print "FizzBuzz".
#-----------------------------------------------

for i in range (100):
  
  # MULTIPLES OF 3 AND 5
  if i%3==0 and i%5==0:
    print("FizzBuzz")

  # MULTIPLES OF 3
  elif i%3==0:
    print("Fizz")

  # MULTIPLES OF 5
  elif i%5==0:
    print("Buzz")

  # ANYTHING ELSE
  else:
    print(i)
