# Пользователь задаёт две строки. Определить количество количество вхождений одной строки в другой.
def count (s1, s2):
    count = 0
    for i in range(len(s1)):
        if s2 == s1[i]:
            count += 1
    return count

s1 = 'qwertyert'
s2 = 'ert'
print(count(s1, s2))