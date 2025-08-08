stroka = input("Введите строку: ")

for i in range(len(stroka)): #цыкл прогоняем столько раз сколько символов в строке
    stroka = stroka.replace("()", '').replace("{}", '').replace("[]", '') #каждую этерацию удаляем в правильно закрытые скобки 
    if len(stroka) == 0:#если переменная = 0 то скобки были закрыты если нет то выводиться false 
        print('true')
        break
else:
    print('false')

