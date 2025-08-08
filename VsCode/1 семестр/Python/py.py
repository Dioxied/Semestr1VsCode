polib = [['а','б','в','г','д'],['е','ж','з','и','к'],['л','м','н','о','п'],['р','с','т','у','ф'],['х','ц','ч','ш','щ'],['ы','ь','э','ю','я']]

def f(s):
    if s == '':
        return ''
    p=False
    for i in range(len(polib)):
        for j in range(len(polib[i])):
            if s[0] == polib[i][j]:
                return str(i+1)+str(j+1)+' '+f(s[1:])
                p=True
                break
        if p:
            break
                    
    

input = input().lower().replace('ё', 'е').replace('й', 'и').replace('ъ', 'ь')
print(f(input))
    
        
                




