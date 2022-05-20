from menus import *
from funciones import *

from LinkedList import *
from BinaryTree import *

seguir = True
while seguir:
    inicio = funcionMenu(menuPrincipal)

    if inicio =="1":
        opcion= input("Ingrese valor inicial (numero entero) para crear linked list ")
        linkedList = LinkedList(int(opcion))
        print(linkedList.Listar())
        seguirMenuLinkedList = True
        while(seguirMenuLinkedList):
         opcionesLinkedList = funcionMenu(menuLinkedList)
         if opcionesLinkedList == '1' :
             opcionLinkedList= input("Ingrese numero para agregar a inicio de la linked list ")
             linkedList.agregarInicio(int(opcionLinkedList))
         if opcionesLinkedList == '2' :
             opcionLinkedList= input("Ingrese numero para agregar al final de la linked list ")
             linkedList.agregarFinal(int(opcionLinkedList))
         
         if opcionesLinkedList == '3' :
             opcionLinkedList= input("Ingrese el  numero que desea borrar de la linked list ")
             linkedList.borrar(int(opcionLinkedList))

         if opcionesLinkedList == '4' :
             opcionLinkedList= input("Ingrese el  numero que desea buscar en la linked list \n ( si lo encuentra se imprime True si no se encuentra imprime false) ")
             print(linkedList.buscar(int(opcionLinkedList)))


         if opcionesLinkedList == '5' :
            print(linkedList.Listar())

         if opcionesLinkedList == '6' :
             del linkedList
             seguirMenuLinkedList= False



    if inicio =="2":
        seguirMenuBinaryTrue = True
        

        tree = BinaryTree()
        while(seguirMenuBinaryTrue):
            opcionesBinaryTree = funcionMenu(menuBinaryTree)
            if  opcionesBinaryTree  == '1' :
             opcionbinaryTree= input("Ingrese numero para agregar al binary tree ")
             tree.insertar(int(opcionbinaryTree))

            if opcionesBinaryTree  == '2' :
             opcionbinaryTree= input("Ingrese numero a buscar  en el binary tree ")
             print(tree.buscar(int(opcionbinaryTree)))

            if opcionesBinaryTree  == '3' :
                opcionbinaryTree= input("Ingrese numero a borrar del binary tree ")
                tree.borrar(int(opcionbinaryTree))

            
            if opcionesBinaryTree  == '4' :
                tree.listar()

            if opcionesBinaryTree == '5' :
             del tree
             seguirMenuBinaryTrue = False

    if inicio =="3":
        seguir = False

            