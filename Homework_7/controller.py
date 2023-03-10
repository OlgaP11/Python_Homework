from data_provider import get_data as gd
from data_writer import write_data as wd 
from logger import log_in as log
from user_interface import supply_data as sd, view_data as vd

def insert_new_data():
    user_path, user_way = sd()
    new_data = gd(user_path, user_way)
    log('Пользователь хочет записать новые номера',new_data)
    wd(new_data,user_way)
    log('Данные успешно сохранены', '')
    vd()
