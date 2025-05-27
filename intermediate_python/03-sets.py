# SETS

# Sets are collections of unique items with no 
# duplicates.
# They are unordered collection of distinct elements.
# Each item in a set must be unique.
#-----------------------------------------------
# PRACTISE

# Create two sets representing your favorite fruits 
# and your best friend's favorite fruits.
# Print the union of the two sets would look like.
# Print the intersection of the two sets.
#-----------------------------------------------

# CREATE THE SETS
my_fruits = {'apple', 'cherrie', 'peach', 'strawberry'}
other_fruits = {'banana', 'kiwi', 'peach', 'apple'}

# SETS UNION
tuttifrutti = my_fruits.union(other_fruits)
print('\n----UNION----\n')
print(tuttifrutti)

# SETS INTERSECTION
somefruits = my_fruits.intersection(other_fruits)
print('\n----INTERSECTION----\n')
print(somefruits)


# SETS DIFFERENCE
difference = my_fruits.difference(other_fruits)
print('\n----DIFFERENCE----\n')
print(difference)
