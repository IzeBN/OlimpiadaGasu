import asyncpg as sq

from database.utils import q, t

class Database:
    
    def __init__(self, dsn) -> None:
        self.dsn = dsn
        self.__isConnection = False
        
    async def __connect(self):
        self.db = await sq.create_pool(
            dsn=self.dsn,
            min_size=50,
            max_size=100
        )
        self.__isConnection = True
        
    def databaseCheckConection(method: function):
        async def wrapper(self, *args, **kwargs):
            if not self.__isConnection:
                await self.__connect()
            try:
                return await method(self, *args, **kwargs) 
            except Exception as e:
                print(f'{method.__name__} | {e}')
        return wrapper
    
    @databaseCheckConection
    async def create_tables(self):
        async with self.db.acquire() as conn:
            async with conn.transaction():
                await conn.execute(q.CREATE_TABLES)


    @databaseCheckConection
    async def add_specialty(self, specialty_code, specialty_title):
        async with self.db.acquire() as conn:
            id = await conn.fetchval("""--sql
                                       SELECT * FROM specialties WHERE specialty_code = $1""",
                                       specialty_code)
            if not id:
                async with conn.transaction():
                    id = await conn.fetchval(q.INSERT('specialties') + 'RETURNING id',
                                         specialty_code, specialty_title)

            return id
        
    @databaseCheckConection
    async def add_faculty(self, faculty_abbrev, faculty_title):
        async with self.db.acquire() as conn:
            id = await conn.fetchval("""--sql
                                     SELECT * FROM faculties WHERE faculty_abbreviation = $1""",
                                     faculty_abbrev)
            if not id:
                async with conn.transaction():
                    id = await conn.fetchval(q.INSERT('faculties') + 'RETURNING id',
                                             faculty_abbrev, faculty_title)
            return id
        
    @databaseCheckConection
    async def add_region(self, region_code, region_title):
        async with self.db.acquire() as conn:
            id = await conn.fetchval("""--sql
                                     SELECT id FROM regions WHERE region_title = $1""",
                                     region_title)
            if not id:
                async with conn.transaction():
                    id = await conn.fetchval(q.INSERT('regions') + 'RETURNING id',
                                             region_code, region_title)
                    
            return id
    @databaseCheckConection
    async def add_city(self, city_title, region_code, region_title):
        async with self.db.acquire() as conn:
            region_id = await self.add_region(region_code, region_title)
            city_id = await conn.fetchval("""--sql
                                          SELECT id FROM cities WHERE region_id = $1 AND city_title = $2""",
                                          region_id, city_title)
            if not city_id:
                async with conn.transaction():
                    city_id = await conn.fetchval(q.INSERT('cities') + 'RETURNING id',
                                             region_id, city_title)
        
            return city_id
        
    @databaseCheckConection
    async def add_phone_number(self, fio, phone_number: str | int):
        if not str(phone_number).isdigit(): return
        async with self.db.acquire() as conn:
            id = await conn.fetchval("""--sql
                                     SELECT id FROM phone_numbers WHERE phone_number = $1""",
                                     phone_number)
            if not id:
                async with conn.transaction():
                    id = await conn.fetchval(q.INSERT('phone_numbers') + 'RETURNING id',
                                             fio, phone_number)
            return id
    @databaseCheckConection
    async def add_parents(self, first_parent_id, second_parent_id):
        async with self.db.acquire() as conn:
            params, query = [], """SELECT id FROM parents WHERE """
            if not first_parent_id and second_parent_id:
                query += """first_parent IS NULL AND second_parent = $1"""
                params.append(second_parent_id)
            elif not second_parent_id and first_parent_id:
                query += """first_parent = $1 AND second_parent IS NULL"""
                params.append(first_parent_id)
            else:
                query += """first_parent = $1 AND second_parent = $2"""
                params = [first_parent_id, second_parent_id]
            id = await conn.fetchval(query, *params)
            if not id:
                async with conn.transaction():
                    id = await conn.fetchval(q.INSERT('parents') + "RETURNING id", 
                                             first_parent_id, second_parent_id)
            return id
        
        
    @databaseCheckConection
    async def add_group(self, group_title, group_faculty, group_specialty):
        async with self.db.acquire() as conn:
            id = await conn.fetchval("""--sql
                                     SELECT id FROM groups WHERE group_title = $1""",
                                     group_title)
            if not id:
                async with conn.transaction():
                    id = await conn.fetchval(q.INSERT('groups') + "RETURNING id", 
                                             group_title, group_faculty,
                                               group_specialty)
            return id
        
    @databaseCheckConection
    async def add_lecturer(self, fio):
        async with self.db.acquire() as conn:
            id = await conn.fetchval("""--sql
                                     SELECT id FROM lecturers WHERE fio = $1""",
                                     fio)
            if not id:
                async with conn.transaction():
                    id = await conn.fetchval(q.INSERT('lecturers') + 'RETURNING id',
                                             fio)
                    
            return id
        
    @databaseCheckConection
    async def add_lecturer_faculty(self, lecturer_id, faculty_id):
        async with self.db.acquire() as conn:
            last = await conn.fetchrow("""--sql
                                       SELECT * FROM lecturer_faculties WHERE lecturer_id = $1 AND faculty_id = $2""",
                                       lecturer_id, faculty_id)
            if not last:
                async with conn.transaction():
                    await conn.execute(q.INSERT('lecturer_faculties'),
                                       lecturer_id, faculty_id)
                    
    @databaseCheckConection
    async def add_discipline(self, discipline_title):
        async with self.db.acquire() as conn:
            id = await conn.fetchval("""--sql
                                     SELECT id FROM disciplines WHERE discipline_title = $1""",
                                     discipline_title)
            if not id:
                async with conn.transaction():
                    id = await conn.fetchval(q.INSERT('disciplines') + "RETURNING id",
                                             discipline_title)
                    
            return id
        
    @databaseCheckConection
    async def add_statement(self, statement_number, discipline_id, group_id):
        async with self.db.acquire() as conn:
            id = await conn.fetchval("""--sql
                                       SELECT id FROM statements WHERE statement_number = $1""",
                                       statement_number)
            if not id:
                async with conn.transaction():
                    id = await conn.fetchval(q.INSERT('statements') + " RETURNING id", 
                                       statement_number, discipline_id,
                                       group_id)
            return id
    @databaseCheckConection
    async def add_assessment(self, assessment_title):
        async with self.db.acquire() as conn:
            id = await conn.fetchval("""--sql
                                     SELECT id FROM assessments WHERE assessment_title = $1""",
                                     assessment_title)
            async with conn.transaction():
                id = await conn.fetchval(q.INSERT('assessments') + ' RETURNING id',
                                         assessment_title)
                
        return id
    
    @databaseCheckConection
    async def add_student(self, fio, gender, birth_date, city_id, phone_number_id, group_id, faculty_id, specialty_id, parents_id):
        async with self.db.acquire() as conn:
            params = [fio, group_id]
            if not phone_number_id is None:  params.append(phone_number_id)
            id = await conn.fetchval(f"""--sql
                                     SELECT id FROM students WHERE fio = $1 AND group_id = $2 AND phone_number_id {'IS NULL' if not phone_number_id else "= $3"}""",
                                     *params)
            if not id:
                async with conn.transaction():
                    id = await conn.fetchval(q.INSERT('students') + 'RETURNING id',
                                             fio, gender, birth_date, city_id, phone_number_id,
                                             group_id, faculty_id, specialty_id, parents_id)
            
            return id
        
    @databaseCheckConection
    async def add_exam(self, statement_id, student_id, lecturer_id, assessment_id, exam_date, due_date):
        async with self.db.acquire() as conn:
            last = await conn.fetchrow("""--sql
                                       SELECT * FROM exams WHERE statement_id = $1 AND student_id = $2 AND lecturer_id = $3""",
                                       statement_id, student_id, lecturer_id)
            if not last:
                async with conn.transaction():
                    await conn.execute(q.INSERT('exams'), statement_id, student_id,
                                       lecturer_id, assessment_id, exam_date, due_date)
                    
    @databaseCheckConection
    async def find_group_by_title(self, title):
        async with self.db.acquire() as conn:
            group = await conn.fetchrow("""--sql
                                        SELECT * FROM groups WHERE group_title = $1""",
                                        title)
            return None if not group else t.Group(*group)
                

    @databaseCheckConection
    async def select_table(self, table):
        async with self.db.acquire() as conn:
            rows = await conn.fetch(f"SELECT * FROM {table}")
            return [dict(row) for row in rows]

                
                
                
                


                