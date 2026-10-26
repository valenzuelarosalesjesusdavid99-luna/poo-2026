
from conexionBD import Conexion, cursor

class CocheBD:
    def __init__(self, marca, color, modelo, velocidad, potencia, asientos):
        self._marca = marca
        self._color = color
        self._modelo = modelo
        self._velocidad = velocidad
        self._potencia = potencia
        self._asientos = asientos

    def insertar(self):
        try:
            sql = """
                INSERT INTO coches
                (marca, color, modelo, velocidad, potencia, asientos)
                VALUES (%s, %s, %s, %s, %s, %s)
            """

            valores = (
                self._marca,
                self._color,
                self._modelo,
                self._velocidad,
                self._potencia,
                self._asientos
            )

            cursor.execute(sql, valores)
            Conexion.commit()

            return True

        except Exception as e:
            print("Error al insertar el coche:", e)
            return False

    def consultar(self):
        try:
            cursor.execute("SELECT * FROM coches WHERE marca = %s AND modelo = %s", (self._marca, self._modelo))
            return cursor.fetchone()
        except Exception as e:
            print("Error al consultar el coche:", e)
            return None

    def eliminar(self):
        try: 
            cursor.execute("DELETE FROM coches WHERE marca = %s AND modelo = %s", (self._marca, self._modelo))
            Conexion.commit()
            return True
        except Exception as e:
            print("Error al eliminar el coche:", e)
            return False

    def actualizar(self):
        try:
            cursor.execute("UPDATE coches SET color = %s, velocidad = %s, potencia = %s, asientos = %s WHERE marca = %s AND modelo = %s",
                           (self._color, self._velocidad, self._potencia, self._asientos, self._marca, self._modelo))
            Conexion.commit()
            return True
        except Exception as e:
            print("Error al actualizar el coche:", e)
            return False
        
        

