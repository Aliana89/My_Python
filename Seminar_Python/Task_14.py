
"""Задача No37. Общее обсуждение
Дано натуральное число N и последовательность из N элементов. Требуется вывести эту последовательность в обратном порядке.
Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).
Input: 2 -> 3 4 Output: 4 3"""
n = 4
def functional(qty):
    if qty == 0:
        return '+' # пустая строка
    number = input("Введите число: ")
    return functional(qty-1) + number

print(functional(4))