print('how many cats do you have?')
numCats = input()
try:
    if int(numCats) >= 4:
        print('Thats a lot of cats.')
    else:
        print('thats a not that many cats')
except ValueError:
    print('You did not enter a number')
