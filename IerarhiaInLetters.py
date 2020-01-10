def sort(d):
    oup = dict()
    while d:
        mx = 0
        ind = 0
        for i in d.items():
            if i[1] > mx:
                mx = i[1]
                ind = i[0]
        oup[ind] = mx
        del d[ind]
    return oup

maxExpList = []
dopLetList = []
oup = dict()
while True:
    xd = input('\n')
    xdd = xd.split()
    if len(xdd) > 1:
        x = xdd
    else:
        x = xd
    #  Error ====
    if maxExpList:
        if sort(oup) in maxExpList:
        print(list(oup))
        dopLetList.append({1 : oup})
    #  ==========
    if x == 'quit':
        quit()
    for i in set(x):
        if i not in oup.keys():
            oup[i] = 0
    for i in list(x):
        oup[i] += 1
    #  Do sort in this block ------------------\
    maxExpList.append(sort(oup))  # <===-------/
    
    print(maxExpList)
    print(dopLetList)