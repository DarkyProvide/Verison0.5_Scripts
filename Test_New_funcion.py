import random as rad
# int()
# str()
# masiv[a, b, c, d, ... 1, 2, 3, 4, ... !, @, #, $, %, ..]

ListNumbers = [3, 1, 2, 3, 4, 5, 6, 7, 8, 9]
ListNumbers.sort()

def podbor(number):

    zero = 0

    while zero != number:

        ListNumbers.append(max(list(ListNumbers)) + 1)

        zero += 1

while True:

    a = input('~>')

    if a:

        # split input
        command = list(a.split())

        # commands
        if command[0] == 'start':

            if command[1] == 'num':

                if command[2]:

                    theRashNumber = int(command[2])
                    podbor(theRashNumber)


                else:
                    print('print your number')

            #elif ...

            else:
                print('num')

        elif command[0] == 'progress':
            print(ListNumbers)

        elif command[0] == 'exit':
            quit()

        else:
            print('print start > num > !>NUMBER<!')
