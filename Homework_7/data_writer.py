def write_data(incom_data, way):
    if way == '1':
        with open ('phone_num_base.txt', 'a', encoding = 'utf-8') as data:
            for i in range (len(incom_data)):
                for j in range (len(incom_data[i])):
                    data.write(incom_data[i][j].lstrip() +'\n')
    else:
        with open ('phone_num_base.txt', 'a', encoding = 'utf-8') as data:
            for i in range (len(incom_data)):
                data.write(incom_data[i].lstrip() +'\n')
