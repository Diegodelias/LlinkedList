
def funcionMenu( diccionario ):
    print("""Seleccione una de las siguientes opciones: """)
    for k , v in diccionario.items():
        print('[',k,']',v )
    opcion= input("Ingrese número de la opción deseada  ")

        
        

   


    res = opcion if opcion.capitalize() in diccionario.keys() else "la opción ingresada es inexistente"

    return res.capitalize()
    