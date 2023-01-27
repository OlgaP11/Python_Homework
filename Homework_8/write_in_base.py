def write_data(base):
    with open ('base.txt','a',encoding='utf8') as data:
        for key,value in base.items():
            data.write(f'{key}| {value}\n') 