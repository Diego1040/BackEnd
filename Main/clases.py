

class Animales:
    def __init__(self, perro, gato):
        self.perro = perro
        self.gato = gato
    
    def MostrarAnimales(self, value):
        arr = []

        arr.append(value)

        return arr
    

class Gato(Animales):
    def __init__(self,perro,gato,nombre,edad,raza):
        super().__init__(perro,gato)
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
        self.gato = gato
    
    def ronroneo(self):
        print(f'el gato {self.nombre}, esta ronroneando')
    
    def __str__(self) -> str:
        return f'el gato tiene los siguientes atributos edad: {self.edad}, raza: {self.raza}, nombre:{self.nombre}'

class Perro(Animales):
    def __init__(self, perro,nombre,edad,raza):
        super().__init__(perro)
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
        self.perro = perro

g = Gato(True,True, 'Simon', 19, 'n/a')

print(g.__str__())





