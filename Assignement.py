'''ASSIGNEMENT: Guess a number bertween 1 and 10'''

import random

def rFunction():

    #print('\n')
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

'''
SELECT
	column_1
    , column_2
    , column_3
    , email
from data_table
left join email_table on data_table.join_id = email_table.join_id
WHERE
	column_1 % 2 = 0
    and column_2 < column_1
    and column_3 like '%1'

'''
