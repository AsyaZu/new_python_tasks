# Задать список из N элементов, заполненных числами из [-N, N]. 
# Найти произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число
from random import*

with open('file.txt', 'w') as data:
    data.write('0\n')
    data.write('1\n')
    data.write('2\n')

def array (n):
    list = [randrange(-n, n + 1) for i in range(n)]
    print(list)
    data = open('file.txt', 'r')
    answer = 1
    for i in data:
        answer *= list[int(i)]
    data.close()
    return answer

print(array(10))


