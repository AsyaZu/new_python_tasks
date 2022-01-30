# Дано число. Составить список чисел Фибоначчи, в том числе для отрицательных индексов. 
# Т е для k = 5, список будет выглядеть так: [5, −3,  2, −1,  1, 0, 1, 1, 2, 3, 5]

def fibonacci(n):
    if n < 2:
        return n
    return (fibonacci(n-1) + fibonacci(n-2))

n = 10
a = ''
for i in range(n):
    a += f'{fibonacci(i)} '
print(a)