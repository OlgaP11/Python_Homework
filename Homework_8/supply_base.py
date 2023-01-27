def supply_data():
    base ={}
    with open ('base.txt','r',encoding='utf8') as data:
        for line in data:
            (key, val) = line.split('|')
            base[key] = val.replace('\n', '')   
    for key,val in base.items():
        base[key] = val.split('],')
    return base
    