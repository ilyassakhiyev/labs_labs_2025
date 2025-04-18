import psycopg2
from psycopg2 import sql

conn = psycopg2.connect(
    dbname="data_base",  
    user="postgres",   
    password="jas0mykr555",  
    host="localhost",          
)

cursor = conn.cursor()

create_table_query = """
CREATE TABLE IF NOT EXISTS basetry (
    User_ID SERIAL PRIMARY KEY,
    User_name VARCHAR(100) NOT NULL,
    numb INT DEFAULT 0
);
"""
cursor.execute(create_table_query)

conn.commit()

cursor.close()
conn.close()

print("done")