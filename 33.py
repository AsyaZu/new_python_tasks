# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k. 
# *Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import*
list = []
for i in range(10):
    k = randint(0, 100)
    list.append(k)
    with open('num.txt', 'w') as data:
        for k in list:
            data.write(f'10*x^{k} = 0\n')
print(list)



