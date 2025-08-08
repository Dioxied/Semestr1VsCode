def fun(sp=[]):
    if len(sp) < 3:
        return sp
    if sp[-1] < sp[-2]:
        sp.remove(sp[-1])
    while True:
        udal = False
        for i in range(2, len(sp)-1):
            if sp[i-2] < sp[i-1] > sp[i]:
                sp.remove(sp[i-1])
                udal = True
        if not udal:
            break
    return sp
            
spisok = [int(i) for i in input().split()]
all = []
for i in range(len(spisok)):
    for j in range(i, len(spisok)):
        pos = [spisok[i]]
        for k in range(j, len(spisok)):
            if spisok[k] > spisok[i]:
                pos.append(spisok[k])
        all.append(fun(pos))
        pos=[]
maxi = []
for i in all:
    if len(i) > len(maxi):
        maxi = i
print(maxi)
print(len(maxi))