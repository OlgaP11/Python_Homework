def supply_data():
    way = input('Выберите способ ввода данных: 1 - взять из файла, 2 - ввести вручную: ')
    if way == '1':
        return input('Введите путь к файлу с данными: '), way
    else:
        return input('Введите фамилию, имя, номер телефона и описание через пробел: '), way

def view_data():
    print('Данные успешно сохранены.')