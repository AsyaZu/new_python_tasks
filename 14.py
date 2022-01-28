# Подсчитать сумму цифр в вещественном числе

def sum (n):
    sum = 0
    n1 = int(n)
    n2 = n - n1
    while n1 > 0:
        sum = sum + n1 % 10
        n1 = n // 10
    while n2 > 0:
        n2 = n2 * 10
        sum = sum + int(n2)
        n2 = n2 - int(n2)
    return sum
    
print(sum(14.23))
