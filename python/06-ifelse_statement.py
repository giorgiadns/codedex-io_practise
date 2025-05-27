# CONTROL FLOW

# So far, every Python program we've encountered 
# has only had one path of execution — they all 
# execute one line at a time, from top to bottom. 
# Every time you run them, it gives you the same 
# result. Sometimes, we want our program to do 
# different things based on different conditions.
#-----------------------------------------------

# PRACTISE

# Create a coin flip program. 
#-----------------------------------------------

import random

# PICKS A RANDOM NUMBER BETWEEN 0 AND 1
num = random.randint(0,1)

# THE IF/ELSE STATEMENT CHECKS THE NUMBER
if (num>0.5):
    print('Heads')
else:
    print('Tails')
