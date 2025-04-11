import csv

import datetime,random

def FileCsvToDict(path):
    with open(path, 'r', encoding='cp1251') as file:
        reader = csv.reader(file, lineterminator='\n')
        data = []
        for i, line in enumerate(reader):
            if i == 0: 
                columns = line
                continue
            data.append({
                columns[i]: item 
                for i, item in enumerate(line)})
        return data
    
            
def get_otchet(data):
    if len(data) == 0: return print('Нету данных')
    with open('otchet.csv', 'w', encoding='cp1251') as file:
        writer = csv.writer(file, lineterminator='\n')
        for i, row in enumerate(data):
            if i == 0: writer.writerow(row.keys())
            else: writer.writerow(row.values())
    print("Отчет сохранен в otchet.csv")
            
def get_random_date():
    return datetime.datetime(random.randint(1950, 2000), random.randint(1, 12), random.randint(1, 28))
