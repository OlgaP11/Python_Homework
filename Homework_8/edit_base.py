all_data = {}
workers = {}
id_worker = 0

def create_department():
    dep_name = input('Введите название отдела: ')
    if dep_name in all_data:
        print('Данный отдел уже существует.')
    else:
        all_data['dep_name'] = None

def create_worker():
    surname = input('Введите фамилию сотрудника: ')
    name = input('Введите имя сотрудника: ')
    patronymic = input('Введите отчество сотрудника: ')
    if surname in workers.values() and name in workers.values() and patronymic in workers.values():
        print('Такой сотруник уже существует.')
    else:
        date_birth = input('Введите дату рождения сотрудника в формате дд.мм.гг: ')
        phone_number = input('Введите номер телефона сотрудника: ')
        adress = input('Введите адрес сотрудника: ')
        department = input('Введите название отдела, где работает сотрудник: ')
        global id_worker
        id_worker += 1
        workers[id_worker] = [surname, name, patronymic, date_birth, phone_number, adress, department]

def edit_worker():
    id_search = input('Введите id сотрудника: ')
    if id_search not in workers.keys():
        print('Сотрудник с таким id не найден.')
    else:
        surname = input('Введите фамилию сотрудника: ')
        name = input('Введите имя сотрудника: ')
        patronymic = input('Введите отчество сотрудника: ')
        print('Такой сотруник уже существует.')
        date_birth = input('Введите дату рождения сотрудника в формате дд.мм.гг: ')
        phone_number = input('Введите номер телефона сотрудника: ')
        adress = input('Введите адрес сотрудника: ')
        department = input('Введите название отдела, где работает сотрудник: ')
        workers[id_search] = [surname, name, patronymic, date_birth, phone_number, adress, department]

def edit_department():
    old_dep_name = input('Введите старое название отдела: ')
    if old_dep_name in all_data.keys():
        new_dep_name = input('Введите новое название отдела: ')
        all_data[new_dep_name] = all_data.pop(old_dep_name)
    else:
        print('Отдела с таким названием нет.')

def change_dep_of_worker():
    id_search = input('Введите id сотрудника: ')
    if id_search not in workers.keys():
        print('Сотрудник с таким id не найден.')
    else:
        new_dep = input('Введите название нового отдела: ')
        workers[id_search][-1] = new_dep
        
def delete_department():
    dep_name = input('Введите название отдела: ')
    if dep_name in all_data.keys():
        del all_data [dep_name]
    else:
        print('Отдела с таким названием нет.')

def delete_worker():
    id_search = input('Введите id сотрудника: ')
    if id_search not in workers.keys():
        print('Сотрудник с таким id не найден.')
    else:
        del workers [id_search]

