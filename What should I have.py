import random
import time
def answer (answernumber):
    if answernumber == 1:
        return 'Banana'
    elif answernumber == 2:
        return 'Peaches and cream'
    elif answernumber == 3:
        return 'chocolate'
    elif answernumber == 4:
        return 'Vanilla'
    elif answernumber == 5:
        return 'Strawberry'

r = random.randint(1,5)
fortune = answer(r)
print('Oh magical and all mighty PyRoe')
print('What should I consume for sustenance today?')
print(fortune)
time.sleep(5)
