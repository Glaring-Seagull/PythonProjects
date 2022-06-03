#setdefault() method, ensures a key exist and makes one if it does not
#pprint or pretty print module, for when you want a cleaner display of the items in a dictionary than what print() provides

import pprint

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
print(message)
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count)
