print('Integer error catching test. Non integers should throw an error prompt, valid integers will print the input')
try:
    name = input()
    print(int(name))
except ValueError:
    print('Error, numbers only please')
