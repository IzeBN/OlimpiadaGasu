from environs import Env

from dataclasses import dataclass

from database import Database

@dataclass
class DatabaseConfig:
    dsn: str
    username: str
    password: str
    host: str
    model: Database
    port: int = 5432
    

@dataclass
class Config:
    database: DatabaseConfig


env = Env()
env.read_env('.env')


config = Config(
    database=DatabaseConfig(
        dsn=f'postgresql://{env.str('DATABASE_USERNAME')}:{env.str('DATABASE_PASSWORD')}@{env.str('DATABASE_HOST')}:{env.int('DATABASE_PORT')}/{env.str('DATABASE_NAME')}',
        username=env.str('DATABASE_USERNAME'),
        password=env.str('DATABASE_PASSWORD'),
        host=env.str('DATABASE_HOST'),
        port=env.int('DATABASE_PORT'),
        model=Database(f'postgresql://{env.str('DATABASE_USERNAME')}:{env.str('DATABASE_PASSWORD')}@{env.str('DATABASE_HOST')}:{env.int('DATABASE_PORT')}/{env.str('DATABASE_NAME')}')
    )
)

STUDENTS_INPUT = [
    {
        "full_name": "Петров Денис Платонович",
        "gender": "Муж",
        "birth_date": "2003-02-19",
        "city": "Горно-Алтайск",
        "region": "Республика Алтай",
        "phone": "89139874683",
        "group_title": "512",
        "faculty_short": "ЭЮФ",
        "specialty": "09.03.03 Прикладная информатика",
        "parent1_name": "Петрова Анна Андреевна",
        "parent2_name": "Петров Иван Владимирович",
        "parent1_phone": "89239994573",
        "parent2_phone": "89234876681"
    },
    {
        "full_name": "Курочкина Мирослава Вадимовна",
        "gender": "Жен",
        "birth_date": "2002-08-15",
        "city": "Бийск",
        "region": "Алтайский край",
        "phone": "89647348449",
        "group_title": "512",
        "faculty_short": "ЭЮФ",
        "specialty": "09.03.03 Прикладная информатика",
        "parent1_name": "Курочкина Ирина Владимировна",
        "parent2_name": "",
        "parent1_phone": "89239994582",
        "parent2_phone": "89035588147"
    },
    {
        "full_name": "Иванов Сергей Германович",
        "gender": "Муж",
        "birth_date": "2001-10-14",
        "city": "Бийск",
        "region": "Алтайский край",
        "phone": "89138794631",
        "group_title": "512",
        "faculty_short": "ЭЮФ",
        "specialty": "09.03.03 Прикладная информатика",
        "parent1_name": "",
        "parent2_name": "Иванов Иван Иванович",
        "parent1_phone": "89239994591",
        "parent2_phone": "89376299613"
    },
    {
        "full_name": "Бобров Лев Артёмович",
        "gender": "Муж",
        "birth_date": "2001-06-09",
        "city": "Майма",
        "region": "Республика Алтай",
        "phone": "89609876485",
        "group_title": "512",
        "faculty_short": "ЭЮФ",
        "specialty": "09.03.03 Прикладная информатика",
        "parent1_name": "Боброва Анастасия Сергеевна",
        "parent2_name": "Бобров Вячеслав Владимирович",
        "parent1_phone": "89239994600",
        "parent2_phone": "89447011079"
    },
    {
        "full_name": "Шаповалов Александр Захарович",
        "gender": "Муж",
        "birth_date": "2001-01-20",
        "city": "Кызыл-Озек",
        "region": "Республика Алтай",
        "phone": "89734984659",
        "group_title": "512",
        "faculty_short": "ЭЮФ",
        "specialty": "09.03.03 Прикладная информатика",
        "parent1_name": "Щадоводова Анастасия Евгеньевна",
        "parent2_name": "Щадоводов Сергей Иванович",
        "parent1_phone": "89239994609",
        "parent2_phone": "89517722545"
    },
    {
        "full_name": "Климов Вадим Давидович",
        "gender": "Муж",
        "birth_date": "2002-06-06",
        "city": "Горно-Алтайск",
        "region": "Республика Алтай",
        "phone": "89139894646",
        "group_title": "512",
        "faculty_short": "ЭЮФ",
        "specialty": "09.03.03 Прикладная информатика",
        "parent1_name": "Климова Надежда Андреевна",
        "parent2_name": "Климов Андрей Петрович",
        "parent1_phone": "89239994627",
        "parent2_phone": "89058834401"
    },
    {
        "full_name": "Елисеев Артём Антонович",
        "gender": "Муж",
        "birth_date": "2002-06-06",
        "city": "Кызыл-Озек",
        "region": "Республика Алтай",
        "phone": "89968439694",
        "group_title": "512",
        "faculty_short": "ЭЮФ",
        "specialty": "09.03.03 Прикладная информатика",
        "parent1_name": "Елисеева Вера Сергеевна",
        "parent2_name": "Елисеев Алексей Петрович",
        "parent1_phone": "89239994632",
        "parent2_phone": "89659145477"
    },
    {
        "full_name": "Васильев Богдан Маркович",
        "gender": "Муж",
        "birth_date": "2002-12-16",
        "city": "Горно-Алтайск",
        "region": "Республика Алтай",
        "phone": "89138943486",
        "group_title": "512",
        "faculty_short": "ЭЮФ",
        "specialty": "09.03.03 Прикладная информатика",
        "parent1_name": "Васильева Влада Андреевна",
        "parent2_name": "Васильев Пётр Иванович",
        "parent1_phone": "89239994636",
        "parent2_phone": "89279569493"
    },
    {
        "full_name": "Мальцева Ульяна Александровна",
        "gender": "Жен",
        "birth_date": "2002-12-17",
        "city": "Барнаул",
        "region": "Алтайский край",
        "phone": "89231698467",
        "group_title": "512",
        "faculty_short": "ЭЮФ",
        "specialty": "09.03.03 Прикладная информатика",
        "parent1_name": "Малышева Ксения Артемовна",
        "parent2_name": "",
        "parent1_phone": "89800485684",
        "parent2_phone": ""
    },
    {
        "full_name": "Смирнова Арина Николаевна",
        "gender": "Жен",
        "birth_date": "2002-03-21",
        "city": "Майма",
        "region": "Республика Алтай",
        "phone": "89054893698",
        "group_title": "512",
        "faculty_short": "ЭЮФ",
        "specialty": "09.03.03 Прикладная информатика",
        "parent1_name": "Смирнова Одесса Станиславовна",
        "parent2_name": "Смирнов Сергей Владимирович",
        "parent1_phone": "89239994654",
        "parent2_phone": "89871279875"
    }
]

