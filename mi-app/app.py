from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)

# Función para conectar con la base de datos
def connect_db():
    return sqlite3.connect('database.db')

# Ruta para consultar todos los registros
@app.route('/')
def index():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM records")
    results = cursor.fetchall()
    conn.close()
    return render_template('index.html', records=results)

# Ruta para consultar un registro por ID
@app.route('/record/<int:id>', methods=['GET'])
def get_record(id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM records WHERE id=?", (id,))
    result = cursor.fetchone()
    conn.close()
    return jsonify(result)

# Ruta para agregar un registro
@app.route('/add', methods=['POST'])
def add_record():
    data = request.form
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO records (name, value) VALUES (?, ?)", (data['name'], data['value']))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Registro agregado exitosamente'})

# Ruta para editar un registro
@app.route('/edit/<int:id>', methods=['POST'])
def update_record(id):
    data = request.form
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE records SET name=?, value=? WHERE id=?", (data['name'], data['value'], id))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Registro actualizado exitosamente'})

# Ruta para eliminar un registro
@app.route('/delete/<int:id>', methods=['POST'])
def delete_record(id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM records WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Registro eliminado exitosamente'})

if __name__ == '__main__':
    app.run(debug=True)
