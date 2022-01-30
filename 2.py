# Найти максимальное из пяти чисел

def max (a, b):
    if a > b:
        return a
    else:
        return b

a = 120
b = 130
c = 56
d = 30
e = 60
print(max(max(max(max(a, b), c), d), e))