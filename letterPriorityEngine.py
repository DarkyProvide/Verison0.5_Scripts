import itertools


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
    if x not in oup.keys():
        oup[x] = 1
    oup[x] += 1
    oup = sort(oup)
    # for i in oup.keys():
    #     print(i, ":", oup[i])
    print(list(oup.keys())[:2])
