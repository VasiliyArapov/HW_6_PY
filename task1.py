# Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

def arithmetic_progression(first_el, d, amount):
    res = []
    for i in range(1, amount + 1):
        res.append(first_el + (i - 1) * d)
    return res


first_el = int(input())
d = int(input())
amount = int(input())

print(*arithmetic_progression(first_el, d, amount))
