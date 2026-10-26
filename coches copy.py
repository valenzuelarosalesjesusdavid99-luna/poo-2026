
class coches:

    def __init__(self, color, marca, modelo, velocidad, potencia, asientos):
        self._color = color
        self._marca = marca
        self._modelo = modelo
        self._velocidad = velocidad
        self._potencia = potencia
        self._asientos = asientos

    def acelerar(self, incremento=10):
        self._velocidad += incremento
        print(f"velocidad del coche {self._marca} {self._modelo} tras acelerar: {self._velocidad} km/h")

    def frenar(self, decremento=10):
        self._velocidad = max(0, self._velocidad - decremento)
        print(f"velocidad del coche {self._marca} {self._modelo} tras frenar: {self._velocidad} km/h")
        


coche1 = coches('blanco', 'VW', 'Golf', 220, 150, 5)
coche2 = coches('rojo', 'BMW', 'Serie 3', 250, 200, 5)

print(f"El coche 1 es de color: {coche1._color}")
print(f"El coche 2 es de color: {coche2._color}")

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
            
