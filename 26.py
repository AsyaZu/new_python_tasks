# Дано число. Составить список чисел Фибоначчи, в том числе для отрицательных индексов. 
# Т е для k = 5, список будет выглядеть так: [5, −3,  2, −1,  1, 0, 1, 1, 2, 3, 5]


for i in range(-10, 11):
    if i < 0:
        i = (-1)**(i+1)*i
    elif i in (1, 2):
        i = 1
    else:
        i = (i - 1) + (i - 2)
    print(i)

    
    


