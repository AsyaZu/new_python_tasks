# Задать список из N чисел последовательности (1+1/n)**n и вывести на экран их сумму
n = 3
a = [(1 + i/n)**n for i in range(1, n + 1)]
sum = 0
for i in a:
    sum += i
print(a)
print(sum)