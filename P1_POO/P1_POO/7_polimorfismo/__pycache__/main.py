#Programa principal desde la que se manda llamar los objetos de la clase de coches

from coches import coches, camiones, camionetas

coche1 = coches('blanco', 'VW', 'Golf', 220, 150, 5)
coche2 = coches('rojo', 'BMW', 'Serie 3', 250, 200, 5)

coche1.acelerar()
coche1.acelerar()

camion1 = camiones('blanco', 'VW', 'Golf', 220, 150, 5, 4, 1000)
camion2 = camiones('rojo', 'BMW', 'Serie 3', 250, 200, 5, 6, 2000)

camioneta1 = camionetas('ford', 'f150', 'negro', 220, 150, 5, 4, 1000, "delantera", True)
camioneta2 = camionetas("nissan", "azul", 2020, 150, 220, 14.6, 2000, "trasera", False)







