"""
    Программа Python для фильтрации нечетных чисел
    в списке, используя функцию filter()
"""

# список чисел
array = [0, 1, 0, 0, 4, 5, 6, 7, 0, 8, -4, 0]

# функция, которая проверяет числа
def filter_odd_num(in_num):
    if in_num == 0:
        return False
    else:
        return True

# Применение filter() для удаления нечетных чисел
out_filter = filter(filter_odd_num, array)

print("Тип объекта out_filter: ", type(out_filter))
print("Отфильтрованный список: ", list(out_filter))
