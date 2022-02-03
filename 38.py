# Напишите программу, удаляющую из текста все слова содержащие "абв".

text = 'апе пероо зшвььа рпнабв оор абв орпа абвгрп ва бв аб ав амипрбпров'
list = text.split()
n = len(list)
list1 = []
f = 'абв'
for i in list:
    if not (i == f or i.find(f) != -1):
        list1.append(i)
        
print(' ' .join(list1))