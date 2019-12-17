import random as rad

'''
Это первая часть - распределитель. В этой части вводятся слова,
а программа их обрабатывает на низком уровне (мелкая обработка
событий) - простое сложение букв из ввода пользователя и рандомные
математические вычисления над числами данные пользователем, и
составленным споском-помошником. Буквы составляются со всеми
возможными способами до максимума - 8 букв. 
'''

alPhaBet = []

ListNumbers = [0]

listIIWorkWithNumbers = []

listIIWorkWithAlphabet = []


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

# Operators doing (int and str)
def givWithOperatorsDo():

    azartRandom = bigRandom(1)

    #  nums
    if azartRandom >= 0.5:

        for i in range(len(list(ListNumbers)) - 1):

            a = ListNumbers[i]

            b = ListNumbers[(i + 1)]

            randa = rad.randint(0, 3)

            # +, -, *, /
            if randa == 0 and (a + b) not in list(listIIWorkWithNumbers):

                listIIWorkWithNumbers.append(a + b)

            elif randa == 1 and (a - b) not in list(listIIWorkWithNumbers):

                listIIWorkWithNumbers.append(a - b)

            elif randa == 2 and (a * b) not in list(listIIWorkWithNumbers):

                listIIWorkWithNumbers.append(a * b)

            elif randa == 3:

                try:

                    if (a / b) not in list(listIIWorkWithNumbers):
                        listIIWorkWithNumbers.append(a / b)

                except ZeroDivisionError:

                    if (a / 1) not in list(listIIWorkWithNumbers):
                        listIIWorkWithNumbers.append(a / 1)

    #  text
    else:

        if alPhaBet:

            q = 0

            progressesd = 0
            progsws = 0

            for q in range(len(list(alPhaBet))):

                ac = 0

                First = list(alPhaBet)[q]

                for ac in range(len(list(alPhaBet))):

                    e = 0

                    Second = list(alPhaBet)[ac]

                    #  2
                    if (First + Second) not in list(listIIWorkWithAlphabet):
                        listIIWorkWithAlphabet.append(First + Second)

                    for e in range(len(list(alPhaBet))):

                        d = 0

                        Third = list(alPhaBet)[e]

                        #  3
                        if (First + Second + Third) not in list(listIIWorkWithAlphabet):
                            listIIWorkWithAlphabet.append(First + Second + Third)

                        for d in range(len(list(alPhaBet))):

                            i = 0

                            Fourth = list(alPhaBet)[d]

                            #  4
                            if (First + Second + Third + Fourth) not in list(listIIWorkWithAlphabet):
                                listIIWorkWithAlphabet.append(First + Second + Third + Fourth)

                            for i in range(len(list(alPhaBet))):

                                Fifth = list(alPhaBet)[i]

                                #  5
                                if (First + Second + Third + Fourth + Fifth) not in list(listIIWorkWithAlphabet):
                                    listIIWorkWithAlphabet.append(First + Second + Third + Fourth + Fifth)

                                for tq in range(len(list(alPhaBet))):

                                    Sixth = list(alPhaBet)[tq]

                                    #  6
                                    if (First + Second + Third + Fourth + Fifth + Sixth) not in list(listIIWorkWithAlphabet):
                                        listIIWorkWithAlphabet.append(First + Second + Third + Fourth + Fifth + Sixth)

                                        for ts in range(len(list(alPhaBet))):

                                            Seventh = list(alPhaBet)[ts]

                                            #  7
                                            if (First + Second + Third + Fourth + Fifth + Sixth + Seventh) not in list(listIIWorkWithAlphabet):
                                                listIIWorkWithAlphabet.append(First + Second + Third + Fourth + Fifth + Sixth + Seventh)

                                                for td in range(len(list(alPhaBet))):

                                                    Eighth = list(alPhaBet)[td]

                                                    #  8
                                                    if (First + Second + Third + Fourth + Fifth + Sixth + Seventh + Eighth) not in list(listIIWorkWithAlphabet):
                                                        listIIWorkWithAlphabet.append(First + Second + Third + Fourth + Fifth + Sixth + Seventh + Eighth)

                                                    if progressesd == 10000:
                                                        progressesd = 0
                                                        progsws += 1
                                                        print('#')

                                                    progressesd += 1

while True:

    a = input('\n~>')

    if a:

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
                    print('num | alphabet | runIntStr')

            else:
                print('num | alphabet')

        elif command[0] == 'look':

            if command[1]:

                if command[1] in list(listIIWorkWithAlphabet):

                    print(command[1], 'in listIIWorkWithAlphabet')

            else:

                print('Text < 5 letters')

        elif command[0] == 'progress':

            print('ListNumbers:', ListNumbers)
            print('alPhaBet:', alPhaBet)
            print('listIIWorkWithNumbers', listIIWorkWithNumbers)
            print('listIIWorkWithAlphabet', listIIWorkWithAlphabet)

        elif command[0] == 'exit':

            print('End and Delete all data')
            quit()

        else:
            print('print :=> start | look | exit >> alphabet | num | runIntStr >> !>NUMBER<! | !>TEXT<!')