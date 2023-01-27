from user_interface import user_choice 
from edit_base import create_department, create_worker, change_dep_of_worker, edit_department,edit_worker,delete_department,delete_worker
from supply_base import supply_data
from write_in_base import write_data
from export import export_data
from logger import log_in as log

def main():
    cur_base = supply_data()
    cur_choice = user_choice()
    if cur_choice == 1:
        create_department(cur_base)
        log('Создание нового отдела')
    elif cur_choice == 2:
        create_worker(cur_base)
        log('Внесение нового сотрудника')
    elif cur_choice == 3:
        edit_worker(cur_base)
        log('Изменение информации о сотруднике')
    elif cur_choice == 4:
        delete_worker(cur_base)
        log('Удаление сотрудника')
    elif cur_choice == 5:
        change_dep_of_worker(cur_base)
        log('Изменение отдела у сотрудника')
    elif cur_choice == 6:
        export_data(cur_base)
        log('Экспорт базы в файл')
    elif cur_choice == 7:
        edit_department(cur_base)
        log('Изменение названия отдела')
    else:
        print('Вы ввели некорректную команду. Попробуйте снова. ')
    write_data(cur_base)


if __name__ == "__main__":
    main()