with open('first.txt', 'r', encoding='utf-8') as first:
    with open('second.txt', 'r', encoding='utf-8') as second:
        file1  = [i.replace('\n', '') for i in first.readlines()]
        file2 = second.read().split()
        for i in range(len(file1)):
            print(f'Сотрудник {file1[i]}, должность - {file2[i]}')