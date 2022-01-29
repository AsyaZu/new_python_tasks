# Найти произведение пар чисел в списке. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д. 
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15] 

from random import*
def mult (n):
    list = [randrange(1, n + 1) for i in range(n)]
    print(list)
    new_list = []
    for i in range(n // 2 + n % 2):
        new_list.append(list[i]*list[-i-1])
    return new_list

print(mult(5))
