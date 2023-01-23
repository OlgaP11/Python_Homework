def get_data(path):
    new_data = list()
    with open (path,'r', encoding = 'utf-8') as data:
        for line in data:
            if ',' in line:
                new_data.append(line.split(','))
            else:
                new_data.append(line.split())
    return new_data