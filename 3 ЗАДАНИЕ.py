try:
    import random
    print('Введите длину массива =')
    n=int(input())
    mass=[random.randint(-10,10) for i in range(0,n)]
    s=1
    k=[]
    for el in mass:
        if el<0: s=s*el
    for i in range(1, len(mass), 2):
        k.append(mass[i])
    for i in range(0, len(mass), 2):
        k.append(mass[i])
    print('Произведение отрицательных чисел =',s)
    print('Исходный массив =', mass)
    print('Преобразованный массив =',k)
except:
    print('Введено недопустимое значение')