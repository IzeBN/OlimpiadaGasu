

CREATE_TABLES = """--sql
                CREATE TABLE IF NOT EXISTS specialties(
                    id SERIAL PRIMARY KEY,
                    specialty_code VARCHAR(32),
                    specialty_title VARCHAR(256)
                );

                CREATE TABLE IF NOT EXISTS faculties(
                    id SERIAL PRIMARY KEY,
                    faculty_abbreviation VARCHAR(16),
                    faculty_title VARCHAR(64)
                );

                CREATE TABLE IF NOT EXISTS regions(
                    id SERIAL PRIMARY KEY,
                    region_code INT DEFAULT NULL,
                    region_title VARCHAR(64)
                );

                CREATE TABLE IF NOT EXISTS cities(
                    id SERIAL PRIMARY KEY,
                    region_id INT REFERENCES regions(id),
                    city_title VARCHAR(64)
                );

                CREATE TABLE IF NOT EXISTS phone_numbers(
                    id SERIAL PRIMARY KEY,
                    fio VARCHAR(128),
                    phone_number BIGINT
                );

                CREATE TABLE IF NOT EXISTS parents(
                    id SERIAL PRIMARY KEY,
                    first_parent INT REFERENCES phone_numbers(id),
                    second_parent INT REFERENCES phone_numbers(id)
                );

                CREATE TABLE IF NOT EXISTS groups(
                    id SERIAL PRIMARY KEY,
                    group_title VARCHAR(32),
                    group_faculty INT REFERENCES faculties(id),
                    group_specialty INT REFERENCES specialties(id)
                );

                CREATE TABLE IF NOT EXISTS lecturers(
                    id SERIAL PRIMARY KEY,
                    fio VARCHAR(128)
                );

                CREATE TABLE IF NOT EXISTS lecturer_faculties(
                    lecturer_id INT REFERENCES lecturers(id),
                    faculty_id INT REFERENCES faculties(id)
                );

                CREATE TABLE IF NOT EXISTS disciplines(
                    id SERIAL PRIMARY KEY,
                    discipline_title VARCHAR(64)
                );

                CREATE TABLE IF NOT EXISTS statements(
                    id SERIAL PRIMARY KEY,
                    statement_number INT,
                    discipline_id INT REFERENCES disciplines(id),
                    group_id INT REFERENCES groups(id)
                );

                CREATE TABLE IF NOT EXISTS assessments(
                    id SERIAL PRIMARY KEY,
                    assessment_title VARCHAR(32)
                );

                CREATE TABLE IF NOT EXISTS students(
                    id SERIAL PRIMARY KEY,
                    fio VARCHAR(128),
                    gender VARCHAR(3),
                    birth_date TIMESTAMP,
                    city_id INT REFERENCES cities(id),
                    phone_number_id INT REFERENCES phone_numbers(id),
                    group_id INT REFERENCES groups(id),
                    faculty_id INT REFERENCES faculties(id),
                    specialty_id INT REFERENCES specialties(id),
                    parents_id INT REFERENCES parents(id)
                );
                
                CREATE TABLE IF NOT EXISTS exams(
                    id SERIAL PRIMARY KEY,
                    statement_id INT REFERENCES statements(id),
                    student_id INT REFERENCES students(id),
                    lecturer_id INT REFERENCES lecturers(id),
                    assessment_id INT REFERENCES assessments(id),
                    exam_date TIMESTAMP,
                    due_date TIMESTAMP
                );
                """

VALUES_TABLES = {
    'specialties': ['specialty_code', 'specialty_title'],
    'faculties': ['faculty_abbreviation', 'faculty_title'],
    'regions': ['region_code', 'region_title'],
    'cities': ['region_id', 'city_title'],
    'phone_numbers': ['fio', 'phone_number'],
    'parents': ['first_parent', 'second_parent'],
    'groups': ['group_title', 'group_faculty', 'group_specialty'],
    'lecturers': ['fio'],
    'lecturer_faculties': ['lecturer_id', 'faculty_id'],
    'disciplines': ['discipline_title'],
    'statements': ['statement_number', 'discipline_id', 'group_id'],
    'assessments': ['assessment_title'],
    'students': [
        'fio', 'gender', 'birth_date', 'city_id', 'phone_number_id',
        'group_id', 'faculty_id', 'specialty_id', 'parents_id'
    ],
    'exams': [
        'statement_id', 'student_id', 'lecturer_id',
        'assessment_id', 'exam_date', 'due_date'
    ]
}

def INSERT(table):   
    return f"""--sql
            INSERT INTO {table}({', '.join(VALUES_TABLES.get(table))}) VALUES({', '.join([f"${i}" for i in range(1, len(VALUES_TABLES.get(table)) + 1)] )})
            """
            
