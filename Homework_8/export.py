def export_data(base):
    with open ('user_request.csv', 'w', encoding='utf-8') as file:
        for key,value in base.items():
            file.write(f'{key}\n {value}\n')