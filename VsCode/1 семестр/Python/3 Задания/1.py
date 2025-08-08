scob = {"(":")",'[':']','{':'}'}
stroka = input()
def fun(strk, p):
    try:
        if scob[p] == strk[0]:
            return 'true'
    except:
        return 'false'

    if len(strk) < 2:
        return 'false'
    else:
        return fun(strk[1:], strk[0])


print(fun(stroka[1:], stroka[0]))
