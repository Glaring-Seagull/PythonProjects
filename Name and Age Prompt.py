# This program says hello and ask for a name and age, then tell you how old you will be next year.
import time

print('Hello!')
print('What is your name?') # print that ask for name
myName = input() #waits for input to assign to 'myName' value
print('It\'s good to meet you, ' + myName) #print response with name input
print('The length of your name is:')
print(len(myName)) # evaluate and print the numerical length of name given
print('What is your age?')  # for age
myAge = input() #wait for input to assign to value 'myAge'
print('You will be ' + str (int(myAge) + 1) + ' in a year.') # prints the age you will be in 1 year, uses intiger ('myAge' + 1) within string
print('It was nice meeting you ' + myName + '! Closing program in a sec!')
time.sleep(5) #wait 5 seconds before closing, uses time import
