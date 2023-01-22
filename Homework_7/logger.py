from datetime import datetime as dt

def log_in(text, data):
    time = dt.now().strftime('%H:%M')
    with open ('log.txt', 'a', encoding = 'utf-8') as file:
        file.write(f'{time} {text}\n {data}\n')