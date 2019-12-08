import random as rad
# int()
# str()

alPhaBet = []

ListNumbers = [0]

listIIWorkWithNumbers = []

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

# Operators doing  --  remark infinity while!
def givWithOperatorsDo():

    azartRandom = 1

    nummy = rad.randint(1, 10000)

    if nummy >= 9000:

        azartRandom -= nummy * 0.001

    elif nummy <= 1000:

        azartRandom -= nummy * 0.00001

    elif nummy >= 1000 and nummy <= 9000:

        azartRandom -= nummy * 0.0001

    else:

        azartRandom -= nummy * 0.0000001

    if azartRandom >= 0.5:  # nums

        i = 0

        print(len(list(ListNumbers)))

        while i != len(list(ListNumbers)):

            a = ListNumbers[i]

            if i < len(list(ListNumbers)):

                b = ListNumbers[(i + 1)]

            else:

                b = 0

            randa = rad.randint(0, 3)

            # +, -, *, /
            if randa == 0:

                listIIWorkWithNumbers.append((a, '+', b, '=', (a + b)))

            elif randa == 1:

                listIIWorkWithNumbers.append((a, '-', b, '=', (a - b)))

            elif randa == 2:

                listIIWorkWithNumbers.append((a, '*', b, '=', (a * b)))

            else:

                try:

                    listIIWorkWithNumbers.append((a, '/', b, '=', (a / b)))

                except ZeroDivisionError:

                    listIIWorkWithNumbers.append((a, '/ 1 =', (a / 1)))

        listIIWorkWithNumbers.sort()

        i += 1

    else:

        pass  # text


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

        elif command[0] == 'exit':

            print('End and Delete all data')
            quit()

        else:
            print('print start >> alphabet | num | runIntStr >> !>NUMBER<! | !>TEXT<!')
