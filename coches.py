
class Coches:

    def __init__(self, color, marca, modelo, velocidad_maxima, potencia, asientos):
        self._color = color
        self._marca = marca
        self._modelo = modelo
        self._velocidad_maxima = velocidad_maxima
        self._velocidad = 0
        self._potencia = potencia
        self._asientos = asientos

    # Método para acelerar
    def acelerar(self, incremento=10):
        if incremento > 0:
            self._velocidad = min(
                self._velocidad + incremento,
                self._velocidad_maxima
            )
            print(
                f"Velocidad del coche {self._marca} {self._modelo} "
                f"tras acelerar: {self._velocidad} km/h"
            )

    # Método para frenar
    def frenar(self, decremento=10):
        if decremento > 0:
            self._velocidad = max(0, self._velocidad - decremento)
            print(
                f"Velocidad del coche {self._marca} {self._modelo} "
                f"tras frenar: {self._velocidad} km/h"
            )

    # GETTER y SETTER del color
    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    # GETTER y SETTER de la marca
    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, marca):
        self._marca = marca

    # GETTER y SETTER del modelo
    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, modelo):
        self._modelo = modelo

    # GETTER y SETTER de la velocidad
    @property
    def velocidad(self):
        return self._velocidad

    @velocidad.setter
    def velocidad(self, velocidad):
        if 0 <= velocidad <= self._velocidad_maxima:
            self._velocidad = velocidad
        else:
            print(
                f"La velocidad debe estar entre 0 y "
                f"{self._velocidad_maxima} km/h."
            )

    # GETTER y SETTER de la velocidad máxima
    @property
    def velocidad_maxima(self):
        return self._velocidad_maxima

    @velocidad_maxima.setter
    def velocidad_maxima(self, velocidad_maxima):
        if velocidad_maxima > 0:
            self._velocidad_maxima = velocidad_maxima
            if self._velocidad > velocidad_maxima:
                self._velocidad = velocidad_maxima
        else:
            print("La velocidad máxima debe ser mayor que cero.")

    # GETTER y SETTER de la potencia
    @property
    def potencia(self):
        return self._potencia

    @potencia.setter
    def potencia(self, potencia):
        if potencia > 0:
            self._potencia = potencia
        else:
            print("La potencia debe ser mayor que cero.")

    # GETTER y SETTER de los asientos
    @property
    def asientos(self):
        return self._asientos

    @asientos.setter
    def asientos(self, asientos):
        if asientos > 0:
            self._asientos = asientos
        else:
            print("El número de asientos debe ser mayor que cero.")


# Crear los objetos
coche1 = Coches("blanco", "VW", "Golf", 220, 150, 5)
coche2 = Coches("rojo", "BMW", "Serie 3", 250, 200, 5)

# Mostrar los colores utilizando getters
print(f"El coche 1 es de color: {coche1.color}")
print(f"El coche 2 es de color: {coche2.color}")

# Acelerar el coche 1 diez veces
for i in range(1, 11):
    coche1.acelerar()

# Frenar el coche 1
coche1.frenar()

# Utilizar setters para modificar los atributos
coche1.color = "negro"
coche1.marca = "Volkswagen"
coche1.modelo = "Golf GTI"
coche1.velocidad = 80
coche1.potencia = 180
coche1.asientos = 5

# Mostrar los valores modificados utilizando getters
print("\n--- Datos actualizados del coche 1 ---")
print(f"Color: {coche1.color}")
print(f"Marca: {coche1.marca}")
print(f"Modelo: {coche1.modelo}")
print(f"Velocidad: {coche1.velocidad} km/h")
print(f"Velocidad máxima: {coche1.velocidad_maxima} km/h")
print(f"Potencia: {coche1.potencia} HP")
print(f"Asientos: {coche1.asientos}")