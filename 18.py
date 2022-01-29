# Реализовать алгоритм перемешивания списка

from random import*

def change_array(n):
    list = [randrange(1, n + 1) for i in range(n)]
    print(list)
    for i in range(n):
        a = randint(i, n - 1)
        list[i], list[a] = list[a], list[i]
    return list
print(change_array(10))
    
