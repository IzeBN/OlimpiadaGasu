from environs import Env

from dataclasses import dataclass

from database import Database


env = Env()
env.read_env('.env')

@dataclass
class DatabaseConfig:
    model: Database
    username: str
    password: str
    host: str
    port: int = 5432
    
@dataclass
class Config:
    database: DatabaseConfig
    
    

config = Config(
    database=DatabaseConfig(
        username=env.str('DATABASE_USERNAME'),
        password=env.str('DATABASE_PASSWORD'),
        host=env.str('DATABASE_HOST'),
        port=env.int('DATABASE_PORT'),
        model=Database(f'postgresql://{env.str('DATABASE_USERNAME')}:{env.str('DATABASE_PASSWORD')}@{env.str('DATABASE_HOST')}:{env.int('DATABASE_PORT')}/{env.str('DATABASE_NAME')}')
    )
)


