import pymysql

conn = pymysql.connect(host="127.0.0.1", port=3308, user="root", password="", db="db1")

# Cursor funciona para hacer consultas
consulta = conn.cursor()

# Ejecuta mi consulta
consulta.execute("SELECT * FROM articulos")

# Recorremos la tabla e imprimimos los datos
for id,descripcion,precio in consulta.fetchall():
    print(id,descripcion,precio)

conn.close()

