'''ASSIGNEMENT: Guess a number bertween 1 and 10'''

import random

def rFunction():

    a = random.randrange(1, 9)
    b = random.randrange(1, 9)
    c = a * b

    print('A = ' + str(a))
    print('C = ' + str(c))

    if c == 4:
        print('Success!')
    else:
        rFunction()

rFunction()

