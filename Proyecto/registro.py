import random


class Libro():

    def __init__(self, nombre, empresa, estado, bio):
        self.nombre = nombre
        self.empresa = empresa
        self.estado = estado
        self.bio = bio

    def get_nombre(self): 
        return self.nombre

    def set_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre
        return self.nombre

    def get_empresa(self):
        return self.empresa

    def set_empresa(self, nuevo_empresa): 
        self.empresa = nuevo_empresa
        return self.empresa

    def get_estado(self):
        return self.estado

    def set_estado(self, nuevo_estado): 
        self.estado = nuevo_estado
        return self.estado

    def get_bio(self):
        return self.bio

    def set_bio(self, nueva_bio): 
        self.bio = nueva_bio
        return self.bio

    def listar_producto(self):  
        """
        Este metodo permite listar los productos ingresados
        """
        print('Nombre: ', self.nombre, end=' | ')
        print('Empresa: ', self.empresa, end=' | ')
        print('Estado: ', self.estado, end=' | ')
        print('Descripcion: ', self.bio)


# Funciones

def crear_producto(lista):
    """
    Esta funcion nos permite crear el objeto libro
    Args:
        lista (list): lista generica
    """
    lista_nombre = [
        'Cenicienta', 'Blanca Nieves', 'Tarzan', 'Ulises','Romeo y Julieta',
        'Homero'
    ]
    lista_empresa = [
        'Hermanos Green', 'Clyde Geronimi', 'Edgar Rice Burroughs',
        'Shakespeare'
    ]
    lista_estado = ['Disponible', 'Alquilado']
    lista_bio = ['Cuento Infantil']

    nombre = random.choice(lista_nombre)
    empresa = random.choice(lista_empresa)
    estado = random.choice(lista_estado)
    bio = random.choice(lista_bio)

    libro_creado = Libro(nombre, empresa, estado,
                         bio)  
    lista.append(libro_creado)  


def cambiar_nombre(lista):
    """
    Esta funcion nos permite cambiarle el nombre al libro

    Args:
        lista (list): lista generica
    """
    if len(lista) == 0:  
        print("La lista de libros esta vacia. Por favor agregue libros. ")
    else:
        for i, libro in enumerate(lista):
            print(i, "Nombre: ", libro.nombre, "|", "Empresa: ", libro.empresa,"|", "Estado: ", libro.estado, "|", "Descripcion: ", libro.bio)
        print('')
        flag = True
        flag_primero = False
        while flag:
            nombre_libro = input("Ingrese el nombre del libro a cambiar: ")

            for i, elemento in enumerate(lista):
                n = lista[i].get_nombre()
                if nombre_libro == n and flag_primero == False:
                    lista[i].nombre = input('Ingrese nuevo nombre: ')
                    flag_primero = True
                    flag = False
            if flag_primero == False:
                print('Nombre no valido, intente nuevamente.')



def cambiar_empresa(lista):
    """
    Esta funcion nos permite cambiar el nombre del autor a traves del nombre de productos

    Args:
        lista (list): lista generica
    """
    if len(lista) == 0:
        print("La lista de productoss esta vacia. Por favor agregue productoss. ")
    else:
        for i, productos in enumerate(lista):
            print(i, "Nombre: ", productos.nombre, "|", "Autor: ", productos.autor,"|", "Estado: ", productos.estado, "|", "Descripcion: ", productos.bio)
        print('')
        flag = True
        flag_primero = False
        while flag:
            nombre_productos = input(
                "Ingrese el nombre del productos que desea cambiarle el autor: ")
            for i, elemento in enumerate(lista):
                n = lista[i].get_nombre()
                if nombre_productos == n and flag_primero == False:
                    lista[i].autor = input('Ingrese nuevo nombre del autor: ').capitalize()
                    flag_primero = True
                    flag = False
            if flag_primero == False:
                print('Nombre no valido, intente nuevamente.')


def cambiar_estado(lista):
    """
    Esta funcion nos permite cambiar el estado al productos a traves del nombre de productos

    Args:
        lista (list): lista generica
    """
    if len(lista) == 0: 
        print("La lista de productoss esta vacia. Por favor agregue productoss. ")
    else:
        for i, productos in enumerate(lista):
            print(i, "Nombre: ", productos.nombre, "|", "Autor: ", productos.autor,"|", "Estado: ", productos.estado, "|", "Descripcion: ", productos.bio)
        print('')
        flag = True
        flag_primero = False
        while flag:
            nombre_productos = input("Ingrese el nombre del productos que desea cambiarle el estado: ")
            for i, elemento in enumerate(lista):
                n = lista[i].get_nombre()
                if nombre_productos == n and flag_primero == False:
                    lista[i].estado= input('Ingrese el nuevo estado del productos (DISPONIBLE O ALQUILADO): ').capitalize()
                    flag_primero = True
                    flag = False
            if flag_primero == False:
                print('Nombre no valido, intente nuevamente.')
  



def cambiar_bio(lista):
    """
    Esta funcion nos permite cambiar la descripcion del productos a traves del nombre de productos

    Args:
        lista (list): lista generica
    """
    if len(lista) == 0: 
        print("La lista de productos esta vacia. Por favor agregue productoss. ")
    else:
        for i, libro in enumerate(lista):
            print(i, "Nombre: ", libro.nombre, "|", "Autor: ", libro.autor,"|", "Estado: ", libro.estado, "|", "Descripcion: ", libro.bio)
        print('')
        flag = True
        flag_primero = False
        while flag:
            nombre_libro = input("Ingrese el nombre del libro que desea cambiarle la descripcion:  ")
            for i, elemento in enumerate(lista):
                n = lista[i].get_nombre()
                if nombre_libro == n and flag_primero == False:
                    lista[i].bio= input('Ingrese la nueva descripcion del libro: ').capitalize()
                    flag_primero = True
                    flag = False
            if flag_primero == False:
                print('Nombre no valido, intente nuevamente.')
