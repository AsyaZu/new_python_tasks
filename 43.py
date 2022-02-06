# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

list = [1, 2, 3, 5, 1, 5, 3, 10]  
list1 = [] 
for i in range(len(list)): 
    count = 0 
    for k in range(len(list)):  
        if list[i] == list[k]:  
            count += 1 
    if count == 1:  
        list1.append(list[i])    
print(list1)


