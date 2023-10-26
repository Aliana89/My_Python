#Требуется найти в массиве list_1 самый близкий
#по величине элемент к заданному числу k и вывести его.

list_1 = [1, 2, 3, 4, 5]
k = 6
# 5
find_num = list_1[0]
for i in list_1:
    if abs(k - find_num) >= abs(k - i):
        find_num = i
   # else:
    #    find_num = find_num + 0
print(find_num)