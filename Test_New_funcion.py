#import random as rad  --  For Maching II
# int()
# str()

alPhaBet = []

ListNumbers = [0]

# 1, 2, 3, 4, ... ====> (int)
def podbor(number):

    zero = 0
    lowSort = 0

    while lowSort != max(list(ListNumbers)):

        if lowSort not in ListNumbers:

            ListNumbers.append(lowSort)

        lowSort += 1

    ListNumbers.sort()

    while zero != number:

        ListNumbers.append(max(list(ListNumbers)) + 1)

        zero += 1

# a, b, c, d, ... !, @, #, $, %, ... ====> (str)
def speakAlphabet(speak):

    for i in speak:

        if i not in alPhaBet:

            try:

                if int(i) not in ListNumbers:
                    ListNumbers.append(int(i))
                    ListNumbers.sort()

            except ValueError or TypeError:

                alPhaBet.append(i)

while True:

    a = input('~>')

    if a:

        # split input
        command = list(a.split())

        # commands
        if command[0] == 'start':

            if command[1]:

                if command[1] == 'num':

                    if command[2]:

                        podbor(int(command[2]))

                    else:
                        print('print your number')

                elif command[1] == 'alphabet':

                    speak = input('Letter the text: ')
                    speakAlphabet(speak)

                else:
                    print('num')

            else:
                print('num | alphabet')

        elif command[0] == 'progress':

            print('ListNumbers:', ListNumbers)
            print('alPhaBet:', alPhaBet)

        elif command[0] == 'exit':

            print('End and Delete all data')
            quit()

        else:
            print('print start >> alphabet | num >> !>NUMBER<! | !>TEXT<!')
