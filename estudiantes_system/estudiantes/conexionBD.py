from importlib import import_module

try:
    mysql_connector = import_module("mysql.connector")

except ImportError:
    print("Instala la librería con: pip install mysql-connector-python")

else:
    try:
        conexion = mysql_connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="bd_estudiantes"
        )

        cursor = conexion.cursor(buffered=True)

        print("Conexión exitosa a la base de datos.")

        cursor.execute("SELECT * FROM estudiantes")

        registros = cursor.fetchall()

        for registro in registros:
            print(registro)

    except mysql_connector.Error as err:
        print(f"Error al conectar o consultar la base de datos: {err}")

    finally:
        if "conexion" in locals() and conexion.is_connected():
            cursor.close()
            conexion.close()