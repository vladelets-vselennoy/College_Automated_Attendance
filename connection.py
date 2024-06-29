# import psycopg2
# from config import DB_PARAMS

# def get_db_connection():
#     return psycopg2.connect(**DB_PARAMS)


from sqlalchemy import create_engine
from config import DB_PARAMS

def get_db_connection():
    db_url = f"postgresql://{DB_PARAMS['user']}:{DB_PARAMS['password']}@{DB_PARAMS['host']}/{DB_PARAMS['dbname']}"
    return create_engine(db_url)