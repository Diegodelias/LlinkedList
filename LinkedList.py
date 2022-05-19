


class LinkedList :
    def __init__(self,numero):
        self.head = { 'numero' : numero, 'link' : None}
        self.tail = self.head
        self.largoLinkedList = 1

    def agregarFinal(self,num):
       # recorrer linkedList  mientras link != None:
       #cuando sea igual None
    #    nodoNuevo = {'numero' : num , 'link' : None}
    #    self.tail['link'] = nodoNuevo
    #    self.tail = nodoNuevo
    #    self.largoLinkedList = self.largoLinkedList + 1
    #    return self

        nodoNuevo = {'numero' : num , 'link' : None}
        if self.head is None:
            self.head = nodoNuevo
            return
        nodo = self.head
        while nodo['link'] is not None:
            nodo = nodo['link']
        nodo['link'] = nodoNuevo



    def agregarInicio(self,num):    
        #  nodoNuevo = {'numero' : num , 'link' : None}
        #  nodoNuevo['link'] = self.head
        #  self.head = nodoNuevo
        #  self.largoLinkedList = self.largoLinkedList + 1
        #  return self
        nodoNuevo = {'numero' : num , 'link' : None}
        nodoNuevo['link'] = self.head
        self.head = nodoNuevo




    #opcional
    def insertar(self,index, num):
        if (index >= self.largoLinkedList) :
            self.agregarFinal(num)
            return self.Listar()

        
        nodoNuevo = {'numero' : num , 'link' : None}

        nodoIzquierda = self.irPosicionInsertar(index-1)
        #guarda referencia a nodo a la derecha del nodo nuevo que se va a insertar
        nodoDerechaTemp = nodoIzquierda['link']
        #inserción nodo nuevo
        nodoIzquierda['link'] = nodoNuevo
        nodoNuevo['link'] = nodoDerechaTemp

        self.largoLinkedList = self.largoLinkedList + 1
        return self.Listar()

    def buscar(self,num):
        contador = 0
        res = False
        nodoActual = self.head
        while (nodoActual is not None ): 
            if  num == nodoActual['numero']:
                res =  True
            nodoActual = nodoActual['link']
            contador = contador + 1

        return res
           
        
             

        

    def Listar(self):
        contador = 0
        lista = []
        nodoActual = self.head
   
        while (nodoActual is not None ):
           
            lista.append(nodoActual['numero'])
            nodoActual = nodoActual['link']
            contador = contador + 1

        return lista


    def borrar(self,num):
      
        if self.head is None:
            print("lista vacia")
            return
        #borrar primer nodo
        if self.head['numero'] == num:
            self.head = self.head['link']
            return
        #borrar nodo intermedio o al final
        nodo = self.head
        while nodo['link'] is not None:

            if nodo['link']['numero'] == num:
               
                 break
               
            nodo = nodo['link']     
           
           
     
        if nodo['link'] is None:
            print("El numero ", num ,"no está en la lista")
        else:
           
            nodo['link'] = nodo['link']['link']

    def irPosicionInsertar(self,index):
        contador = 0
        nodoActual = self.head
        while (contador != index):
             nodoActual = nodoActual['link']
             contador = contador + 1

        return nodoActual



    


#obte



linkedList = LinkedList(3)
linkedList.agregarFinal(20)
linkedList.agregarFinal(55)
linkedList.agregarFinal(204)
print(linkedList.Listar())
linkedList.agregarInicio(7)
print(linkedList.Listar())
linkedList.borrar(204)
print(linkedList.Listar())
linkedList.agregarFinal(155)
print(linkedList.Listar())
linkedList.borrar(20)
print(linkedList.Listar())
linkedList.borrar(55)
print(linkedList.Listar())
# print(linkedList.Listar())
# linkedList.agregarFinal(79)
# print(linkedList.Listar())
# print(linkedList.buscar(557))
# linkedList.borrar(3)
# print(linkedList.Listar())

print(linkedList.buscar(77))

print(linkedList.buscar(3))



#print(linkedList.buscar(28))


# print(linkedList.Listar())

# linkedList.agregarInicio(79)



# print(linkedList.Listar())

# linkedList.insertar(2,107)

# print(linkedList.Listar())

# linkedList.borrar(2)

# print(linkedList.Listar())

# linkedList.borrar(3)





