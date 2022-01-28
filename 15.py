# Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда
# [ 1, 2, 6, 24 ]

def numbers (n):
    list = []
    fact = 1
    i = 1
    while i <= n:
        fact *= i
        list.append(fact)
        i += 1
    return list

print(numbers(5)) 