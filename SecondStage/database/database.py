import asyncpg as sq

from database.utils import q, t

class Database:
    def __init__(self, dsn):
        self.dsn = dsn
        self.isConnect = False
        
    async def __connect(self):
        self.db = await sq.create_pool(
            self.dsn,
            min_size=50,
            max_size=100
        )
        
    def databaseCheckConnection(method):
        async def wrapper(self, *args, **kwargs):
            if not self.isConnect:
                await self.__connect()
                self.isConnect = True
            try:
                return await method(self, *args, **kwargs)
            except Exception as e:
                print(f'{method.__name__} | {e}')
                
        return wrapper
    
    
    @databaseCheckConnection
    async def create_tables(self):
        async with self.db.acquire() as conn:
            async with conn.transaction():
                await conn.execute(q.CREATE_TABLES)
                
                
    @databaseCheckConnection
    async def select_table(self, table): 
        async with self.db.acquire() as conn:
            rows = await conn.fetch(f"""--sql
                                    SELECT * FROM {table}""")    
            return [dict(row) for row in rows]
        
        
    @databaseCheckConnection
    async def insert_to_table(self, table, *args):
        async with self.db.acquire() as conn:
            async with conn.transaction():
                await conn.execute(q.INSERT(table), *args)
                
    @databaseCheckConnection
    async def add_discipline(self, discipline_title):
        async with self.db.acquire() as conn:
            id = await conn.fetchval("""--sql
                                     SELECT id FROM disciplines WHERE discipline_title = $1""", discipline_title)
            if not id:
                async with conn.transaction():
                    id = await conn.fetchval(q.INSERT('disciplines') + "RETURNING id",
                                             discipline_title)
                    
            return id
        
    @databaseCheckConnection
    async def add_teacher(self, fio):
        async with self.db.acquire() as conn:
            id = await conn.fetchval("""--sql
                                     SELECT id FROM teachers WHERE fio = $1""", fio)
            if not id:
                async with conn.transaction():
                    id = await conn.fetchval(q.INSERT('teachers') + 'RETURNING id',
                                             fio)
                    
            return id
        

    @databaseCheckConnection
    async def add_faculty(self, faculty_title):
        async with self.db.acquire() as conn:
            id = await conn.fetchval("""--sql
                                     SELECT id FROM faculties WHERE faculty_title = $1""",
                                     faculty_title)
            if not id:
                async with conn.transaction():
                    id = await conn.fetchval(q.INSERT('faculties') + "RETURNING id",
                                             faculty_title)
            return id
        
    @databaseCheckConnection
    async def add_region(self, region_title, region_number):
        async with self.db.acquire() as conn:
            id = await conn.fetchval("""--sql
                                     SELECT id FROM regions WHERE region_title = $1""",
                                     region_title)
            if not id:
                async with conn.transaction():
                    id = await conn.fetchval(q.INSERT('regions') + 'RETURNING id',
                                             region_title, region_number)
                    
            return id
    
    @databaseCheckConnection
    async def add_town(self, town_title, region_title, region_number):
        async with self.db.acquire() as conn:
            region_id = await self.add_region(region_title, region_number)
            id = await conn.fetchval("""--sql
                                     SELECT id FROM towns WHERE town_title = $1 AND region_id = $2""",
                                     town_title, region_id)
            if not id:
                async with conn.transaction():
                    id = await conn.fetchval(q.INSERT('towns') + " RETURNING id",
                                             town_title, region_id)
            
        return id
        
    @databaseCheckConnection
    async def add_specialty(self, specialty_title, faculty_id):
        async with self.db.acquire() as conn:
            id = await conn.fetchval("""--sql
                                     SELECT id FROM specialties WHERE specialty_title = $1 AND faculty_id = $2""",
                                     specialty_title, faculty_id)
            if not id:
                async with conn.transaction():
                    id = await conn.fetchval(q.INSERT('specialties') + "RETURNING id",
                                             specialty_title, faculty_id)
                    
            return id
        
    @databaseCheckConnection
    async def add_group(self, group_title, specialty_id):
        async with self.db.acquire() as conn:
            id = await conn.fetchval("""--sql
                                     SELECT id FROM groups WHERE group_title = $1 AND specialty_id = $2""",
                                     group_title, specialty_id)
            if not id:
                async with conn.transaction():
                    id = await conn.fetchval(q.INSERT('groups') + 'RETURNING id',
                                             group_title, specialty_id)
            return id
        
    @databaseCheckConnection
    async def add_phone_number(self, phone_number):
        async with self.db.acquire() as conn:
            id = await conn.fetchval("""--sql
                                     SELECT id FROM phone_numbers WHERE phone_number = $1""",
                                     phone_number)
            if not id:
                async with conn.transaction():
                    id = await conn.fetchval(q.INSERT('phone_numbers') + "RETURNING id",
                                             phone_number)
            return id
        
    @databaseCheckConnection
    async def add_parents(self, parent_name, gender_parent, birth_date, town_id):
        async with self.db.acquire() as conn:
            id = await conn.fetchval("""--sql
                                     SELECT id FROM parents WHERE parent_name = $1 AND town_id = $2""",
                                     parent_name, town_id)
            if not id:
                async with conn.transaction():
                    id = await conn.fetchval(q.INSERT('parents') + "RETURNING id",
                                             parent_name, gender_parent, birth_date, town_id)
                    
            return id


    @databaseCheckConnection
    async def add_statement(self, date_statement, num_statement, group_id, discipline_id, teacher_id):
        async with self.db.acquire() as conn:
            id = await conn.fetchval("""--sql
                                     SELECT id FROM statements WHERE num_statement = $1""",
                                     num_statement)
            if not id:
                async with conn.transaction():
                    id = await conn.fetchval(q.INSERT('statements') + "RETURNING id",
                                             date_statement, num_statement, group_id,
                                             discipline_id, teacher_id)
            return id
        
    @databaseCheckConnection
    async def add_student(self, fio, gender, birth_date, town_id, group_id):
        async with self.db.acquire() as conn:
            id = await conn.fetchval("""--sql
                                     SELECT id FROM students WHERE fio = $1 AND town_id = $2 AND group_id = $3""",
                                     fio, town_id, group_id)
            if not id:
                async with conn.transaction():
                    id = await conn.fetchval(q.INSERT('students') + "RETURNING id",
                                             fio, gender, birth_date, town_id, group_id)
                    
            return id
        
    @databaseCheckConnection
    async def add_student_parent(self, student_id, parent_id):
        async with self.db.acquire() as conn:
            id = await conn.fetchval("""--sql
                                     SELECT id FROM student_parents WHERE student_id = $1 AND parent_id = $2""",
                                     student_id, parent_id)
            if not id:
                async with conn.transaction():
                    id = await conn.fetchval(q.INSERT('student_parents') + 'RETURNING id',
                                             student_id, parent_id)
                    
            return id
        
    @databaseCheckConnection
    async def add_phone_number_student(self, phone_id, student_id):
        async with self.db.acquire() as conn:
            id = await conn.fetchval("""--sql
                                     SELECT id FROM phone_number_students WHERE phone_id = $1 AND student_id = $2""",
                                     phone_id, student_id)
            if not id:
                async with conn.transaction():
                    id = await conn.fetchval(q.INSERT('phone_number_students') + "RETURNING id",
                                             phone_id, student_id)
                    
            return id
    
    @databaseCheckConnection
    async def add_phone_number_parent(self, phone_id, parent_id):
        async with self.db.acquire() as conn:
            id = await conn.fetchval("""--sql
                                     SELECT id FROM phone_number_parents WHERE phone_id = $1 AND parent_id = $2""",
                                     phone_id, parent_id)
            if not id:
                async with conn.transaction():
                    id = await conn.fetchval(q.INSERT('phone_number_parents') + "RETURNING id",
                                             phone_id, parent_id)
                    
            return id
                
    @databaseCheckConnection
    async def add_grade(self, due_date, student_id, statement_id, grade):
        async with self.db.acquire() as conn:
            id = await conn.fetchval("""--sql
                                     SELECT id FROM grades WHERE student_id = $1 AND statement_id = $2""",
                                     student_id, statement_id)
            async with conn.transaction():
                id = await conn.fetchval(q.INSERT('grades') + "RETURNING id",
                                         due_date, student_id, statement_id, grade)
                
            return id
                
    @databaseCheckConnection
    async def get_otchet_data(self):
        async with self.db.acquire() as conn:
            rows = await conn.fetch(q.GET_OTCHET)
            return [dict(row) for row in rows]
            
                
    
    