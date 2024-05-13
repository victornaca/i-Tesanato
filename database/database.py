import sqlite3
from pathlib import Path

def create_database_in_memory():
    conn = sqlite3.connect(":memory:")

    ddl_script_path = Path("database/ddl.sql")
    if ddl_script_path.is_file():
        with open(ddl_script_path, "r") as ddl_file:
            ddl_script = ddl_file.read()
            conn.executescript(ddl_script)
    else:
        print("Script DDL not found.")

    dml_script_path = Path("database/inserts.sql")
    if dml_script_path.is_file():
        with open(dml_script_path, "r") as dml_file:
            dml_script = dml_file.read()
            conn.executescript(dml_script)
    else:
        print("Script DML not found.")
    
    return conn

def get_table_info(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    for table in tables:
        print(f"Table: {table[0]}")
        cursor.execute(f"PRAGMA table_info({table[0]});")
        columns = cursor.fetchall()
        for column in columns:
            print(f"  Column: {column[1]} - Type: {column[2]}")