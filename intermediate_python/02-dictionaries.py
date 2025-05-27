# DICTIONARIES

# Dictionaries are unordered collections that
# allow you to store and access data with
# key:value pairs
#-----------------------------------------------
# PRACTISE

# Create a dictionary with the information of
# your favorite artifact from the Met Museum,
# including:
# - artist
# - period
# - title
#-----------------------------------------------

artifact = {
    'artist':'Gustave Coubert',
    'period': '1851-52',
    'title':'Young Ladies of the Village'
}

print('\n---A WAY TO PRINT THE DICTIONARY---\n')
print('Artist: ', artifact['artist'])
print('Period: ', artifact['period'])
print('Title: ', artifact['title'])

print('\n---ANOTHER WAY TO PRINT THE DICTIONARY---\n')
print('Keys: ', artifact.keys())
print('Values: ', artifact.values())
print('Items: ', artifact.items())
