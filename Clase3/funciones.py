def sumar(a, b):

    resultado = a + b
    return resultado

resultado_suma = sumar(2, 3)
print(resultado_suma)
print(sumar(2,3))

def resta():
    resultado= 2- 3
    return resultado

print(resta())

def saludo(cantidad_saludos):
    lista_nombres = []
    for i in range(cantidad_saludos):

        nombre = input('Ingrese su nombre: ')
        print('hola', nombre)

        lista_nombres.append(nombre)
    
    print(lista_nombres)
    return lista_nombres

def orden(lista, sentido):
    lista.sort(reverse=sentido)
    return lista


nombres = saludo(int(input('Ingrese la cantidad de saludos: ')))

print(
    orden(nombres, True)
)
