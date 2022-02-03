# В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найти его.

with open('35.txt', 'r') as data:
    for i in data:
        data = list(map(int, i.split()))
print(data)
data = sorted(data)
print(data)

for i in range(1, len(data)):
    if data[i] - 1 != data[i - 1]:
        print(data[i] - 1)