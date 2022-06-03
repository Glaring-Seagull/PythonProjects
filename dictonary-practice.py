#An example of how dictionaries work


#This line creates a dictionary for the variable myCat. Note that the curly cracket {} indicates a dictionary.
myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
#The keys are size, color, and disposition, the values for the keys are fat, gray, and loud.


#This line will print the value for the key size, which is fat.
print(myCat['size'])

#This line will print my cat has gray fur, because the key for the value color is gray
print('My cat has ' + myCat['color'] + ' fur.')

#More examples of printing the key's values
print('My cat is a ' + myCat['disposition'] + ', ' + myCat['size'] + ', ' + myCat['color'] + ', asshole')
