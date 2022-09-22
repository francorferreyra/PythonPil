import registro as registros

def menu():  
  print("""
------------------------ INICIO ------------------------
\t Por favor ingrese una opcion:
\t 1. Crear un producto
\t 2. Listar de productos
\t 3. Cambiar nombre del producto 
\t 4. Cambiar nombre de la empresa 
\t 5. Cambiar estado del producto (STOCK O SIN STOCK) 
\t 6. Cambiar descripcion del producto 
\t 7. Salir
""")
  print("-"*64)
  print('')

def validar_productos(lista):
  if len(lista) < 1:
    print('Debe cargar productos')
  else:
    for i in lista:
        i.listar_producto()

lista = []
opcion = -1
while opcion != '7':
    menu()
    opcion = input('Elija una opcion: ')

    if (opcion == '1'):
      cant = int(input('Ingrese cantidad de productos a cargar: '))
      for i in range(cant):
        registros.crear_producto(lista)
      print('Se han cargado productos')
      print('Total de productos cargados: ', + lista.__len__())
       
    elif (opcion == '2'):
      validar_productos(lista)
    
    elif (opcion == '3'):
      registros.cambiar_nombre(lista)

    elif (opcion == '4'):
      registros.cambiar_empresa(lista)

    elif (opcion == '5'):
      registros.cambiar_estado(lista)
      
    elif (opcion == '6'):
      registros.cambiar_bio(lista)

    else:
      print('¡Gracias por utilizar este programa!')   