"""Задача №45. Решение в группах
Два различных натуральных числа n и m называются
дружественными, если сумма делителей числа n
(включая 1, но исключая само n) равна числу m и
наоборот. Например, 220 и 284 – дружественные числа.
По данному числу k выведите все пары дружественных
чисел, каждое из которых не превосходит k. Программа
получает на вход одно натуральное число k, не
превосходящее 105
. Программа должна вывести все
пары дружественных чисел, каждое из которых не
превосходит k. Пары необходимо выводить по одной в
строке, разделяя пробелами. Каждая пара должна быть
выведена только один раз (перестановка чисел новую
пару не дает).
Ввод: Вывод:
300 220 284
def sum_divisors(n):
    sum_div = 0
    for i in range(1, n):
        if n % i == 0:
            sum_div += i
    return sum_div

k = int(input("Введите число k: "))

result_list = []

for n in range(1, k+1):
    m = sum_divisors(n)
    if sum_divisors(m) == n and m != n:
        result_list.append((n, m))

for result in result_list:
    print(result)"""
def sum_divisors(num):
    # Функция для получения суммы делителей числа, исключая само число
    divisors_sum = 0
    for i in range(1, num):
        if num % i == 0:
            divisors_sum += i
    return divisors_sum

k = int(input("Введите число k: "))

friendly_pairs = []
for n in range(1, k):
    m = sum_divisors(n)
    if sum_divisors(m) == n and n < m:
        friendly_pairs.append((n, m))

for pair in friendly_pairs:
    print(pair)