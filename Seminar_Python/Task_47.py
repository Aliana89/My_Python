#Задача No47. Решение в группах

"""def same_by(characteristic, objects):
    # return list(filter(characteristic, objects))==objects
    return len(list(filter(characteristic, objects)))==len(objects)
values = [0, 2, 10, 6] 
if same_by(lambda x: x % 2 == 0, values):
    print('same') 
else:
    print('different')"""
def same_by(characteristic, objects):
    if len(objects) > 1:
        value = characteristic(objects[0])
        for obj in objects[1:]:
            if characteristic(obj) != value:
                return False
    return True

values = [0, 2, 10, 6]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')