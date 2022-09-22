class Perro:

    especie = 'mamimeferos'
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza

    def ladrar(self):
        print('Guau')

    def jugar(self, objeto):
        print('El perro esta jugando', objeto)

    def saludar(self):
        print('Guau, mi nombre es', self.nombre)

perro_1 = Perro('Rex', 'Coli')
print(f'perro_1 -> {perro_1.raza}, {perro_1.nombre}')
perro_1.ladrar()
perro_1.jugar('Pelota')
perro_1.saludar()

perro_2 = Perro('Ana', 'Coli')
print(f'perro_1 -> {perro_1.raza}, {perro_1.nombre}')
perro_2.saludar()