STATEMENT_INPUT = [
    {"statement_number": "1", "student_name": "Петров Денис Платонович", "group": "512", "faculty": "ЭЮФ", "teacher": "Ермакова С. В.", "subject": "Макроэкономика", "grade": "Отлично", "exam_date": "2025-02-11", "submission_date": "2025-02-11"},
    {"statement_number": "1", "student_name": "Курочкина Мирослава Вадимовна", "group": "512", "faculty": "ЭЮФ", "teacher": "Ермакова С. В.", "subject": "Макроэкономика", "grade": "Отлично", "exam_date": "2025-02-11", "submission_date": "2025-02-11"},
    {"statement_number": "1", "student_name": "Иванов Сергей Германович", "group": "512", "faculty": "ЭЮФ", "teacher": "Ермакова С. В.", "subject": "Макроэкономика", "grade": "Отлично", "exam_date": "2025-02-11", "submission_date": "2025-02-11"},
    {"statement_number": "1", "student_name": "Бобров Лев Артёмович", "group": "512", "faculty": "ЭЮФ", "teacher": "Ермакова С. В.", "subject": "Макроэкономика", "grade": "Хорошо", "exam_date": "2025-02-11", "submission_date": "2025-02-11"},
    {"statement_number": "1", "student_name": "Шаповалов Александр Захарович", "group": "512", "faculty": "ЭЮФ", "teacher": "Ермакова С. В.", "subject": "Макроэкономика", "grade": "Хорошо", "exam_date": "2025-02-11", "submission_date": "2025-02-11"},
    {"statement_number": "1", "student_name": "Климов Вадим Давидович", "group": "512", "faculty": "ЭЮФ", "teacher": "Ермакова С. В.", "subject": "Макроэкономика", "grade": "Отлично", "exam_date": "2025-02-11", "submission_date": "2025-02-11"},
    {"statement_number": "1", "student_name": "Елисеев Артём Антонович", "group": "512", "faculty": "ЭЮФ", "teacher": "Ермакова С. В.", "subject": "Макроэкономика", "grade": "Отлично", "exam_date": "2025-02-11", "submission_date": "2025-02-11"},
    {"statement_number": "1", "student_name": "Васильев Богдан Маркович", "group": "512", "faculty": "ЭЮФ", "teacher": "Ермакова С. В.", "subject": "Макроэкономика", "grade": "Хорошо", "exam_date": "2025-02-11", "submission_date": "2025-02-11"},
    {"statement_number": "1", "student_name": "Мальцева Ульяна Александровна", "group": "512", "faculty": "ЭЮФ", "teacher": "Ермакова С. В.", "subject": "Макроэкономика", "grade": "Хорошо", "exam_date": "2025-02-11", "submission_date": "2025-02-11"},
    {"statement_number": "1", "student_name": "Смирнова Арина Николаевна", "group": "512", "faculty": "ЭЮФ", "teacher": "Ермакова С. В.", "subject": "Макроэкономика", "grade": "Отлично", "exam_date": "2025-02-11", "submission_date": "2025-02-11"},
    {"statement_number": "8", "student_name": "Петров Денис Платонович", "group": "512", "faculty": "ЭЮФ", "teacher": "Гусева М. М.", "subject": "Информационные системы в экономике", "grade": "Отлично", "exam_date": "2025-02-07", "submission_date": "2025-02-07"},
    {"statement_number": "8", "student_name": "Курочкина Мирослава Вадимовна", "group": "512", "faculty": "ЭЮФ", "teacher": "Гусева М. М.", "subject": "Информационные системы в экономике", "grade": "Хорошо", "exam_date": "2025-02-07", "submission_date": "2025-02-07"},
    {"statement_number": "8", "student_name": "Иванов Сергей Германович", "group": "512", "faculty": "ЭЮФ", "teacher": "Гусева М. М.", "subject": "Информационные системы в экономике", "grade": "Удовлетворительно", "exam_date": "2025-02-07", "submission_date": "2025-02-07"},
    {"statement_number": "8", "student_name": "Бобров Лев Артёмович", "group": "512", "faculty": "ЭЮФ", "teacher": "Гусева М. М.", "subject": "Информационные системы в экономике", "grade": "Хорошо", "exam_date": "2025-02-07", "submission_date": "2025-02-07"},
    {"statement_number": "8", "student_name": "Шаповалов Александр Захарович", "group": "512", "faculty": "ЭЮФ", "teacher": "Гусева М. М.", "subject": "Информационные системы в экономике", "grade": "Не сдал", "exam_date": "2025-02-07", "submission_date": "2025-03-09"},
    {"statement_number": "8", "student_name": "Климов Вадим Давидович", "group": "512", "faculty": "ЭЮФ", "teacher": "Гусева М. М.", "subject": "Информационные системы в экономике", "grade": "Отлично", "exam_date": "2025-02-07", "submission_date": "2025-02-07"},
    {"statement_number": "8", "student_name": "Елисеев Артём Антонович", "group": "512", "faculty": "ЭЮФ", "teacher": "Гусева М. М.", "subject": "Информационные системы в экономике", "grade": "Отлично", "exam_date": "2025-02-07", "submission_date": "2025-02-07"},
    {"statement_number": "8", "student_name": "Васильев Богдан Маркович", "group": "512", "faculty": "ЭЮФ", "teacher": "Гусева М. М.", "subject": "Информационные системы в экономике", "grade": "Хорошо", "exam_date": "2025-02-07", "submission_date": "2025-02-07"},
    {"statement_number": "8", "student_name": "Мальцева Ульяна Александровна", "group": "512", "faculty": "ЭЮФ", "teacher": "Гусева М. М.", "subject": "Информационные системы в экономике", "grade": "Хорошо", "exam_date": "2025-02-07", "submission_date": "2025-02-07"},
    {"statement_number": "8", "student_name": "Смирнова Арина Николаевна", "group": "512", "faculty": "ЭЮФ", "teacher": "Гусева М. М.", "subject": "Информационные системы в экономике", "grade": "Отлично", "exam_date": "2025-02-07", "submission_date": "2025-02-07"},
    {"statement_number": "11", "student_name": "Петров Денис Платонович", "group": "512", "faculty": "ЭЮФ", "teacher": "Леонова А. Р.", "subject": "Программирование в 1С", "grade": "Отлично", "exam_date": "2025-01-28", "submission_date": "2025-01-28"},
    {"statement_number": "11", "student_name": "Курочкина Мирослава Вадимовна", "group": "512", "faculty": "ЭЮФ", "teacher": "Леонова А. Р.", "subject": "Программирование в 1С", "grade": "Отлично", "exam_date": "2025-01-28", "submission_date": "2025-01-28"},
    {"statement_number": "11", "student_name": "Иванов Сергей Германович", "group": "512", "faculty": "ЭЮФ", "teacher": "Леонова А. Р.", "subject": "Программирование в 1С", "grade": "Хорошо", "exam_date": "2025-01-28", "submission_date": "2025-01-28"},
    {"statement_number": "11", "student_name": "Бобров Лев Артёмович", "group": "512", "faculty": "ЭЮФ", "teacher": "Леонова А. Р.", "subject": "Программирование в 1С", "grade": "Отлично", "exam_date": "2025-01-28", "submission_date": "2025-01-28"},
    {"statement_number": "11", "student_name": "Шаповалов Александр Захарович", "group": "512", "faculty": "ЭЮФ", "teacher": "Леонова А. Р.", "subject": "Программирование в 1С", "grade": "Не сдал", "exam_date": "2025-01-28", "submission_date": "2025-01-28"},
    {"statement_number": "11", "student_name": "Климов Вадим Давидович", "group": "512", "faculty": "ЭЮФ", "teacher": "Леонова А. Р.", "subject": "Программирование в 1С", "grade": "Отлично", "exam_date": "2025-01-28", "submission_date": "2025-01-28"},
    {"statement_number": "11", "student_name": "Елисеев Артём Антонович", "group": "512", "faculty": "ЭЮФ", "teacher": "Леонова А. Р.", "subject": "Программирование в 1С", "grade": "Удовлетворительно", "exam_date": "2025-01-28", "submission_date": "2025-01-28"},
    {"statement_number": "11", "student_name": "Васильев Богдан Маркович", "group": "512", "faculty": "ЭЮФ", "teacher": "Леонова А. Р.", "subject": "Программирование в 1С", "grade": "Хорошо", "exam_date": "2025-01-28", "submission_date": "2025-01-28"},
    {"statement_number": "11", "student_name": "Мальцева Ульяна Александровна", "group": "512", "faculty": "ЭЮФ", "teacher": "Леонова А. Р.", "subject": "Программирование в 1С", "grade": "Отлично", "exam_date": "2025-01-28", "submission_date": "2025-01-28"},
    {"statement_number": "11", "student_name": "Смирнова Арина Николаевна", "group": "512", "faculty": "ЭЮФ", "teacher": "Леонова А. Р.", "subject": "Программирование в 1С", "grade": "Хорошо", "exam_date": "2025-01-28", "submission_date": "2025-01-28"},
    {"statement_number": "12", "student_name": "Петров Денис Платонович", "group": "512", "faculty": "ЭЮФ", "teacher": "Ермакова С. В.", "subject": "Эконометрика", "grade": "Отлично", "exam_date": "2025-02-02", "submission_date": "2025-02-02"},
    {"statement_number": "12", "student_name": "Курочкина Мирослава Вадимовна", "group": "512", "faculty": "ЭЮФ", "teacher": "Ермакова С. В.", "subject": "Эконометрика", "grade": "Отлично", "exam_date": "2025-02-02", "submission_date": "2025-02-02"},
    {"statement_number": "12", "student_name": "Иванов Сергей Германович", "group": "512", "faculty": "ЭЮФ", "teacher": "Ермакова С. В.", "subject": "Эконометрика", "grade": "Отлично", "exam_date": "2025-02-02", "submission_date": "2025-02-02"},
    {"statement_number": "12", "student_name": "Бобров Лев Артёмович", "group": "512", "faculty": "ЭЮФ", "teacher": "Ермакова С. В.", "subject": "Эконометрика", "grade": "Отлично", "exam_date": "2025-02-02", "submission_date": "2025-02-02"},
    {"statement_number": "12", "student_name": "Шаповалов Александр Захарович", "group": "512", "faculty": "ЭЮФ", "teacher": "Ермакова С. В.", "subject": "Эконометрика", "grade": "Не сдал", "exam_date": "2025-02-02", "submission_date": "2025-02-02"},
    {"statement_number": "12", "student_name": "Климов Вадим Давидович", "group": "512", "faculty": "ЭЮФ", "teacher": "Ермакова С. В.", "subject": "Эконометрика", "grade": "Хорошо", "exam_date": "2025-02-02", "submission_date": "2025-02-02"},
    {"statement_number": "12", "student_name": "Елисеев Артём Антонович", "group": "512", "faculty": "ЭЮФ", "teacher": "Ермакова С. В.", "subject": "Эконометрика", "grade": "Хорошо", "exam_date": "2025-02-02", "submission_date": "2025-02-02"},
    {"statement_number": "12", "student_name": "Васильев Богдан Маркович", "group": "512", "faculty": "ЭЮФ", "teacher": "Ермакова С. В.", "subject": "Эконометрика", "grade": "Не сдал", "exam_date": "2025-02-02", "submission_date": "2025-02-02"},
    {"statement_number": "12", "student_name": "Мальцева Ульяна Александровна", "group": "512", "faculty": "ЭЮФ", "teacher": "Ермакова С. В.", "subject": "Эконометрика", "grade": "Отлично", "exam_date": "2025-02-02", "submission_date": "2025-02-02"},
    {"statement_number": "12", "student_name": "Смирнова Арина Николаевна", "group": "512", "faculty": "ЭЮФ", "teacher": "Ермакова С. В.", "subject": "Эконометрика", "grade": "Хорошо", "exam_date": "2025-02-02", "submission_date": "2025-02-02"}
]