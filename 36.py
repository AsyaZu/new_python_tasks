# Дан список чисел. Выделить среди них числа, удовлетворяющие условию: следующее больше предыдущего. 
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д. 
# Порядок элементов менять нельзя

list = [1, 5, 2, 3, 4, 6, 1, 7]
list1 = [list[0]]
for i in range(1, len(list) - 1):
    if list[i - 1] < list[i] < list[i + 2]:
        list1.append(list[i])     
print(list1)


