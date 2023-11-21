print('Введите текст')
a='abcdefghiJklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
b=str(input())
s=list(b)
f=0
Max_=0
n=0
for i in range(len(s)):
    if s[i] not in a:
        n=n+1
        f = n
    else:
        f=n
        n=0
if f>Max_:
    Max_=f
    f=0
print('Максимальная последовательность символов без латинских букв =',Max_)
