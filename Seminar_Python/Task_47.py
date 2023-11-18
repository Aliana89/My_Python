#Задача No47. Решение в группах

def same_by(characteristic, objects):
    # return list(filter(characteristic, objects))==objects
    return len(list(filter(characteristic, objects)))==len(objects)
values = [0, 2, 10, 6] 
if same_by(lambda x: x % 2 == 0, values):
    print('same') 
else:
    print('different')