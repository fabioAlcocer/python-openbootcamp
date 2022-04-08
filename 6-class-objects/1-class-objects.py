class Vehiculo:
  color = 'negro'
  ruedas = 4
  puertas = 4


class Coche(Vehiculo):
  velocidad = "249Km"
  cilindrada = "200cc"

coche = Coche()
print(coche.velocidad, coche.cilindrada)