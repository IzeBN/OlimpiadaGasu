


CREATE_TABLES = """--sql
                CREATE TABLE IF NOT EXISTS disciplines(
                    id SERIAL PRIMARY KEY,
                    discipline_title VARCHAR(64)
                );
                
                CREATE TABLE IF NOT EXISTS teachers(
                    id SERIAL PRIMARY KEY,
                    fio VARCHAR(128)
                );
                
                CREATE TABLE IF NOT EXISTS faculties(
                    id SERIAL PRIMARY KEY,
                    faculty_title VARCHAR(128)
                );
                
                CREATE TABLE IF NOT EXISTS regions(
                    id SERIAL PRIMARY KEY,
                    region_title VARCHAR(64),
                    region_number INT
                );
                
                CREATE TABLE IF NOT EXISTS towns(
                    id SERIAL PRIMARY KEY,
                    town_title VARCHAR(64),
                    region_id INT REFERENCES regions(id)
                );
                
                CREATE TABLE IF NOT EXISTS specialties(
                    id SERIAL PRIMARY KEY,
                    specialty_title VARCHAR(128),
                    faculty_id INT REFERENCES faculties(id)
                );
                
                CREATE TABLE IF NOT EXISTS groups(
                    id SERIAL PRIMARY KEY,
                    group_title VARCHAR(32),
                    specialty_id INT REFERENCES specialties(id)
                );
                
                CREATE TABLE IF NOT EXISTS phone_numbers(
                    id SERIAL PRIMARY KEY,
                    phone_number VARCHAR(32)
                );
                
                CREATE TABLE IF NOT EXISTS parents(
                    id SERIAL PRIMARY KEY,
                    parent_name VARCHAR(64),
                    gender_parent VARCHAR(12),
                    birth_date TIMESTAMP,
                    town_id INT REFERENCES towns(id)
                );
                
                CREATE TABLE IF NOT EXISTS statements(
                    id SERIAL PRIMARY KEY,
                    date_statement TIMESTAMP,
                    num_statement INT,
                    group_id INT REFERENCES groups(id),
                    discipline_id INT REFERENCES disciplines(id),
                    teacher_id INT REFERENCES teachers(id)
                );
                
                CREATE TABLE IF NOT EXISTS students(
                    id SERIAL PRIMARY KEY,
                    fio VARCHAR(128),
                    gender VARCHAR(12),
                    birth_date TIMESTAMP,
                    town_id INT REFERENCES towns(id),
                    group_id INT REFERENCES groups(id)
                );
                
                CREATE TABLE IF NOT EXISTS student_parents(
                    id SERIAL PRIMARY KEY,
                    student_id INT REFERENCES students(id),
                    parent_id INT REFERENCES parents(id)
                );
                
                CREATE TABLE IF NOT EXISTS phone_number_students(
                    id SERIAL PRIMARY KEY,
                    phone_id INT REFERENCES phone_numbers(id),
                    student_id INT REFERENCES students(id)
                );
                
                CREATE TABLE IF NOT EXISTS phone_number_parents(
                    id SERIAL PRIMARY KEY,
                    phone_id INT REFERENCES phone_numbers(id),
                    parent_id INT REFERENCES parents(id)
                );
                
                CREATE TABLE IF NOT EXISTS grades(
                    id SERIAL PRIMARY KEY,
                    due_date TIMESTAMP,
                    student_id INT REFERENCES students(id),
                    statement_id INT REFERENCES statements(id),
                    grade VARCHAR(32)
                );
                """
                
TABLE_COLUMNS = {
    "disciplines": ['discipline_title'],
    "teachers": ['fio'],
    "faculties": ['faculty_title'],
    "regions": ['region_title', 'region_number'],
    "towns": ['town_title', 'region_id'],
    "specialties": ['specialty_title', 'faculty_id'],
    "groups": ['group_title', 'specialty_id'],
    "phone_numbers": ['phone_number'],
    "parents": ['parent_name', 'gender_parent', 'birth_date', 'town_id'],
    "statements": ['date_statement', 'num_statement', 'group_id', 'discipline_id', 'teacher_id'],
    "students": ['fio', 'gender', 'birth_date', 'town_id', 'group_id'],
    "student_parents": ['student_id', 'parent_id'],
    "phone_number_students": ['phone_id', 'student_id'],
    "phone_number_parents": ['phone_id', 'parent_id'],
    "grades": ['due_date', 'student_id', 'statement_id', 'grade']
}

def INSERT(table: str):
    return f"""--sql
            INSERT INTO {table}({", ".join(TABLE_COLUMNS[table])}) VALUES({', '.join([f'${i}' for i in range(1, len(TABLE_COLUMNS[table]) + 1)])})
            """
            
            
GET_OTCHET = """--sql
            SELECT
                st.fio,
                st.gender,
                st.birth_date,
                ph.phone_number,
                gr.group_title as group,
                sp.specialty_title as specialty,
                fac.faculty_title as faculty,
                dis.discipline_title as discipline,
                teach.fio,
                statement.num_statement,
                grade.grade
            FROM grades grade
            JOIN students AS st ON st.id = grade.student_id
            JOIN phone_number_students AS ph_st ON ph_st.student_id = st.id
            JOIN phone_numbers AS ph ON ph_st.phone_id = ph.id
            JOIN groups AS gr ON st.group_id = gr.id
            JOIN specialties AS sp ON sp.id = gr.specialty_id
            JOIN faculties AS fac ON fac.id = sp.faculty_id
            JOIN statements AS statement ON statement.id = grade.statement_id
            JOIN disciplines AS dis ON dis.id = statement.discipline_id
            JOIN teachers AS teach ON teach.id = statement.teacher_id   
            """