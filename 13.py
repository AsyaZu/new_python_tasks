# Пользователь задаёт две строки. Определить количество количество вхождений одной строки в другой.

s1 = 'qwertyert'
s2 = 'er'
count = 0
while len(s1) > 0 or i != -1:
    i = s1.find(s2)
    count += 1
    i = s1.find(s2, i + 1)  
print(count)