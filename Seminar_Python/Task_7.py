"""Задача No17. Решение в группах
Дан список чисел. Определите, сколько в нем встречается различных чисел.
Input: [1, 1, 2, 0, -1, 3, 4, 4] Output: 6"""
'''n =  [1, 1, 2, 0, -1, 3, 3, -1, 4, 1, 1,  -1,  4, 4]
dif = n[0]
count = 0
numbers = []
for i in n:
    if i not in numbers:
        numbers.append(i)
print(len(numbers))'''

n =  [1, 1, 2, 0, -1, 3, 3, -1, 4, 1, 1, 5, -1,  4, 4]
print(len(set(n)))
