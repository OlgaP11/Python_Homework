def get_data(path, way):
    new_data = list()
    if way == '1':
        with open (path,'r', encoding = 'utf-8') as data:
            for line in data:
                if ',' in line:
                    new_data.append(line.split(','))
                else:
                    new_data.append(line.split())
    else:
        new_data = path.split(' ')
    return new_data