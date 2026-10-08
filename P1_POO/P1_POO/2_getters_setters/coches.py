"""  
 Programación Orinetada a Objetos POO o OOP

CLASES .- es como un molde a traves del cual se puede instanciar un objeto dentro de las clases se definen los atributos (propiedades / caracteristicas) y los métodos (funciones o acciones)

OBJETOS O INSTANCIAS .- son parte de una clase los objetos o instacias pertenecen a una clase, es decir para interacturar con la clase o clases y hacer uso de los atributos y metodos es necesario crear un objeto o objetos.

METODO CONSTRUCTOR.- Este metodo especial dentro de una clase y se utiliza para dar un valor a los atributos del objeto al crearlo, es el primer metodo que se ejecuta al crear el objeto y se manda llamar automaticamente al crearlo, es decir este metodo puede recibir parametros al momento de crear el objeto 

Cuando se crear un metodo constructor se utiliza la funcion _init_(), para que se llame automáticamente cada vez que se utiliza la clase para crear un nuevo objeto.

El self es un parámetro es una referencia a la instancia actual de la clase y se utiliza para acceder a variables que pertenecen a la clase.

No es necesario que tenga nombre self, puedes llamarlo como quieras, pero tiene que ser el primer parámetro de cualquier función de la clase. Es decir por regla se utiliza en la palabra self pero puede ser llamado con otro nombre por ejemplo: valor, abd, parametro, etc.

"""

#Ejemplo 1 Crear una clase (un molde para crear mas objetos)llamada Coches y apartir de la clase crear objetos o instancias (coche) con caracteristicas similares

class coches:

    def __init__(self, color, marca, modelo, velocidad, potencia, asientos):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.potencia = potencia
        self.asientos = asientos

    def acelerar(self, incremento=10):
        self._velocidad += incremento
        print(f"velocidad del coche {self.marca} {self.modelo} tras acelerar: {self._velocidad} km/h")

    def frenar(self, decremento=10):
        self._velocidad = max(0, self._velocidad - decremento)
        print(f"velocidad del coche {self.marca} {self.modelo} tras frenar: {self._velocidad} km/h")
        


coche1 = coches('blanco', 'VW', 'Golf', 220, 150, 5)
coche2 = coches('rojo', 'BMW', 'Serie 3', 250, 200, 5)

print(f"El coche 1 es de color: {coche1.color}")
print(f"El coche 2 es de color: {coche2.color}")

for i in range(1, 11):
    coche1.acelerar()


#Crear los metodos setters y getters .- estos metodos son importantes y necesarios en todos clases para que el programador interactue con los valores de los atributos a traves de estos metodos ... digamos que es la manera mas adecuada y recomendada para solicitar un valor (get) y/o para ingresar o cambiar un valor (set) a un atributo en particular de la clase a traves de un objeto. 
    # En teoria se deberia de crear un metodo Getters y Setters por   cada atributo que contenga la clase
        #   Los metodos get siempre regresan valor es decir el valor de la propiedad a traves del return
        #Por otro lado el metodo set siempre recibe parametros para cambiar o modificar el valor del atributo o propiedad en cuestion

def setvelocidad(self, velocidad):
    if velocidad >= 0:
        self._velocidad = velocidad
    else:
        print("La velocidad no puede ser negativa.")

def getvelocidad(self):
    return self._velocidad

def getmarca(self):
    return self._marca

def setmarca(self, marca):
    self._marca = marca
    
    def getmodelo(self):
        return self._modelo
    
    def setmodelo(self, modelo):
        self._modelo = modelo
        
        def getcolor(self):
            return self._color
        
        def setcolor(self, color):
            self._color = color
            
        def getpotencia(self):
            return self._potencia
        
        def setpotencia(self, potencia):
            self._potencia = potencia
            
        def getAsientos(self):
            return self._asientos
        
        def setAsientos(self, asientos):
            self._asientos = asientos
            
                