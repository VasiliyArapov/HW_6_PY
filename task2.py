# Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)


def is_in_mass(num_list, num_min, num_max):
    res = []
    for i in range(len(num_list)):
        if num_min <= num_list[i] <= num_max:
            res.append(i)
    return res


num_list = list(map(int, input().split()))
num_min = int(input())
num_max = int(input())
print(is_in_mass(num_list, num_min, num_max))
