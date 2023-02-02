from datetime import datetime

def log_in(title, data):
    with open("log.txt", "a", encoding='utf-8') as file:
        file.write(f'{datetime.now()}, {title} : {data}.\n')