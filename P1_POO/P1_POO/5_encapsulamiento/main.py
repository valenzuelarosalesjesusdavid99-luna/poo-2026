#Programa principal desde la que se manda llamar los objetos de la clase de coches

from coches import coches 

coche1 = coches('blanco', 'VW', 'Golf', 220, 150, 5)
coche2 = coches('rojo', 'BMW', 'Serie 3', 250, 200, 5)

coche1.acelerar()
coche1.acelerar()

print(coche1._velocidad)

coche1._velocidad = 300
print(coche1._velocidad)

coche1.setvelocidad(300)
print(coche1.getvelocidad())



