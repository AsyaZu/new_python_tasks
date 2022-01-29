# Определить, присутствует ли в заданном списке строк, некоторое число 

def find_num (list, n):
    answer = False
    for i in list:
        a = str(i)
        if a == n or a == str(n) or a.find(str(n)) != -1:
            answer = True       
    return answer

list = [2, 'aaa', 'htd', 5, 'ty', '44']
n = 4
print(find_num(list, n))