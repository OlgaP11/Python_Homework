from datetime import datetime

def log_in(data):
    time = datetime.now()
    with open('log.txt', 'a', encoding='utf-8') as file:
        file.write(f'{time} {data}\n')