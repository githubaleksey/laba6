print('Введите текст')
b=str(input())
c=[]
for el in b:
    if el not in c:
        c.append(el)
print('Количесвто различных букв равно =',len(c))
