# Задать список из N элементов, заполненных числами из [-N, N]. 
# Найти произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число
from random import*

def array (n):
    list = [randrange(-n, n + 1) for i in range(n)]
    data = open('file.txt', 'r')
    answer = 1
    for i in data:
        answer *= list[int(i)]
    data.close()
    return list, answer

print(array(10))

