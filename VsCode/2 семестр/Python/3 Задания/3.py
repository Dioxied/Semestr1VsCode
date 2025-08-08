def umn():
    el = sp[sp.index("*")-1] * sp[sp.index("*")+1]
    sp.remove(sp[sp.index("*")-1])
    sp.remove(sp[sp.index("*")+1])
    sp[sp.index("*")]=el
def delen():
    el = sp[sp.index("/")-1] / sp[sp.index("/")+1]
    sp.remove(sp[sp.index("/")-1])
    sp.remove(sp[sp.index("/")+1])
    sp[sp.index("/")]=el
def plus():
    el = sp[sp.index("+")-1] + sp[sp.index("+")+1]
    sp.remove(sp[sp.index("+")-1])
    sp.remove(sp[sp.index("+")+1])
    sp[sp.index("+")]=el
def minus():
    el = sp[sp.index("-")-1] - sp[sp.index("-")+1]
    sp.remove(sp[sp.index("-")-1])
    sp.remove(sp[sp.index("-")+1])
    sp[sp.index("-")]=el


urav = input("Введите уравнение: ")+'.'#принимаем строку с уравнениям + .
sp=[]
r=''
for i in urav: #через цыкл проходим все элементы строки, и пытаемся конвертировать в целочисленное
    try:
        r+=str(int(i))
    except:
        sp.append(int(r))
        r=''
        sp.append(i)

sp=sp[:-1] # удаляем точку из списка
for i in range(len(sp), 1, -2):
    if "*" in sp or '/' in sp:
        if "*" in sp and '/' in sp:
            if sp.index("*") < sp.index("/"):
                umn()
                continue
            else:
                delen()
                continue
        elif "*" in sp:
            umn()
            continue
        elif "/" in sp:
            delen()
            continue
    if "+" in sp or '-' in sp:
        if "+" in sp and '-' in sp:
            if sp.index("+") < sp.index("-"):
                plus()
                continue
            else:
                minus()
                continue
        elif "+" in sp:
            plus()
            continue
        elif "-" in sp:
            minus()
            continue
print(sp[-1])

