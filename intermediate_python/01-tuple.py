# STRING INTERPOLATION

# Tuples are ordered collections that cannot be 
# changed once created. 
#-----------------------------------------------
# PRACTISE

# Create 3 tuples for your friends, each with the 
# latitude and longitude of the cities they live in.
# Print the locations of all your friends.
# Which of your friends is the furthest away?
#-----------------------------------------------

# TUPLES
city1 = ('Rome', '41.902782', '12.496365')
city2 = ('London', '51.507351', '-0.127758')
city3 = ('Sydney', '-33.868820', '151.209290')

# COMBINING THE TUPLES
allcities= city1 + city2 + city3

# PRINT (NOTICE THE DIFFERENCES)
print(city1[0])
print(city2[0])
print(city3[0])
print(allcities)
