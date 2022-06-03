import time
def one():
   print('You\'re name, plus four, is ' + str(len(name) + 4) + ' characters long.')

def two():
    print('Hello ' + name)

def three():
    print(name + '. You\'ve selected three, how odd.')
    while True:
        print('Are you sure about that?')
        confirm = input()
        if confirm == 'yes':
            print('If you say so...')
            break
        elif confirm == 'no':
            print('Then why\'d you\'d pick it?')
            time.sleep(1)
            print('Reopen the program and try again. Exiting...')
            time.sleep(2)
            break
        elif confirm != 'yes' or 'no':
            print('That doesn\'t answer my question...')
            time.sleep(1)
            continue
            
        


print('What is your name?')

name = input()

print('Please type one two or three')
while True:
    x = input()
    if x == 'one':
        one()
        break
    elif x == 'two':
        two()
        break
    elif x == 'three':
        three()
        break
    elif x != 'one' or 'two' or 'three':
        print('Invalid entry. Try again. one, two, or three')
