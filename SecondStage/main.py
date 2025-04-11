from utils import FileCsvToDict, get_random_date, get_otchet

import asyncio

from load_config import config

db = config.database.model


import datetime

async def insert_data():
    students_input = FileCsvToDict('stud.csv')
    statement_input = FileCsvToDict('statements.csv')
    ids = {}
    
    for student in students_input:
        d, m, y = map(int, student['ДатаРождения'].split('.'))
        birth_date = datetime.datetime(y, m, d)
        
        city_id = await db.add_town(student['Город'], student['Регион'], None)
        student_phone_id = await db.add_phone_number(student["Телефон"])
        faculty_id = await db.add_faculty(student['Факультет'])
        specialty_id = await db.add_specialty(student['Специальность'], faculty_id)
        group_id = await db.add_group(student['Группа'], specialty_id)
        first_parent_phone_id = None if not student['НомерТелефонаРодитель1'].strip() else await db.add_phone_number(student['НомерТелефонаРодитель1'])
        second_parent_phone_id = None if not student['НомерТелефонаРодитель2'].strip() else await db.add_phone_number(student['НомерТелефонаРодитель2'])
        
        first_parent = None if not student['Родитель1'].strip() else await db.add_parents(student['Родитель1'], 'Жен', get_random_date(), city_id)
        second_parent = None if not student['Родитель2'].strip() else await db.add_parents(student['Родитель2'], 'Муж', get_random_date(), city_id)
        
        await db.add_phone_number_parent(first_parent_phone_id, first_parent)
        await db.add_phone_number_parent(second_parent_phone_id, second_parent)
        
        student_id = await db.add_student(student['ФИО'], student['Пол'], birth_date, city_id, group_id)
        await db.add_phone_number_student(student_phone_id, student_id)
        await db.add_student_parent(student_id, first_parent)
        await db.add_student_parent(student_id, second_parent)
        
        ids[f'stud{student['ФИО']}|{student['Группа']}'] = student_id
        ids[f'fac{student['Факультет']}'] = faculty_id
        ids[f'spec{student['Специальность']}'] = specialty_id
        ids[f'group{student['Группа']}'] = group_id
        
        
    for statement in statement_input:
        d, m, y = map(int, statement['ДатаЭкзамена'].split('.'))
        date_statement = datetime.datetime(y, m, d)
        
        d, m, y = map(int, statement['ДатаСдачи'].split('.'))
        due_date = datetime.datetime(y, m, d)
        
        student_id = ids.get(f'stud{statement['ФИО']}|{statement['Группа']}')
        
        discipline_id = await db.add_discipline(statement['Дисциплина']) or \
            ids.get(f'dis{statement['Дисциплина']}')
            
        lecturer_id = await db.add_teacher(statement['Преподаватель']) or \
            ids.get(f'lec{statement['Преподаватель']}')
        
        group_id = ids.get(f'group{statement['Группа']}')    
          
        statement_id = await db.add_statement(date_statement, int(statement['Номер']), group_id, discipline_id, lecturer_id)

        await db.add_grade(due_date, student_id, statement_id, statement['Оценка'])
        
        ids[f'dis{statement['Дисциплина']}'] = discipline_id
        ids[f'lec{statement['Преподаватель']}'] = lecturer_id

async def main():
    await db.create_tables()
    data = await db.get_otchet_data()
    get_otchet(data)
    
    
if __name__ == "__main__":
    asyncio.run(main())