# В заданном списке вещественных чисел найдите разницу между максимальным и минимальным значением дробной части элементов. 
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from random import* 

def diff (n):
    list = [round(uniform(0.0, 11.0),3) for i in range(n)]
    list1 = []
    print(list)
    for i in list:
        i = i - int(i)
        list1.append(i)
    return(round(max(list1) - min(list1), 3))

print(diff(5))
