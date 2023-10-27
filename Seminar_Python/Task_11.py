""" Напишите программу для печати всех уникальных значений в словаре.
Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]
Output: {'S005', 'S002', 'S007', 'S001', 'S009'} """
lst = [{"V": "S001"}, {"V": "S002"},{"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]
list1 = set()
for i in lst:
    for j,y in i.items():
        print(j,y)
        list1.add(y)
        #list1.add(i[j])
print(list1)