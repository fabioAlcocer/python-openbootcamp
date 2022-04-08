class Alumno:
    def inicializar(self,nombre,nota):
        self.nombre=nombre
        self.nota=nota
 
 
    def imprimir(self):
      print("Nombre: ",self.nombre)
      print("Nota: ",self.nota)


    def resultado(self):
      if self.nota < 5:
        print("El alumno ha reprobado")
      else:
        print("El alumno ha aprobado")

alumnoUno = Alumno()
alumnoDos = Alumno()

alumnoUno.inicializar("Gus",8)
alumnoDos.inicializar("Nataly",2)

alumnoUno.imprimir()
alumnoUno.resultado()

alumnoDos.imprimir()
alumnoDos.resultado()