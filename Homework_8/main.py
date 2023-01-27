from user_interface import user_choice 
from edit_base import create_department, create_worker, change_dep_of_worker, edit_department,edit_worker,delete_department,delete_worker
from supply_base import supply_data
from write_in_base import write_data
from export import export_data

def main():
    cur_choice = int(user_choice)
    while cur_choice != 9:
        if cur_choice == 1:
            create_department()
        elif cur_choice == 2:
            create_worker()
        elif cur_choice == 3:
            edit_worker()
        elif cur_choice == 4:
            delete_worker()
        elif cur_choice == 5:
            change_dep_of_worker()
        elif cur_choice == 6:
            export_data()
        elif cur_choice not in (1,2,3,4,5,6,9):
            print('Вы ввели некорректную команду. Попробуйте снова. ')


if __name__ == "__main__":
    main()