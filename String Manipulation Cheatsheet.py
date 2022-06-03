#Python string cheat sheet with examples


#Escape characters
"""
\' Single quote
\" Double qoute
\t Tab
\ Newline(line break)
\\ Backslash

Raw strings- place before beggining qoutation
>>> print(r'that is carol\'s cat.')
That is carol\'s cat.
"""


#Indexing and Slicing

"""
>>> spam = 'Hello world!'
>>> spam[0]
'H'
>>> spam[4]
'o'
>>> spam[-1]
'!'
>>> spam[0:5]
'Hello'
>>> spam[:5]
'Hello'
>>> spam[6:]
'world!'
"""


#The in and not Operators
"""
Will evaluate a string to a boolean value.
These expressions test whether the first string (the exact string, case sensitive) can be found within the second string.

>>> 'Hello' in 'Hello World'
True
>>> 'Hello' in 'Hello'
True
>>> 'HELLO' in 'Hello World'
False
>>> '' in 'spam'
True
>>> 'cats' not in 'cats and dogs'
False
"""

#The upper() lower() isupper() islower() methods
"""
The upper() and lower() string methods return a new string where all the letters in the original \n
string have been converted to uppercase or lower-case, respectively.
Nonletter characters in the string remain unchanged.
Note that these methods do not change the string itself but return new string values unless calling the function on a string

>>> spam = 'Hello world!'
>>> spam.upper()
'HELLO WORLD!'
>>> spam = spam.upper()
>>> spam
'HELLO WORLD!'
>>> spam = spam.lower()
>>> spam
'hello world!'

The isupper() and islower() string methods will return a boolean True value if the string has at least one letter \n
and all the letters are uppercase or lowercase, respectively. Otherwise, the method returns False.

>>> spam = 'Hello world!'
>>> spam.islower()
False
>>> spam.isupper()
False
>>> 'HELLO'.isupper()
True
>>> 'abc12345'.islower()
True
>>> '12345'.islower()
False
>>> '12345'.isupper()
False

Since the upper() and lower() string methods themselves return strings, \n
you can call string methods on those returned string values as well.
Expressions that do this will look like a chain of method calls.

>>> 'Hello'.upper()
'HELLO'
>>> 'Hello'.upper().lower()
'hello'
>>> 'Hello'.upper().lower().upper()
'HELLO'
>>> 'HELLO'.lower()
'hello'
>>> 'HELLO'.lower().islower()
True

"""

#The isX String Method

"""
isalpha() returns True if the string consists only of letters and is not blank.
isalnum() returns True if the string consists only of letters and numbers and is not blank.
isdecimal() returns True if the string consists only of numeric characters and is not blank.
isspace() returns True if the string consists only of spaces, tabs, and new-lines and is not blank.
istitle() returns True if the string consists only of words that begin with an uppercase letter followed by only lowercase letters.

>>> 'hello'.isalpha()
True
>>> 'hello123'.isalpha()
False
>>> 'hello123'.isalnum()
True
>>> 'hello'.isalnum()
True
>>> '123'.isdecimal()
True
>>> '    '.isspace()
True
>>> 'This Is Title Case'.istitle()
True
>>> 'This Is Title Case 123'.istitle()
True
>>> 'This Is not Title Case'.istitle()
False
>>> 'This Is NOT Title Case Either'.istitle()
False

"""

####Basic input validations with isX example

while True:
    print('Enter your age:')
    age = input()
    if age.isdecimal():
        break
    print('Please enter a number for your age.')

while True:
    print('Select a new password (letters and numbers only):')
    password = input()
    if password.isalnum():
        break
    print('Passwords can only have letters and numbers.')


#The startswith() and endswith() methods
"""
The startswith() and endswith() methods return True if the string value they are called on begins or ends (respectively) \n
with the string passed to the method, otherwise, they return False.

>>> 'Hello world!'.startswith('Hello')
True
>>> 'Hello world!'.endswith('world!')
True
>>> 'abc123'.startswith('abcdef')
False
>>> 'abc123'.endswith('12')
False
>>> 'Hello world!'.startswith('Hello world!')
True
>>> 'Hello world!'.endswith('Hello world!')
True

"""

#The join() and split() methods
"""
The join() method is useful when you have a list of strings that need to be joined together into a single string value.
The join() method is called on a string, gets passed a list of strings, and returns a string.
The returned string is the concatenation of each string in the passed-in list.

>>> ', '.join(['cats', 'rats', 'bats'])
'cats, rats, bats'
>>> ' '.join(['My', 'name', 'is', 'Simon'])
'My name is Simon'
>>> 'ABC'.join(['My', 'name', 'is', 'Simon'])
'MyABCnameABCisABCSimon'

Remember that join() is called on a string value and is passed a list value.
The split() method does the opposite: It’s called on a string value and returns a list of strings.

>>> 'My name is Simon'.split()
['My', 'name', 'is', 'Simon']
>>> 'MyABCnameABCisABCSimon'.split('ABC')
['My', 'name', 'is', 'Simon']
>>> 'My name is Simon'.split('m')
['My na', 'e is Si', 'on']

###using split() with \n argument example

>>> spam = '''Dear Alice,
How have you been? I am fine.
There is a container in the fridge
that is labeled "Milk Experiment".

Please do not drink it.
Sincerely,
Bob'''

>>> spam.split('\n')
['Dear Alice,', 'How have you been? I am fine.', 'There is a container in the
fridge', 'that is labeled "Milk Experiment".', '', 'Please do not drink it.',
'Sincerely,', 'Bob']

"""

#Justifiying text with rjust() ljust() and center()
"""
The rjust() and ljust() string methods return a padded version of the string they are called on, with spaces inserted to justify the text.
The first argument to both methods is an integer length for the justified string.

>>> 'Hello'.rjust(10)
'     Hello'
>>> 'Hello'.rjust(20)
'               Hello'
>>> 'Hello World'.rjust(20)
'         Hello World'
>>> 'Hello'.ljust(10)
'Hello     '

An optional second argument to rjust() and ljust() will specify a fill character other than a space character.

>>> 'Hello'.rjust(20, '*')
'***************Hello'
>>> 'Hello'.ljust(20, '-')
'Hello---------------'

The center() string method works like ljust() and rjust() but centers the text rather than justifying it to the left or right.

>>> 'Hello'.center(20)
'       Hello       '
>>> 'Hello'.center(20, '=')
'=======Hello========'

"""

###Print tabular data with correct spacing example

def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))
picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)

#Removing Whitespace with strip(), rstrip(), and lstrip()
"""
The strip() string method will return a new string without any whitespace characters at the beginning or end.
The lstrip() and rstrip() methods will remove whitespace characters from the left and right ends, respectively.


>>> spam = '    Hello World     '
>>> spam.strip()
'Hello World'
>>> spam.lstrip()
'Hello World '
>>> spam.rstrip()
'    Hello World'
>>> spam = 'SpamSpamBaconSpamEggsSpamSpam'
>>> spam.strip('ampS')
'BaconSpamEggs' #notice it strips the ampS characters from only the ends of the string

