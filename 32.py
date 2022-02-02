# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.

from random import randrange

numbers = [randrange(1, 11) for i in range(10)]
print(numbers)
print(list(set(numbers)))