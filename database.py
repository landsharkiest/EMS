import sqlite3
conn = sqlite3.connect('employee_management.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS departments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS employees (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT NOT NULL,
               email TEXT UNIQUE NOT NULL,
               position TEXT,
               department_id INTEGER,
               hire_date DATE,
               salary REAL,
               FOREIGN KEY (department_id) REFERENCES departments(id)
)
''')

cursor.execute('''
               INSERT INTO departments (name) VALUES ('Engineering'), ('HR'), ('Sales')
               ''')

cursor.execute('''
               INSERT INTO employees (name, email, position, department_id, hire_date, salary)
               VALUES ('Owen Kirchenstien', 'owenkirchenstien@gmail.com', 'Software Engineer', 1, '2024-10-17', 120000)
               ''')

conn.commit()
