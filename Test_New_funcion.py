import random as rad
# int()
# str()

alPhaBet = []

ListNumbers = [0]

listIIWorkWithNumbers = []

listIIWorkWithAlphabet = []


#  do insort numbers (+, -, *, / on numbers) --> using in givWithOperatorsDo <--
def sortPodbProgramm():

    i = 0

    while i != (len(list(ListNumbers)) - 1):

        a = ListNumbers[i]

        b = ListNumbers[(i + 1)]

        randa = rad.randint(0, 3)

        # +, -, *, /
        if randa == 0 and ('+' + str(a + b)) not in list(listIIWorkWithNumbers):

            listIIWorkWithNumbers.append('+' + str(a + b))

            print(a + b)

        elif randa == 1 and ('-' + str(a - b)) not in list(listIIWorkWithNumbers):

            listIIWorkWithNumbers.append('-' + str(a - b))

            print(a - b)

        elif randa == 2 and ('*' + str(a * b)) not in list(listIIWorkWithNumbers):

            listIIWorkWithNumbers.append('*' + str(a * b))

            print(a * b)

        elif randa == 3:

            try:

                if ('/' + str(a / b)) not in list(listIIWorkWithNumbers):

                    listIIWorkWithNumbers.append('/' + str(a / b))

                    print(a / b)

            except ZeroDivisionError:

                if ('/' + str(a / 1)) not in list(listIIWorkWithNumbers):

                    listIIWorkWithNumbers.append('/' + str(a / 1))

                    print(a / 1)

        i += 1

#  big random
def bigRandom(azartRandom):
    nummy = rad.randint(1, 10000)

    if nummy >= 9000:

        azartRandom -= nummy * 0.001

    elif nummy <= 1000:

        azartRandom -= nummy * 0.00001

    elif nummy >= 1000 and nummy <= 9000:

        azartRandom -= nummy * 0.0001

    else:

        azartRandom -= nummy * 0.0000001

    return azartRandom

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

# Operators doing
def givWithOperatorsDo():

    azartRandomaizer = 1

    azartRandom = bigRandom(azartRandomaizer)

    if azartRandom >= 0.5:  # nums

        sortPodbProgramm()

    else:  # text alphabet program sort

        if alPhaBet:

            q = 0

            while q != len(list(alPhaBet)):

                i = 0

                while i != len(list(alPhaBet)):

                    First = list(alPhaBet)[q]
                    Second = list(alPhaBet)[i]

                    listIIWorkWithAlphabet.append(First + Second)

                    i += 1

                q += 1


while True:

    a = input('\n~>')

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

                elif command[1] == 'runIntStr':

                    givWithOperatorsDo()

                else:
                    print('num')

            else:
                print('num | alphabet')

        elif command[0] == 'progress':

            print('ListNumbers:', ListNumbers)
            print('alPhaBet:', alPhaBet)
            print('listIIWorkWithNumbers', listIIWorkWithNumbers)
            print('listIIWorkWithAlphabet', listIIWorkWithAlphabet)

        elif command[0] == 'exit':

            print('End and Delete all data')
            quit()

        else:
            print('print start >> alphabet | num | runIntStr >> !>NUMBER<! | !>TEXT<!')
