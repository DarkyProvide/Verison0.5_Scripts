import random as rad
import itertools as itt

alPhaBet = []

ListNumbers = [0]

listIIWorkWithNumbers = []

listIIWorkWithAlphabet = []

saveNums = r'C:\GitProgects\Verison0.5_Scripts\TwoPCRescui\Pac\saveNums.txt'
saveAlphabet = r'C:\GitProgects\Verison0.5_Scripts\TwoPCRescui\Pac\saveAlphabet.txt'
workNums = r'C:\GitProgects\Verison0.5_Scripts\TwoPCRescui\Pac\workNums.txt'
workAlphabet = r'C:\GitProgects\Verison0.5_Scripts\TwoPCRescui\Pac\workAlphabet.txt'

#  saves
def _saveprogress(fileName, textInp):

    fileA = open(fileName, 'a')
    
    fileA.writelines(str(textInp))
    
    fileA.close()

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

#  1, 2, 3, 4, ... ====> (int)
def goNum(number):
    
    lowSort = 0

    while lowSort != max(list(ListNumbers)):

        if lowSort not in ListNumbers:

            ListNumbers.append(lowSort)
            
            _saveprogress(saveNums, (str(lowSort) + ','))
        
        lowSort += 1

    ListNumbers.sort()

    for zero in range(int(number)):

        ListNumbers.append(max(list(ListNumbers)) + 1)
        
        _saveprogress(saveNums, (str(max(list(ListNumbers)) + 1) + ','))
    
#  a, b, c, d, ... !, @, #, $, %, ... ====> (str)
def goLet(text):
    
    for i in text:

        if i not in alPhaBet:

            try:

                if int(i) not in ListNumbers:

                    ListNumbers.append(int(i))
                    ListNumbers.sort()
                    _saveprogress(saveNums, i)


            except ValueError or TypeError:

                alPhaBet.append(i)
                _saveprogress(saveAlphabet, i)

#  run II func on rundom
def runIntOrStr():
    
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
                _saveprogress(workNums, (str(a + b) + ','))

            elif randa == 1 and (a - b) not in list(listIIWorkWithNumbers):

                listIIWorkWithNumbers.append(a - b)
                _saveprogress(workNums, (str(a - b) + ','))

            elif randa == 2 and (a * b) not in list(listIIWorkWithNumbers):

                listIIWorkWithNumbers.append(a * b)
                _saveprogress(workNums, (str(a * b) + ','))

            elif randa == 3:

                try:

                    if (a / b) not in list(listIIWorkWithNumbers):
                        listIIWorkWithNumbers.append(a / b)
                        _saveprogress(workNums, (str(a / b) + ','))

                except ZeroDivisionError:

                    if (a / 1) not in list(listIIWorkWithNumbers):
                        listIIWorkWithNumbers.append(a / 1)
                        _saveprogress(workNums, (str(a / 1) + ','))

    #  text
    else:

        if alPhaBet:
            
            qwer = rad.randint(2, 10)
            
            for i in itt.combinations_with_replacement(alPhaBet, qwer):

                listIIWorkWithAlphabet.append(i)
                _saveprogress(workAlphabet, i)

#  Chack func
def lookLet(see):
    
    if see in listIIWorkWithAlphabet:

        print(see, 'in listIIWorkWithAlphabet')

    elif see in alPhaBet:

        print(see, 'in alPhaBet')
       



#  Проверка и сортировка всех данных при запуске
#===============================================
#  Работа с алфавитом
#--------------------
#  Обычный алфавит
try:
    readAlphabetSaves = open(saveAlphabet, 'r')
    readLinesAlphabet = (readAlphabetSaves.readlines())[0]
    for i in readLinesAlphabet:
        alPhaBet.append(i)
    readAlphabetSaves.close()
except IndexError:
    pass
print('Progress starting:     |', end='')
#  Переработанный программой алфавит
try:
    readAlphabetWork = open(workAlphabet, 'r')
    readLinesAlphabetW = (readAlphabetWork.readlines())[0]
    try:
        allDalp = 0
        i = 0
        while readLinesAlphabetW[i] in list(readLinesAlphabetW):
            if readLinesAlphabetW[i] == '(':
                allDalp += 1
            i += 1
    except IndexError:
        l = []
        try:
            p = 0
            for t in range(allDalp):
                e = ''
                while readLinesAlphabetW[p] != ')':
                    if readLinesAlphabetW[p + 1] != ',' and readLinesAlphabetW[p + 1] != ' ' and readLinesAlphabetW[p + 1] != '\'':
                        if (readLinesAlphabetW[p + 1]) != ')':
                            e = e + (readLinesAlphabetW[p + 1])
                    p += 1
                p += 1
                l.append(tuple(e))
                for i in l:
                    listIIWorkWithAlphabet.append(i)
        except IndexError:
            pass
    readAlphabetWork.close()
except IndexError:
    pass
print('|', end='')


#  Работа с цифрами
#------------------
#  Обычные числа
try:
    readNUMSSaves = open(saveNums, 'r')
    readLinesNUMS = (readNUMSSaves.readlines())[0]
    try:
        i = 0
        while readLinesNUMS[i] in list(readLinesNUMS):
            dopListOne = []
            while readLinesNUMS[i] != ',':
                dopListOne.append((readLinesNUMS)[i])
                i += 1
            w = ''
            for q in dopListOne:
                w = w + q
            ListNumbers.append(int(w))
            ListNumbers.sort()
            i += 1
    except IndexError:
        pass
    readNUMSSaves.close()
except IndexError:
    pass
print('|', end='')
#  Переработанные программой числа
try:#
    readNUMSWorks = open(workNums, 'r')
    readLinesNUMSW = (readNUMSWorks.readlines())[0]
    try:
        i = 0
        while readLinesNUMSW[i] in list(readLinesNUMSW):
            dopListTwo = []
            while readLinesNUMSW[i] != ',':
                dopListTwo.append((readLinesNUMSW)[i])
                i += 1
            w = ''
            for q in dopListTwo:
                w = w + q
            try:
                listIIWorkWithNumbers.append(int(w))
            except ValueError:
                listIIWorkWithNumbers.append(float(w))
            i += 1
    except IndexError:
        pass
    readNUMSWorks.close()
except IndexError:
    pass
print('|', end='')
#===============================================


#  Мини код для тестинга

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
        
        print(listIIWorkWithAlphabet)

    elif command == '4':
    
        runIntOrStr()
        
    elif command == '=':

        print(ListNumbers)
        print(alPhaBet)
        print(listIIWorkWithNumbers)
        print(listIIWorkWithAlphabet)
        
    elif command == '5':

        quit()
