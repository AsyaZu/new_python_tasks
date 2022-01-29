# Найти сумму чисел списка стоящих на нечетной позиции

from random import*
def sum (n):
    list = [randrange(-n, n + 1) for i in range(n)]
    print(list)
    sum = 0
    for i in range(1, n, 2):
        sum += list[i]
    return sum
print(sum(10))