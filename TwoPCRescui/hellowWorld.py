import random as rad
import itertools as itt

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

saveNums = r'C:\GitProgects\Verison0.5_Scripts\TwoPCRescui\Pac\saveNums.txt'
saveAlphabet = r'C:\GitProgects\Verison0.5_Scripts\TwoPCRescui\Pac\saveAlphabet.txt'
workNums = r'C:\GitProgects\Verison0.5_Scripts\TwoPCRescui\Pac\workNums.txt'
workAlphabet = r'C:\GitProgects\Verison0.5_Scripts\TwoPCRescui\Pac\workAlphabet.txt'


#  saves progress in file
def _savesold(fileName, writeTextInFile):

    wrt = open(fileName, 'a')
    wrt.writelines(str(writeTextInFile))
        
    wrt.close()
    del wrt

#  chacked text in save_file
def _chack(fileName, text, save=True):
    
    rd = open(fileName, 'r')

    rad = list(rd.readlines())
    
    text = list(text)
    
    listC = []
    
    for i in range(len(rad)):
    
        for d in range(len(text)):
    
            if rad[i] not in text[d]:
                
                listC.append(text[d])
                
    if save == True:
        
        _savesold(fileName, listC)

#  big random
def _bigRandom(azartRandom):
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
def _podbor(number):

    zero = 0
    lowSort = 0

    while lowSort != max(list(ListNumbers)):

        if lowSort not in ListNumbers:

            ListNumbers.append(lowSort)

        lowSort += 1

    ListNumbers.sort()

    for zero in range(int(number)):

        ListNumbers.append(max(list(ListNumbers)) + 1)

        zero += 1
        
    _savesold(saveNums, ListNumbers)

# a, b, c, d, ... !, @, #, $, %, ... ====> (str)
def _speakAlphabet(speak):

    for i in speak:

        if i not in alPhaBet:

            try:

                if int(i) not in ListNumbers:

                    ListNumbers.append(int(i))
                    ListNumbers.sort()


            except ValueError or TypeError:

                alPhaBet.append(i)
                
    _chack(saveAlphabet, alPhaBet)

# Operators doing (int and str)
def _givWithOperatorsDo():

    azartRandom = _bigRandom(1)

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
                        
            _savesold(workNums, listIIWorkWithNumbers)

    #  text
    else:

        if alPhaBet:

            for i in itt.combinations_with_replacement(alPhaBet, 5):

                listIIWorkWithAlphabet.append(i)

            _savesold(workAlphabet, listIIWorkWithAlphabet)
                
                
def goNum(col):
    
    _podbor(col)
    
def goLet(text):
    
    _speakAlphabet(text)

def runIntOrStr():
    
    _givWithOperatorsDo()

def lookLet(see):
    
    if see in listIIWorkWithAlphabet:

        print(see, 'in listIIWorkWithAlphabet')

    elif see in alPhaBet:

        print(see, 'in alPhaBet')
      
'''      
#  Тест для работы с модулем
while True:

    a = input('\n~>')

    command = a[0]
    
    if command == '1':
    
        inp = input('==>')
        
        goNum(inp)
        
    elif command == '2':
    
        inp = input('==>')
        
        goLet(inp)
        
    elif command == '3':
    
        inp = input('==>')
        
        lookLet(inp)
        
    elif command == '4':
    
        runIntOrStr()
'''