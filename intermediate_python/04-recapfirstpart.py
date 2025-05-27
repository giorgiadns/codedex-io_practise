# RECAP

# In this chapter, we learned the following:
# - Tuples are ordered, immutable sequences.
# - Dictionaries are unordered sequences of key-value pairs.
# - Sets are unordered lists of unique items.
#-----------------------------------------------

# PRACTISE
# Create a list of dictionaries where each dictionary represents 
# a player. Include attributes such as 'name,' 
# 'position,' and 'jersey number.'
# Print out a list of all player positions in the dataset.

#-----------------------------------------------

# LIST OF PLAYERS
players = [
    {'name' : 'Patrick Mahomes', 'position' : 'Quarterback', 'jersey_number' : '1', 'touchdowns' : 3},
    {'name' : 'Travis Kelce', 'position' : 'Tight end', 'jersey_number' : '2', 'touchdowns': 2},
    {'name' : 'Xavier Worthy', 'position' : 'Receiver', 'jersey_number' : '3', 'touchdowns': 1},
    {'name' : 'Isiah Pacheco', 'position' : 'Running back', 'jersey_number' : '4', 'touchdowns': 3}
]

#PRINT NAMES
names = [player['name'] for player in players]
print('\nPlayers names: ', names)

#PRINT POSITIONS
positions = [player['position'] for player in players]
print('\nPlayer positions: ', positions)

#UPDATE DATA
players[1]['jersey_number'] = 12
print("\nName: ", players[1]['name'])
print("\nUpdated number: ", players[1]['jersey_number'])

# AVERAGE STATS
average_touchdowns = sum(player['touchdowns'] for player in players) / len(players)
print("\nAverage Touchdowns: ", average_touchdowns)
