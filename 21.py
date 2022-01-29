# Определить, позицию второго вхождения строки в списке либо сообщить, что его нет.

list = ['qq', 'ww', 'qq', 'qqq', 'qqw', 'er']
s1 = 'qq'
try:
    a = list.index(s1)
    b = list.index(s1, a + 1)
    print(b)
except ValueError:
    print(False)


