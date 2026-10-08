"""  
 Programación Orinetada a Objetos POO o OOP

CLASES .- es como un molde a traves del cual se puede instanciar un objeto dentro de las clases se definen los atributos (propiedades / caracteristicas) y los métodos (funciones o acciones)

OBJETOS O INSTANCIAS .- son parte de una clase los objetos o instacias pertenecen a una clase, es decir para interacturar con la clase o clases y hacer uso de los atributos y metodos es necesario crear un objeto o objetos.
"""

#Ejemplo 1 Crear una clase (un molde para crear mas objetos)llamada Coches y apartir de la clase crear objetos o instancias (coche) con caracteristicas similares (marca,color,modelo,velocidad,potencia,asientos) y con los operaciones de acelerar y frenar. Que los atributos y metodos sean publicos.
#Muestre el color de los coches
#Que los operaciones disminuyan o aumenten la velocidad segun sea el caso y hay jugar con los metodos e imprimes la velocidad final

class coches:

    def __init__(self, color, marca, modelo, velocidad, potencia, asientos):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.potencia = potencia
        self.asientos = asientos

    def acelerar(self, incremento=10):
        self.velocidad += incremento
        print(f"velocidad del coche {self.marca} {self.modelo} tras acelerar: {self.velocidad} km/h")

    def frenar(self, decremento=10):
        self.velocidad = max(0, self.velocidad - decremento)
        print(f"velocidad del coche {self.marca} {self.modelo} tras frenar: {self.velocidad} km/h")
        


coche1 = coches('blanco', 'VW', 'Golf', 220, 150, 5)
coche2 = coches('rojo', 'BMW', 'Serie 3', 250, 200, 5)

print(f"El coche 1 es de color: {coche1.color}")
print(f"El coche 2 es de color: {coche2.color}")

for i in range(1, 11):
    coche1.acelerar()
