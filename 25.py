# Написать программу преобразования десятичного числа в двоичное

def change (n):
    s = 0
    sum = 0
    while n > 0:
        a = n % 10 * 2**s
        n = n // 10
        sum += a
        s += 1
    return sum
print(change(10011))