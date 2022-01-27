# Для натурального N создать множество: 1, -3, 9, -27, 81 и т.д.

def numbers (N):
    a = set()
    d = 0
    for i in range(N):
        if d % 2 == 0:
            i = 3**d
        else:
            i = -3**d
        d += 1
        a.add(i)
    return a

print(numbers(10))

