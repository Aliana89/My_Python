"""Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
повторениями). Выдать без повторений в порядке возрастания все те числа, которые
встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
элементов второго множества. Затем пользователь вводит сами элементы множеств.
11 6
2 4 6 8 10 12 10 8 6 4 2
3 6 9 12 15 18
6 12 """

#var1 = '5 4'
var2 = '1 3 5 7 9'
var3 = '2 3 4 5'

#n, m = var1.split()
first_set = set(var2.split())
second_set = set(var3.split())

var4 = (first_set & second_set)

#result = sorted(var4)
#result = ' '.join(var4)
print(*var4)
