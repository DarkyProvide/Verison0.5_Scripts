from hellowWorld import goNum, goLet, runIntOrStr, lookLet

#  Тест для работы с модулем(hellowWorld.py)
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