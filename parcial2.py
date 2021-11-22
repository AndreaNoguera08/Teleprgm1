class Animales():
  def __init__(self,nombre,raza,edad):
    self.nombre = nombre
    self.__edad = 0
    self.raza = raza
    self.vacuna = False
  
  @abstractmethod  
  def publicarEdad(self):
    return self.__edad
  
  def actualizarEdad(self, edad):
    if edad > 0:
      self.__edad = edad
      print("Edad = ", edad)
    else:
      print("Ingresar edad vàlida"
  

class Perro(Animales):
  __vacuna = "P1478"
  def vacuna(self, vacuna):
    if self.__vacuna == vacuna:
      super().vacunado = True
    else:
      print("El codigo de la vacuna es incorrecto")
 
class Gato(Animales):
  __vacuna = "G1478"
  def vacuna(self, vacuna):
    if self.__vacuna == vacuna:
      super().vacunado = True
    else:
      print("El codigo de la vacuna es incorrecto")
  
class Loro(Animales):
  __vacuna = "L1478"
  def vacuna(self, vacuna):
    if self.__vacuna == vacuna:
      super().vacunado = True
    else:
      print("El codigo de la vacuna es incorrecto")
  
perro = Perro("Rockie", "Macho", "Poodle")
perro.actualizarEdad(4)
perro.publicarEdad()
perro.vacunar("P1478")

gato = Gato("Tom", "Macho", "Siames")
gato.actualizarEdad(11)
gato.publicarEdad()
gato.publicarPeso()
gato.vacunar("G1478")

loro = Loro("duki", "Hembra", "Guacamaya")
loro.actualizarEdad(2)
loro.publicarEdad()
loro.publicarPeso()
loro.vacunar("L1478")

    

            

            
