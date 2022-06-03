import random
def answer (answernumber):
    if answernumber == 1:
        return 'Banana'
    elif answernumber == 2:
        return 'Peaches and cream'
    elif answernumber == 3:
        return 'Chocolate'
    elif answernumber == 4:
        return 'Vanilla'
    elif answernumber == 5:
        return 'Strawberry'
while True:
    ran = random.randint(1,5)
    fortune = answer(ran)
    print('Oh magical and all mighty PyRoe')
    print('What should I consume for sustenance today?')
    print(fortune)
    check = input ("Press 'z' to do another fortune or press any other key to quit.")
    if check.lower() == "z": #loop back to start
        continue
    print("Enjoy your food!")
    break