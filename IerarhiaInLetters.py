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


oup = dict()
x = ''
while True:
    x = input()
    if x == 'quit':
        quit()
    for i in set(x):
        if i not in oup.keys():
            oup[i] = 0
    for i in list(x):
        oup[i] += 1
    oup = sort(oup)
    for i in oup.keys():
        print(i, ":", oup[i])
