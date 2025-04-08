from load_config import config, STATEMENT_INPUT, STUDENTS_INPUT

import asyncio, datetime

db = config.database.model

async def main():
    await db.create_tables()
    ids = {}
    for student in STUDENTS_INPUT:
        y, m, d = map(int, student['birth_date'].split('-'))
        birth_date = datetime.datetime(y, m, d)
        
        faculty_id = await db.add_faculty(student['faculty_short'], None)
        ids[f"faculty{student['faculty_short']}"] = faculty_id
        
        specialty_code, specialty_title = student['specialty'].split(' ', maxsplit=1)
        specialty_id = await db.add_specialty(specialty_code, specialty_title)
        ids[f'specialty{student['specialty']}'] = specialty_id
        
        group_id = await db.add_group(student['group_title'], faculty_id, specialty_id)
        ids[f"group{student['group_title']}"] = group_id
        
        student_phone_id = await db.add_phone_number(student['full_name'], None if not student['phone'].strip() else int(student['phone']))
        
        city_id = await db.add_city(student['city'], None, student['region'])
        
        parentFirstFio, parentFirstNumber = student['parent1_name'].strip() or None, \
                                            student['parent1_phone'].strip() or None
        parentFirstId = await db.add_phone_number(parentFirstFio, None if not parentFirstNumber else int(parentFirstNumber))
                                            
        parentSecondFio, parentSecondNumber = student['parent2_name'].strip() or None, \
                                            student['parent2_phone'].strip() or None
        parentSecondId = await db.add_phone_number(parentSecondFio, None if not parentSecondNumber else int(parentSecondNumber))
        
        parents_id = await db.add_parents(parentFirstId, parentSecondId)
        
        student_id = await db.add_student(student['full_name'], student['gender'], birth_date,
                             city_id, student_phone_id, group_id, faculty_id,
                             specialty_id, parents_id)
        
        ids[f'student{student['full_name']}|{student['group_title']}|{student['faculty_short']}'] = student_id
        
    for exam in STATEMENT_INPUT:
        y, m, d = map(int, exam['exam_date'].split('-'))
        exam_date = datetime.datetime(y, m, d)
        
        y, m, d = map(int, exam['submission_date'].split('-'))
        due_date = datetime.datetime(y, m, d)
        
        group_id = ids.get(f'group{exam['group']}')
        student_id = ids.get(f'student{exam['student_name']}|{exam['group']}|{exam['faculty']}')

        discipline_id = ids.get(f'discipline{exam['subject']}') or \
            await db.add_discipline(exam['subject'])
        ids[f'discipline{exam['subject']}'] = discipline_id
        
        statement_id = ids.get(f'statement{exam['statement_number']}') or \
            await db.add_statement(int(exam['statement_number']), discipline_id, group_id)
        ids[f'statement{exam['statement_number']}'] = statement_id
        
        lecturer_id = ids.get(f'lecturer{exam['teacher']}') or \
            await db.add_lecturer(exam['teacher'])
        ids[f'lecturer{exam['teacher']}'] = lecturer_id
        
        assessment_id = ids.get(f'assessment{exam['grade']}') or \
            await db.add_assessment(exam['grade'])
        ids[f'assessment{exam['grade']}'] = assessment_id
        await db.add_exam(statement_id, student_id, lecturer_id, assessment_id,
                          exam_date, due_date)
    
    # for a, b in ids.items():
    #     if a.startswith('statement'): print(f"{a} | {b}")
        
if __name__ == "__main__":
    asyncio.run(main())