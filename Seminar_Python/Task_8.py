#Задача No19. Решение в группах
#Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо, K – положительное число.
#Input: [1, 2, 3, 4, 5] k = 3 Output: [4, 5, 1, 2, 3]

lst = [1, 2, 3, 4, 5]
k = 7
l = len(lst)


#print(list1.pop())
#print(list1.remove(4))
k = k%l

"""for i in range(k):
    temp = lst.pop()
    lst.insert(0,temp)
    print(lst)  """

#второе решение
list2 = lst[-k :] + lst[ :-k]
print(list2)