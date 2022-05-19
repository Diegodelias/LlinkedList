from menus import *
from funciones import *

from LinkedList import *

seguir = True
while seguir:
    inicio = funcionMenu(menuPrincipal)

    if inicio =="1":
        opcion= input("Ingrese valor inicial (numero entero) para crear linked list ")
        linkedList = LinkedList(int(opcion))
        print(linkedList.Listar())
       