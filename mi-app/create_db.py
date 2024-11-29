import sqlite3

def create_database():
    # Crear base de datos y tabla
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS records (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        value TEXT NOT NULL
    )
    ''')

    conn.commit()
    conn.close()

    print("Base de datos y tabla creadas con éxito.")

# Ejecutar función si el archivo es ejecutado directamente
if __name__ == '__main__':
    create_database()
